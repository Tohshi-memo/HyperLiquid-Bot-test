# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-27T11:22:23.497462+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0551` n `12`; crypto_alt avg `-0.0369` n `231`; crypto_major avg `-0.0127` n `8`; equity avg `-0.0967` n `127`; fx avg `-0.0075` n `6`; index avg `-0.0016` n `26`; metal avg `0.0294` n `20`; unknown avg `-0.0089` n `792`
- 1h: commodity avg `0.0583` n `12`; crypto_alt avg `-0.2199` n `231`; crypto_major avg `-0.2974` n `8`; equity avg `-0.0642` n `127`; fx avg `-0.0114` n `6`; index avg `0.0197` n `26`; metal avg `0.0683` n `20`; unknown avg `-0.0093` n `792`
- 4h: commodity avg `0.3332` n `12`; crypto_alt avg `0.7875` n `231`; crypto_major avg `1.2672` n `8`; equity avg `0.3504` n `127`; fx avg `-0.0151` n `6`; index avg `0.0404` n `26`; metal avg `-0.0411` n `20`; unknown avg `0.1238` n `791`
- 24h: commodity avg `0.4991` n `12`; crypto_alt avg `0.9951` n `231`; crypto_major avg `1.6418` n `8`; equity avg `1.7382` n `127`; fx avg `-0.0929` n `6`; index avg `0.2813` n `26`; metal avg `-0.3462` n `20`; unknown avg `0.7739` n `775`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1187`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1056`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0946`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0932`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.091`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0851`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0763`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0666`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.065`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0629`, n `668`, weak_sample_signal
