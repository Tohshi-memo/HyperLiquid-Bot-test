# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-27T23:22:31.425107+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.5171` - Index perps are stronger than crypto majors; possible risk-on canary.
- 1h_index_leads_crypto: score `1.1021` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0154` n `12`; crypto_alt avg `0.2237` n `230`; crypto_major avg `0.2164` n `8`; equity avg `0.0149` n `102`; fx avg `0.0004` n `6`; index avg `-0.0077` n `25`; metal avg `-0.0065` n `20`; unknown avg `0.0161` n `774`
- 1h: commodity avg `0.03` n `12`; crypto_alt avg `-1.345` n `230`; crypto_major avg `-1.1144` n `8`; equity avg `-0.3518` n `102`; fx avg `0.0031` n `6`; index avg `-0.0123` n `25`; metal avg `-0.0313` n `20`; unknown avg `1.2542` n `774`
- 4h: commodity avg `-0.0525` n `12`; crypto_alt avg `-1.5523` n `230`; crypto_major avg `-1.57` n `8`; equity avg `-0.4692` n `102`; fx avg `-0.0144` n `6`; index avg `-0.0529` n `25`; metal avg `-0.0964` n `20`; unknown avg `-0.0753` n `774`
- 24h: commodity avg `-0.717` n `12`; crypto_alt avg `-3.3639` n `230`; crypto_major avg `-2.8557` n `8`; equity avg `-2.0521` n `102`; fx avg `-0.0355` n `6`; index avg `-0.5093` n `25`; metal avg `-0.0056` n `20`; unknown avg `1161.7936` n `757`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.3237`, n `668`, moderate_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.2836`, n `668`, moderate_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1924`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1418`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1352`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1249`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0999`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0967`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0958`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0757`, n `668`, weak_sample_signal
