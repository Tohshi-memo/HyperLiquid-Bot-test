# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-11T21:22:31.688958+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0119` n `13`; crypto_alt avg `-0.1056` n `239`; crypto_major avg `-0.058` n `8`; equity avg `0.0016` n `161`; fx avg `-0.0141` n `6`; index avg `-0.0098` n `27`; metal avg `0.0169` n `20`; unknown avg `-0.307` n `1258`
- 1h: commodity avg `0.0728` n `13`; crypto_alt avg `-0.1192` n `239`; crypto_major avg `0.0856` n `8`; equity avg `-0.1152` n `161`; fx avg `-0.0189` n `6`; index avg `-0.0386` n `27`; metal avg `-0.0286` n `20`; unknown avg `3.5557` n `1218`
- 4h: commodity avg `-0.1683` n `13`; crypto_alt avg `-1.3657` n `239`; crypto_major avg `-0.8303` n `8`; equity avg `-1.0093` n `161`; fx avg `0.0081` n `6`; index avg `-0.0871` n `27`; metal avg `-0.2374` n `20`; unknown avg `2.2882` n `1210`
- 24h: commodity avg `0.2059` n `13`; crypto_alt avg `0.4261` n `239`; crypto_major avg `0.9156` n `8`; equity avg `4.5779` n `161`; fx avg `-0.1476` n `6`; index avg `0.4384` n `27`; metal avg `-0.061` n `20`; unknown avg `5.3244` n `1141`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1419`, n `669`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1245`, n `669`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1237`, n `669`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1231`, n `669`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1193`, n `669`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1102`, n `669`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1082`, n `669`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1009`, n `669`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1004`, n `669`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0945`, n `669`, weak_sample_signal
