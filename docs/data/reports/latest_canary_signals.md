# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-29T05:37:36.039094+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0018` n `12`; crypto_alt avg `0.1232` n `230`; crypto_major avg `0.1711` n `8`; equity avg `0.4009` n `102`; fx avg `0.0252` n `6`; index avg `0.1152` n `25`; metal avg `0.0183` n `20`; unknown avg `0.0408` n `777`
- 1h: commodity avg `-0.0413` n `12`; crypto_alt avg `0.2976` n `230`; crypto_major avg `0.3895` n `8`; equity avg `1.3563` n `102`; fx avg `0.0333` n `6`; index avg `0.2346` n `25`; metal avg `0.1134` n `20`; unknown avg `-0.089` n `777`
- 4h: commodity avg `-0.1968` n `12`; crypto_alt avg `-1.117` n `230`; crypto_major avg `0.0817` n `8`; equity avg `-0.8779` n `102`; fx avg `-0.1142` n `6`; index avg `-0.3314` n `25`; metal avg `-0.0173` n `20`; unknown avg `0.2435` n `777`
- 24h: commodity avg `-0.2322` n `12`; crypto_alt avg `-1.3474` n `230`; crypto_major avg `0.7021` n `8`; equity avg `-1.6122` n `102`; fx avg `-0.1624` n `6`; index avg `-0.2947` n `25`; metal avg `0.0653` n `20`; unknown avg `0.4609` n `758`

## Correlations

- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.1486`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1303`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1269`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1189`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.097`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0969`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0865`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0801`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0773`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0727`, n `668`, weak_sample_signal
