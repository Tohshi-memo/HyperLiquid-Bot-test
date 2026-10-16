# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-16T15:37:44.610612+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `-1.6798` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `1.5398` - Index perps are stronger than crypto majors; possible risk-on canary.
- 1h_index_leads_crypto: score `1.0493` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0533` n `13`; crypto_alt avg `0.59` n `236`; crypto_major avg `0.3903` n `8`; equity avg `0.2381` n `151`; fx avg `0.005` n `6`; index avg `0.0527` n `26`; metal avg `0.0033` n `20`; unknown avg `5.0647` n `1158`
- 1h: commodity avg `0.1034` n `13`; crypto_alt avg `-0.9458` n `236`; crypto_major avg `-1.1833` n `8`; equity avg `-0.9532` n `151`; fx avg `-0.0252` n `6`; index avg `-0.134` n `26`; metal avg `-0.108` n `20`; unknown avg `6.8619` n `1072`
- 4h: commodity avg `-0.3306` n `13`; crypto_alt avg `-1.5833` n `236`; crypto_major avg `-1.7797` n `8`; equity avg `-1.9863` n `151`; fx avg `0.0011` n `6`; index avg `-0.2399` n `26`; metal avg `-0.0999` n `20`; unknown avg `6.9785` n `998`
- 24h: commodity avg `-0.4897` n `13`; crypto_alt avg `0.1139` n `236`; crypto_major avg `-0.7886` n `8`; equity avg `-1.0869` n `151`; fx avg `0.0319` n `6`; index avg `-0.1702` n `26`; metal avg `0.1663` n `20`; unknown avg `17.426` n `906`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1089`, n `666`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1001`, n `666`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0894`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0851`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0811`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0801`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.08`, n `666`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0799`, n `666`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0788`, n `666`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0714`, n `668`, weak_sample_signal
