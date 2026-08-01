# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-01T19:07:28.943457+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.1782` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0116` n `12`; crypto_alt avg `0.3892` n `230`; crypto_major avg `0.3889` n `8`; equity avg `-0.0168` n `102`; fx avg `-0.0027` n `6`; index avg `0.0034` n `25`; metal avg `0.0301` n `20`; unknown avg `0.1215` n `782`
- 1h: commodity avg `-0.0411` n `12`; crypto_alt avg `-0.5558` n `230`; crypto_major avg `-0.5624` n `8`; equity avg `-0.1654` n `102`; fx avg `0.0048` n `6`; index avg `-0.0115` n `25`; metal avg `0.0277` n `20`; unknown avg `1.8161` n `782`
- 4h: commodity avg `0.0897` n `12`; crypto_alt avg `-1.0755` n `230`; crypto_major avg `-1.2141` n `8`; equity avg `-0.3501` n `102`; fx avg `-0.0063` n `6`; index avg `-0.0359` n `25`; metal avg `0.0102` n `20`; unknown avg `2.4534` n `782`
- 24h: commodity avg `0.5808` n `12`; crypto_alt avg `-0.9194` n `230`; crypto_major avg `-1.4891` n `8`; equity avg `-1.2641` n `102`; fx avg `-0.1607` n `6`; index avg `-0.1432` n `25`; metal avg `-0.0815` n `20`; unknown avg `4.2763` n `764`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1126`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0992`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0854`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0839`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0778`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0707`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0695`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0679`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0666`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.066`, n `668`, weak_sample_signal
