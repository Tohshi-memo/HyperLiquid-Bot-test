# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-10T05:07:31.330517+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0336` n `12`; crypto_alt avg `0.096` n `230`; crypto_major avg `0.0761` n `8`; equity avg `0.0473` n `112`; fx avg `0.0147` n `6`; index avg `0.0286` n `25`; metal avg `0.0284` n `20`; unknown avg `-0.2129` n `785`
- 1h: commodity avg `-0.0693` n `12`; crypto_alt avg `0.0176` n `230`; crypto_major avg `0.0144` n `8`; equity avg `-0.0443` n `112`; fx avg `0.0366` n `6`; index avg `0.0013` n `25`; metal avg `0.065` n `20`; unknown avg `0.5376` n `785`
- 4h: commodity avg `-0.0875` n `12`; crypto_alt avg `0.0281` n `230`; crypto_major avg `0.1164` n `8`; equity avg `0.0228` n `112`; fx avg `0.0477` n `6`; index avg `0.0501` n `25`; metal avg `0.1538` n `20`; unknown avg `1.3125` n `785`
- 24h: commodity avg `0.2794` n `12`; crypto_alt avg `0.4693` n `230`; crypto_major avg `-0.074` n `8`; equity avg `-0.2449` n `112`; fx avg `0.1224` n `6`; index avg `0.0134` n `25`; metal avg `-0.1009` n `20`; unknown avg `-0.2324` n `752`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1939`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1447`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.141`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1295`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.1256`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1226`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1157`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1031`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1004`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0969`, n `668`, weak_sample_signal
