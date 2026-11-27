# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-27T00:07:21.647675+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0066` n `13`; crypto_alt avg `0.1194` n `239`; crypto_major avg `0.174` n `8`; equity avg `0.194` n `168`; fx avg `0.0188` n `6`; index avg `0.033` n `27`; metal avg `0.0248` n `20`; unknown avg `1.0989` n `1239`
- 1h: commodity avg `0.0203` n `13`; crypto_alt avg `0.21` n `239`; crypto_major avg `0.1917` n `8`; equity avg `0.2055` n `168`; fx avg `0.0375` n `6`; index avg `0.033` n `27`; metal avg `0.0503` n `20`; unknown avg `63.6576` n `1245`
- 4h: commodity avg `0.0537` n `13`; crypto_alt avg `-0.3301` n `239`; crypto_major avg `-0.4417` n `8`; equity avg `-0.0346` n `168`; fx avg `0.0395` n `6`; index avg `0.0259` n `27`; metal avg `-0.0112` n `20`; unknown avg `68.5268` n `1143`
- 24h: commodity avg `0.1428` n `13`; crypto_alt avg `0.9223` n `239`; crypto_major avg `0.4086` n `8`; equity avg `0.4685` n `168`; fx avg `0.0312` n `6`; index avg `0.0676` n `27`; metal avg `-0.0054` n `20`; unknown avg `208.6869` n `991`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1153`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1097`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1047`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.102`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.099`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0967`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0874`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0869`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0848`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0824`, n `668`, weak_sample_signal
