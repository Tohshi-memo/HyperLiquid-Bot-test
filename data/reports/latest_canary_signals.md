# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-27T00:52:22.675246+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0178` n `13`; crypto_alt avg `0.1271` n `239`; crypto_major avg `0.1464` n `8`; equity avg `0.0232` n `168`; fx avg `-0.0032` n `6`; index avg `0.0025` n `27`; metal avg `-0.071` n `20`; unknown avg `0.121` n `1263`
- 1h: commodity avg `0.0405` n `13`; crypto_alt avg `0.3381` n `239`; crypto_major avg `0.4122` n `8`; equity avg `0.0933` n `168`; fx avg `-0.0389` n `6`; index avg `-0.0036` n `27`; metal avg `-0.0354` n `20`; unknown avg `0.9152` n `1245`
- 4h: commodity avg `0.0981` n `13`; crypto_alt avg `-0.1261` n `239`; crypto_major avg `-0.2951` n `8`; equity avg `-0.185` n `168`; fx avg `-0.0169` n `6`; index avg `-0.0154` n `27`; metal avg `-0.0895` n `20`; unknown avg `375.221` n `1171`
- 24h: commodity avg `0.1762` n `13`; crypto_alt avg `0.701` n `239`; crypto_major avg `0.5461` n `8`; equity avg `-0.3959` n `168`; fx avg `-0.0188` n `6`; index avg `-0.0647` n `27`; metal avg `0.0197` n `20`; unknown avg `210.6375` n `995`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.114`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1097`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1045`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1002`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0999`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0956`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0904`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0876`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0835`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0823`, n `668`, weak_sample_signal
