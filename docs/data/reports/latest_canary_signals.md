# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-28T06:07:18.059951+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.2239` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.153` n `12`; crypto_alt avg `0.0922` n `228`; crypto_major avg `-0.0004` n `8`; equity avg `0.1026` n `67`; fx avg `0.003` n `6`; index avg `0.0761` n `23`; metal avg `-0.1935` n `18`; unknown avg `0.0174` n `409`
- 1h: commodity avg `-0.3352` n `12`; crypto_alt avg `-0.3724` n `228`; crypto_major avg `-0.2062` n `8`; equity avg `0.9768` n `67`; fx avg `0.0203` n `6`; index avg `0.3757` n `23`; metal avg `0.6214` n `18`; unknown avg `-0.1157` n `409`
- 4h: commodity avg `0.3556` n `12`; crypto_alt avg `-2.8515` n `228`; crypto_major avg `-1.6083` n `8`; equity avg `-0.7191` n `67`; fx avg `-0.0817` n `6`; index avg `-0.3844` n `23`; metal avg `-0.3058` n `18`; unknown avg `-0.6619` n `409`
- 24h: commodity avg `0.0025` n `12`; crypto_alt avg `-5.0947` n `228`; crypto_major avg `-3.7709` n `8`; equity avg `-1.1143` n `67`; fx avg `-0.1341` n `6`; index avg `-0.9421` n `23`; metal avg `-1.9867` n `18`; unknown avg `-1.7243` n `408`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1894`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1736`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1731`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1697`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.164`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1578`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.155`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.152`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1408`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1357`, n `668`, weak_sample_signal
