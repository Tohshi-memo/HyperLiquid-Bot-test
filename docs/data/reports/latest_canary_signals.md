# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-06T14:07:23.376817+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0163` n `12`; crypto_alt avg `-0.0952` n `232`; crypto_major avg `-0.0663` n `8`; equity avg `-0.0715` n `134`; fx avg `0.0031` n `6`; index avg `-0.0212` n `26`; metal avg `-0.0074` n `20`; unknown avg `0.0659` n `790`
- 1h: commodity avg `0.0202` n `12`; crypto_alt avg `-0.1478` n `232`; crypto_major avg `-0.2609` n `8`; equity avg `-0.1661` n `134`; fx avg `0.0096` n `6`; index avg `-0.0248` n `26`; metal avg `-0.0083` n `20`; unknown avg `-0.0657` n `742`
- 4h: commodity avg `-0.0046` n `12`; crypto_alt avg `0.1796` n `232`; crypto_major avg `-0.0553` n `8`; equity avg `-0.1164` n `134`; fx avg `0.0177` n `6`; index avg `-0.0432` n `26`; metal avg `-0.0168` n `20`; unknown avg `67.4633` n `720`
- 24h: commodity avg `0.1318` n `12`; crypto_alt avg `1.9361` n `232`; crypto_major avg `1.3815` n `8`; equity avg `0.3474` n `134`; fx avg `-0.0179` n `6`; index avg `0.047` n `26`; metal avg `-0.0022` n `20`; unknown avg `0.1228` n `664`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1317`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1175`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1171`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.113`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1129`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1052`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0992`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0981`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0929`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0899`, n `668`, weak_sample_signal
