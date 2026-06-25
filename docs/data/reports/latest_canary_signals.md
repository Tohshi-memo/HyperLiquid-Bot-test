# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-25T18:52:34.278350+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0012` n `12`; crypto_alt avg `0.1424` n `228`; crypto_major avg `0.235` n `8`; equity avg `0.0939` n `86`; fx avg `0.0038` n `6`; index avg `0.008` n `23`; metal avg `0.0311` n `20`; unknown avg `0.1089` n `765`
- 1h: commodity avg `0.0138` n `12`; crypto_alt avg `-0.3512` n `228`; crypto_major avg `-0.1368` n `8`; equity avg `0.1967` n `86`; fx avg `0.0114` n `6`; index avg `0.0257` n `23`; metal avg `0.0402` n `20`; unknown avg `0.1075` n `765`
- 4h: commodity avg `0.4158` n `12`; crypto_alt avg `-0.3923` n `228`; crypto_major avg `0.3295` n `8`; equity avg `-0.2447` n `86`; fx avg `0.0763` n `6`; index avg `-0.0191` n `23`; metal avg `0.1323` n `20`; unknown avg `0.521` n `765`
- 24h: commodity avg `0.5036` n `12`; crypto_alt avg `0.3929` n `228`; crypto_major avg `0.5915` n `8`; equity avg `0.655` n `86`; fx avg `0.0825` n `6`; index avg `0.5365` n `23`; metal avg `0.8495` n `20`; unknown avg `0.6076` n `700`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1672`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1131`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1024`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0845`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0833`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0806`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0764`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0725`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0651`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0604`, n `668`, weak_sample_signal
