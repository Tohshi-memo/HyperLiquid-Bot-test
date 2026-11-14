# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-14T22:52:28.035958+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-3.8727` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `3.756` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-3.5055` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `-3.2025` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0119` n `13`; crypto_alt avg `0.1621` n `239`; crypto_major avg `-0.0106` n `8`; equity avg `-0.0797` n `162`; fx avg `0.013` n `6`; index avg `-0.0056` n `27`; metal avg `0.0142` n `20`; unknown avg `0.2698` n `1232`
- 1h: commodity avg `0.0857` n `13`; crypto_alt avg `-0.346` n `239`; crypto_major avg `-0.7879` n `8`; equity avg `-0.2348` n `162`; fx avg `0.0134` n `6`; index avg `-0.0009` n `27`; metal avg `0.0465` n `20`; unknown avg `164.6082` n `1222`
- 4h: commodity avg `0.1044` n `13`; crypto_alt avg `-3.3518` n `239`; crypto_major avg `-3.7683` n `8`; equity avg `-0.5658` n `162`; fx avg `0.036` n `6`; index avg `-0.0123` n `27`; metal avg `-0.2628` n `20`; unknown avg `-0.3268` n `1176`
- 24h: commodity avg `0.0386` n `13`; crypto_alt avg `-9.3651` n `239`; crypto_major avg `-9.353` n `8`; equity avg `-1.7994` n `162`; fx avg `0.0143` n `6`; index avg `-0.1358` n `27`; metal avg `-0.4945` n `20`; unknown avg `46.525` n `1070`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1408`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1235`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1153`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1132`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1116`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1039`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0919`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0912`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0895`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0865`, n `668`, weak_sample_signal
