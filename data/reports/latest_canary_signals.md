# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-18T01:37:31.781102+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0295` n `13`; crypto_alt avg `-0.0408` n `237`; crypto_major avg `0.0649` n `8`; equity avg `0.0601` n `151`; fx avg `-0.0026` n `6`; index avg `0.0108` n `26`; metal avg `-0.0095` n `20`; unknown avg `2.3071` n `1193`
- 1h: commodity avg `-0.0104` n `13`; crypto_alt avg `0.266` n `237`; crypto_major avg `0.3567` n `8`; equity avg `0.3196` n `151`; fx avg `-0.0038` n `6`; index avg `0.0447` n `26`; metal avg `0.0057` n `20`; unknown avg `0.3492` n `1191`
- 4h: commodity avg `-0.113` n `13`; crypto_alt avg `1.1908` n `236`; crypto_major avg `1.1826` n `8`; equity avg `1.055` n `151`; fx avg `0.0038` n `6`; index avg `0.106` n `26`; metal avg `0.0818` n `20`; unknown avg `4.1626` n `1185`
- 24h: commodity avg `-0.1811` n `13`; crypto_alt avg `-1.8361` n `236`; crypto_major avg `-0.4483` n `8`; equity avg `-0.7281` n `151`; fx avg `-0.0243` n `6`; index avg `-0.077` n `26`; metal avg `-0.0639` n `20`; unknown avg `3.7337` n `1049`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1628`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.132`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1029`, n `666`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1008`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.095`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.092`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0757`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0756`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0744`, n `666`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0576`, n `668`, weak_sample_signal
