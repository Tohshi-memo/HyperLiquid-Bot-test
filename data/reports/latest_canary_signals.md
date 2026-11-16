# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-16T15:37:28.937810+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 1h_commodity_crypto_divergence: score `-2.2599` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 1h_index_leads_crypto: score `2.1809` - Index perps are stronger than crypto majors; possible risk-on canary.
- 1h_crypto_metal_divergence: score `-2.0451` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0783` n `13`; crypto_alt avg `-0.244` n `239`; crypto_major avg `-0.2223` n `8`; equity avg `-0.4484` n `162`; fx avg `-0.0162` n `6`; index avg `-0.0316` n `27`; metal avg `-0.0157` n `20`; unknown avg `7.9608` n `1253`
- 1h: commodity avg `-0.0257` n `13`; crypto_alt avg `-1.8593` n `239`; crypto_major avg `-2.2856` n `8`; equity avg `-1.1905` n `162`; fx avg `-0.0156` n `6`; index avg `-0.1047` n `27`; metal avg `-0.2405` n `20`; unknown avg `4.3599` n `1247`
- 4h: commodity avg `-0.3854` n `13`; crypto_alt avg `-0.6985` n `239`; crypto_major avg `-0.9826` n `8`; equity avg `-1.9804` n `162`; fx avg `0.0021` n `6`; index avg `-0.1631` n `27`; metal avg `-0.2977` n `20`; unknown avg `54.7706` n `1233`
- 24h: commodity avg `-0.7281` n `13`; crypto_alt avg `-0.863` n `239`; crypto_major avg `-0.8557` n `8`; equity avg `-2.6535` n `162`; fx avg `-0.0341` n `6`; index avg `-0.2304` n `27`; metal avg `-0.1664` n `20`; unknown avg `253.4234` n `1038`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1342`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1212`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.116`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.109`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0994`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0959`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0954`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0949`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0834`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0798`, n `668`, weak_sample_signal
