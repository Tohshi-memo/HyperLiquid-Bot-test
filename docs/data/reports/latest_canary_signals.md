# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-28T02:22:35.953583+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.4445` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0386` n `12`; crypto_alt avg `0.2797` n `230`; crypto_major avg `0.1802` n `8`; equity avg `0.2089` n `102`; fx avg `-0.0338` n `6`; index avg `0.0773` n `25`; metal avg `0.0481` n `20`; unknown avg `0.097` n `774`
- 1h: commodity avg `-0.0752` n `12`; crypto_alt avg `0.5012` n `230`; crypto_major avg `0.3515` n `8`; equity avg `-0.1507` n `102`; fx avg `-0.0413` n `6`; index avg `-0.0025` n `25`; metal avg `0.0234` n `20`; unknown avg `-0.0515` n `773`
- 4h: commodity avg `-0.1466` n `12`; crypto_alt avg `-1.8231` n `230`; crypto_major avg `-1.7105` n `8`; equity avg `-1.488` n `102`; fx avg `0.0343` n `6`; index avg `-0.266` n `25`; metal avg `-0.2897` n `20`; unknown avg `1.9053` n `774`
- 24h: commodity avg `-0.9536` n `12`; crypto_alt avg `-3.8237` n `230`; crypto_major avg `-3.1503` n `8`; equity avg `-2.8838` n `102`; fx avg `-0.1275` n `6`; index avg `-0.6257` n `25`; metal avg `-0.3729` n `20`; unknown avg `1161.8666` n `757`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1915`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1908`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1745`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1435`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1411`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1377`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1326`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1232`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1119`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1093`, n `668`, weak_sample_signal
