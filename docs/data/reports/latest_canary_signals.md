# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-14T23:21:35.708702+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-3.5072` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `3.3906` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-3.1923` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `-2.8315` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0179` n `13`; crypto_alt avg `0.473` n `239`; crypto_major avg `0.5749` n `8`; equity avg `0.05` n `162`; fx avg `-0.0031` n `6`; index avg `0.0116` n `27`; metal avg `0.038` n `20`; unknown avg `0.0571` n `1260`
- 1h: commodity avg `0.0274` n `13`; crypto_alt avg `-0.3264` n `239`; crypto_major avg `-0.4608` n `8`; equity avg `-0.1815` n `162`; fx avg `0.0109` n `6`; index avg `-0.0088` n `27`; metal avg `0.0547` n `20`; unknown avg `-0.3091` n `1228`
- 4h: commodity avg `0.1141` n `13`; crypto_alt avg `-3.1709` n `239`; crypto_major avg `-3.3931` n `8`; equity avg `-0.5616` n `162`; fx avg `0.0171` n `6`; index avg `-0.0025` n `27`; metal avg `-0.2008` n `20`; unknown avg `-0.4757` n `1176`
- 24h: commodity avg `0.0426` n `13`; crypto_alt avg `-8.8035` n `239`; crypto_major avg `-8.2896` n `8`; equity avg `-1.5915` n `162`; fx avg `0.0062` n `6`; index avg `-0.1211` n `27`; metal avg `-0.43` n `20`; unknown avg `46.4074` n `1070`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1399`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1236`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1149`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1133`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.111`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1041`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0916`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0911`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0887`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0878`, n `668`, weak_sample_signal
