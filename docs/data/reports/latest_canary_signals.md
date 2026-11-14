# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-14T17:22:32.852393+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-3.0621` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `3.0595` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-2.9732` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `-2.3868` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0184` n `13`; crypto_alt avg `0.4451` n `239`; crypto_major avg `0.3207` n `8`; equity avg `0.1993` n `162`; fx avg `-0.0008` n `6`; index avg `0.0134` n `27`; metal avg `0.0505` n `20`; unknown avg `0.3468` n `1260`
- 1h: commodity avg `-0.0267` n `13`; crypto_alt avg `-0.1082` n `239`; crypto_major avg `-0.5513` n `8`; equity avg `-0.0015` n `162`; fx avg `0.0061` n `6`; index avg `0.0035` n `27`; metal avg `0.0671` n `20`; unknown avg `0.3132` n `1260`
- 4h: commodity avg `-0.0688` n `13`; crypto_alt avg `-3.196` n `239`; crypto_major avg `-3.1309` n `8`; equity avg `-0.7441` n `162`; fx avg `0.0056` n `6`; index avg `-0.0714` n `27`; metal avg `-0.1577` n `20`; unknown avg `159.9203` n `1252`
- 24h: commodity avg `-0.0193` n `13`; crypto_alt avg `-6.1391` n `239`; crypto_major avg `-6.1485` n `8`; equity avg `-1.1383` n `162`; fx avg `-0.0605` n `6`; index avg `-0.0691` n `27`; metal avg `-0.2875` n `20`; unknown avg `1.5197` n `1096`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1421`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1202`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1156`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1148`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1108`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1037`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1004`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0954`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0919`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0911`, n `668`, weak_sample_signal
