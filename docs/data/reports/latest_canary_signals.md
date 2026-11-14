# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-14T04:52:27.561565+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.0066` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `2.0004` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-1.9934` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `-1.8083` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0023` n `13`; crypto_alt avg `-0.0127` n `239`; crypto_major avg `0.0272` n `8`; equity avg `-0.0342` n `162`; fx avg `-0.005` n `6`; index avg `-0.0005` n `27`; metal avg `-0.0068` n `20`; unknown avg `-0.1075` n `1256`
- 1h: commodity avg `-0.0011` n `13`; crypto_alt avg `0.0156` n `239`; crypto_major avg `0.3005` n `8`; equity avg `0.0232` n `162`; fx avg `0.0` n `6`; index avg `0.0023` n `27`; metal avg `0.0088` n `20`; unknown avg `1.8272` n `1248`
- 4h: commodity avg `-0.0479` n `13`; crypto_alt avg `-1.3964` n `239`; crypto_major avg `-2.0545` n `8`; equity avg `-0.2462` n `162`; fx avg `-0.0045` n `6`; index avg `-0.0541` n `27`; metal avg `-0.0611` n `20`; unknown avg `3.0599` n `1242`
- 24h: commodity avg `-0.1512` n `13`; crypto_alt avg `-0.1285` n `239`; crypto_major avg `-1.7791` n `8`; equity avg `-3.0398` n `162`; fx avg `-0.1038` n `6`; index avg `-0.2649` n `27`; metal avg `-0.596` n `20`; unknown avg `60.4239` n `1026`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1258`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.121`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1188`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.116`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1141`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1129`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1099`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1031`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0959`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0934`, n `668`, weak_sample_signal
