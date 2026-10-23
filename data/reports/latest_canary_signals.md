# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-23T23:07:28.368206+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.1842` - Index perps are stronger than crypto majors; possible risk-on canary.
- 1h_index_leads_crypto: score `1.1147` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0484` n `13`; crypto_alt avg `-0.0613` n `237`; crypto_major avg `-0.0169` n `8`; equity avg `-0.0524` n `152`; fx avg `0.0035` n `6`; index avg `-0.0063` n `26`; metal avg `0.0336` n `20`; unknown avg `0.0157` n `1228`
- 1h: commodity avg `0.0396` n `13`; crypto_alt avg `-2.0637` n `237`; crypto_major avg `-1.1657` n `8`; equity avg `-0.3861` n `152`; fx avg `0.024` n `6`; index avg `-0.051` n `26`; metal avg `-0.0746` n `20`; unknown avg `3.9538` n `1230`
- 4h: commodity avg `0.2145` n `13`; crypto_alt avg `-2.4496` n `237`; crypto_major avg `-1.2101` n `8`; equity avg `-0.3766` n `152`; fx avg `0.0252` n `6`; index avg `-0.0259` n `26`; metal avg `-0.1042` n `20`; unknown avg `0.7103` n `1134`
- 24h: commodity avg `0.5934` n `13`; crypto_alt avg `-1.5394` n `237`; crypto_major avg `-0.7279` n `8`; equity avg `0.959` n `152`; fx avg `-0.0431` n `6`; index avg `0.0204` n `26`; metal avg `-0.2318` n `20`; unknown avg `199.4344` n `1024`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.2026`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1852`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1586`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1531`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1502`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.149`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.128`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1273`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1223`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1199`, n `668`, weak_sample_signal
