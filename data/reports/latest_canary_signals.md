# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-09T11:52:30.882717+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.1792` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0001` n `12`; crypto_alt avg `0.0237` n `228`; crypto_major avg `-0.1115` n `8`; equity avg `-0.0415` n `74`; fx avg `0.0091` n `6`; index avg `-0.0077` n `23`; metal avg `0.0557` n `18`; unknown avg `0.0273` n `547`
- 1h: commodity avg `0.2447` n `12`; crypto_alt avg `0.0317` n `228`; crypto_major avg `-0.319` n `8`; equity avg `0.188` n `74`; fx avg `0.0323` n `6`; index avg `0.0874` n `23`; metal avg `0.1722` n `18`; unknown avg `0.1096` n `547`
- 4h: commodity avg `-0.0936` n `12`; crypto_alt avg `-0.397` n `228`; crypto_major avg `-0.7888` n `8`; equity avg `0.3094` n `74`; fx avg `0.1833` n `6`; index avg `0.3904` n `23`; metal avg `0.4573` n `18`; unknown avg `-0.0538` n `547`
- 24h: commodity avg `-0.0207` n `12`; crypto_alt avg `-1.1867` n `228`; crypto_major avg `-0.7859` n `8`; equity avg `1.4906` n `74`; fx avg `0.1314` n `6`; index avg `0.7836` n `23`; metal avg `0.3517` n `18`; unknown avg `-3.0638` n `503`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1149`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1039`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0986`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0979`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0923`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.084`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0814`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.08`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0683`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0597`, n `668`, weak_sample_signal
