# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-15T22:37:56.765564+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0022` n `13`; crypto_alt avg `-0.0389` n `236`; crypto_major avg `-0.0325` n `8`; equity avg `-0.1095` n `151`; fx avg `0.004` n `6`; index avg `-0.0105` n `26`; metal avg `-0.0029` n `20`; unknown avg `-0.0713` n `1136`
- 1h: commodity avg `0.0218` n `13`; crypto_alt avg `-0.0541` n `236`; crypto_major avg `-0.0124` n `8`; equity avg `0.0726` n `151`; fx avg `0.005` n `6`; index avg `-0.0035` n `26`; metal avg `-0.0104` n `20`; unknown avg `-0.2182` n `1102`
- 4h: commodity avg `-0.1454` n `13`; crypto_alt avg `0.1834` n `236`; crypto_major avg `0.2599` n `8`; equity avg `1.1387` n `151`; fx avg `-0.0182` n `6`; index avg `0.11` n `26`; metal avg `0.0778` n `20`; unknown avg `-0.0377` n `1020`
- 24h: commodity avg `-0.2386` n `13`; crypto_alt avg `0.8433` n `236`; crypto_major avg `1.0379` n `8`; equity avg `1.3223` n `151`; fx avg `0.1832` n `6`; index avg `0.03` n `26`; metal avg `0.4736` n `20`; unknown avg `24.951` n `910`

## Correlations

- risk_on_score -> index_forward_1h_return_pct: corr `-0.0975`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0938`, n `666`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.088`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0859`, n `666`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0757`, n `666`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0752`, n `666`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0745`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0721`, n `666`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0478`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0473`, n `668`, weak_sample_signal
