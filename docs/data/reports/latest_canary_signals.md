# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-09T09:22:30.798238+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.034` n `12`; crypto_alt avg `-0.0849` n `229`; crypto_major avg `-0.0884` n `8`; equity avg `0.0314` n `91`; fx avg `0.007` n `6`; index avg `-0.0087` n `25`; metal avg `0.0061` n `20`; unknown avg `-0.0295` n `764`
- 1h: commodity avg `0.1315` n `12`; crypto_alt avg `-0.1928` n `229`; crypto_major avg `-0.2168` n `8`; equity avg `-0.199` n `91`; fx avg `-0.0163` n `6`; index avg `-0.0594` n `25`; metal avg `0.0041` n `20`; unknown avg `-0.0955` n `764`
- 4h: commodity avg `-0.2924` n `12`; crypto_alt avg `0.4459` n `229`; crypto_major avg `0.3468` n `8`; equity avg `0.6671` n `91`; fx avg `0.1149` n `6`; index avg `0.0848` n `25`; metal avg `0.646` n `20`; unknown avg `0.074` n `748`
- 24h: commodity avg `-0.7204` n `12`; crypto_alt avg `1.9401` n `229`; crypto_major avg `1.1568` n `8`; equity avg `4.0771` n `91`; fx avg `0.1235` n `6`; index avg `0.6047` n `25`; metal avg `0.6476` n `20`; unknown avg `0.7047` n `741`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.1004`, n `669`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0987`, n `669`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0704`, n `669`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0676`, n `669`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0665`, n `669`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0638`, n `669`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0636`, n `669`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0588`, n `669`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0586`, n `669`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0566`, n `669`, weak_sample_signal
