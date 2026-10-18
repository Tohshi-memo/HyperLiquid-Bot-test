# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-18T00:37:25.614619+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0124` n `13`; crypto_alt avg `-0.244` n `236`; crypto_major avg `-0.0528` n `8`; equity avg `-0.1374` n `151`; fx avg `0.0025` n `6`; index avg `-0.0121` n `26`; metal avg `0.0012` n `20`; unknown avg `-0.0755` n `1193`
- 1h: commodity avg `-0.0474` n `13`; crypto_alt avg `-0.0264` n `236`; crypto_major avg `0.169` n `8`; equity avg `-0.1359` n `151`; fx avg `0.0039` n `6`; index avg `-0.016` n `26`; metal avg `0.0165` n `20`; unknown avg `3.183` n `1185`
- 4h: commodity avg `-0.0432` n `13`; crypto_alt avg `-1.0449` n `236`; crypto_major avg `-0.6297` n `8`; equity avg `-0.9459` n `151`; fx avg `0.0051` n `6`; index avg `-0.1144` n `26`; metal avg `-0.0439` n `20`; unknown avg `0.1212` n `1179`
- 24h: commodity avg `-0.1324` n `13`; crypto_alt avg `-2.4013` n `236`; crypto_major avg `-1.0165` n `8`; equity avg `-0.9853` n `151`; fx avg `-0.0345` n `6`; index avg `-0.1259` n `26`; metal avg `-0.07` n `20`; unknown avg `4.161` n `1049`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1635`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1337`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1041`, n `666`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1025`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0954`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0933`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0771`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0765`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0731`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0586`, n `668`, weak_sample_signal
