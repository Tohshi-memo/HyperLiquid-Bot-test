# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-14T23:07:23.476438+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-4.1727` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `4.0451` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-3.826` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `-3.4253` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0072` n `13`; crypto_alt avg `-0.2242` n `239`; crypto_major avg `-0.0287` n `8`; equity avg `-0.0075` n `162`; fx avg `-0.0006` n `6`; index avg `-0.0036` n `27`; metal avg `0.0174` n `20`; unknown avg `39.789` n `1256`
- 1h: commodity avg `0.0877` n `13`; crypto_alt avg `-0.2072` n `239`; crypto_major avg `-0.3182` n `8`; equity avg `-0.1008` n `162`; fx avg `0.0199` n `6`; index avg `-0.0061` n `27`; metal avg `0.0497` n `20`; unknown avg `0.8413` n `1226`
- 4h: commodity avg `0.1009` n `13`; crypto_alt avg `-3.7883` n `239`; crypto_major avg `-4.0718` n `8`; equity avg `-0.6465` n `162`; fx avg `0.0249` n `6`; index avg `-0.0267` n `27`; metal avg `-0.2458` n `20`; unknown avg `3.2273` n `1176`
- 24h: commodity avg `0.0145` n `13`; crypto_alt avg `-9.2495` n `239`; crypto_major avg `-8.9401` n `8`; equity avg `-1.6804` n `162`; fx avg `0.0019` n `6`; index avg `-0.1323` n `27`; metal avg `-0.4633` n `20`; unknown avg `46.7785` n `1070`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1404`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1235`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1151`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1132`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1114`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1039`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0918`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0911`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0891`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0872`, n `668`, weak_sample_signal
