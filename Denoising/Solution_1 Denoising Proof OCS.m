function denoised_audio = Solution_1(input_audio_file)
    % Load input audio file
    speech_with_beeps = importdata(input_audio_file);

    % Parameters
    fs = 8000;
    num_samples = 160;
    OverlapLength = floor(num_samples * 0.5);
    win_fun = hamming(num_samples);

    % STFT
    [S, f, t] = stft(speech_with_beeps, fs, 'Window', win_fun, 'OverlapLength', OverlapLength);
    pos_freq_index = find(f >= 0, 1);
    S = S(pos_freq_index:end, :);

    % Denoising Parameters
    threshold_factor = 3.3;
    gain_factor = -4;

    %Logic
    s_mean = mean(10*log10(abs(S)), 2);
    s_stddev = std(10*log10(abs(S)));
    threshold = s_mean + threshold_factor * s_stddev;
    energy_matrix = 10*log10(abs(S));
    for i = 1:size(S, 1)
        for j = 1:size(S, 2)
            if (energy_matrix(i, j) > threshold(i))
                energy_matrix(i, j) = energy_matrix(i, j)*(gain_factor);
            end
        end
    end

    % Inverse STFT
    nfft = num_samples;
    amp_matrix = 10.^((energy_matrix)/10);
    S_unit = S./abs(S);
    S_final = amp_matrix.*S_unit;
    speech_clean = inverse_stft(S_final, win_fun, OverlapLength, nfft, fs);

    % Output denoised audio
    denoised_audio = speech_clean;
end

function s = inverse_stft(specgram, window, overlap, fft_size, fs)
    s_length = (size(specgram, 2) - 1) * overlap + fft_size;
    s = zeros(s_length, 1);
    for n = 1:size(specgram, 2)
        start_index = (n - 1) * overlap + 1;
        end_index = start_index + fft_size - 1;
        segment = real(ifft(specgram(:, n), fft_size));
        s(start_index:end_index) = s(start_index:end_index) + segment .* window;
    end
    s = s';
end

