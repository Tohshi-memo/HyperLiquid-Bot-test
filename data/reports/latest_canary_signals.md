# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-20T00:07:26.238960+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0107` n `12`; crypto_alt avg `0.3482` n `228`; crypto_major avg `0.2832` n `8`; equity avg `0.0971` n `78`; fx avg `-0.0029` n `6`; index avg `-0.0062` n `23`; metal avg `-0.0009` n `18`; unknown avg `-0.0126` n `687`
- 1h: commodity avg `0.0553` n `12`; crypto_alt avg `0.5799` n `228`; crypto_major avg `0.3652` n `8`; equity avg `0.1955` n `78`; fx avg `0.0307` n `6`; index avg `0.0654` n `23`; metal avg `-0.0131` n `18`; unknown avg `-0.0945` n `679`
- 4h: commodity avg `0.0973` n `12`; crypto_alt avg `0.5648` n `228`; crypto_major avg `0.3562` n `8`; equity avg `0.2997` n `78`; fx avg `0.0016` n `6`; index avg `0.0535` n `23`; metal avg `0.0525` n `18`; unknown avg `-0.1189` n `679`
- 24h: commodity avg `0.3731` n `12`; crypto_alt avg `-3.2106` n `228`; crypto_major avg `-4.1985` n `8`; equity avg `0.9899` n `78`; fx avg `-0.0919` n `6`; index avg `0.2814` n `23`; metal avg `-4.1111` n `18`; unknown avg `-0.4075` n `564`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0835`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0767`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0747`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0687`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0649`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0606`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0603`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0588`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0578`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0542`, n `668`, weak_sample_signal
