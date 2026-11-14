# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-14T17:37:28.433023+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `2.0774` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_commodity_crypto_divergence: score `-2.0561` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `-1.9766` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `-1.5995` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0004` n `13`; crypto_alt avg `0.779` n `239`; crypto_major avg `1.0028` n `8`; equity avg `0.1551` n `162`; fx avg `0.004` n `6`; index avg `0.0177` n `27`; metal avg `0.01` n `20`; unknown avg `9.4502` n `1262`
- 1h: commodity avg `-0.0129` n `13`; crypto_alt avg `0.8421` n `239`; crypto_major avg `0.6052` n `8`; equity avg `0.2746` n `162`; fx avg `0.008` n `6`; index avg `0.0354` n `27`; metal avg `0.0468` n `20`; unknown avg `167.6105` n `1260`
- 4h: commodity avg `-0.0733` n `13`; crypto_alt avg `-2.3141` n `239`; crypto_major avg `-2.1294` n `8`; equity avg `-0.5299` n `162`; fx avg `0.0098` n `6`; index avg `-0.052` n `27`; metal avg `-0.1528` n `20`; unknown avg `324.7172` n `1250`
- 24h: commodity avg `-0.0009` n `13`; crypto_alt avg `-5.9658` n `239`; crypto_major avg `-5.7702` n `8`; equity avg `-1.3221` n `162`; fx avg `-0.0505` n `6`; index avg `-0.087` n `27`; metal avg `-0.3086` n `20`; unknown avg `1.8365` n `1096`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1409`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1208`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1154`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1148`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1119`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1018`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1011`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0964`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0934`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0917`, n `668`, weak_sample_signal
