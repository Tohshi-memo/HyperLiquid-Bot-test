# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-14T16:52:26.610428+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-3.213` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `3.1909` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-3.094` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `-2.2977` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 1h_index_leads_crypto: score `1.006` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0227` n `13`; crypto_alt avg `-0.0836` n `239`; crypto_major avg `-0.1793` n `8`; equity avg `-0.0378` n `162`; fx avg `0.0108` n `6`; index avg `-0.0077` n `27`; metal avg `0.0098` n `20`; unknown avg `0.1603` n `1262`
- 1h: commodity avg `-0.0358` n `13`; crypto_alt avg `-1.4323` n `239`; crypto_major avg `-1.0589` n `8`; equity avg `-0.4074` n `162`; fx avg `0.0063` n `6`; index avg `-0.0529` n `27`; metal avg `0.0347` n `20`; unknown avg `0.2116` n `1254`
- 4h: commodity avg `-0.0821` n `13`; crypto_alt avg `-3.5056` n `239`; crypto_major avg `-3.2951` n `8`; equity avg `-0.9974` n `162`; fx avg `0.0112` n `6`; index avg `-0.1042` n `27`; metal avg `-0.2011` n `20`; unknown avg `0.8058` n `1250`
- 24h: commodity avg `0.0335` n `13`; crypto_alt avg `-6.5845` n `239`; crypto_major avg `-6.0325` n `8`; equity avg `-0.9815` n `162`; fx avg `-0.0599` n `6`; index avg `-0.0469` n `27`; metal avg `-0.2728` n `20`; unknown avg `1.6767` n `1096`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1404`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.12`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1155`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1146`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1103`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1044`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1041`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0977`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0961`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0918`, n `668`, weak_sample_signal
