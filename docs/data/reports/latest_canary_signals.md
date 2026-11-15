# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-15T01:07:29.926296+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `-1.6885` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_crypto_metal_divergence: score `-1.636` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `1.5833` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0035` n `13`; crypto_alt avg `-0.204` n `239`; crypto_major avg `-0.6336` n `8`; equity avg `-0.1722` n `162`; fx avg `0.0059` n `6`; index avg `-0.0156` n `27`; metal avg `-0.0279` n `20`; unknown avg `0.1556` n `1256`
- 1h: commodity avg `0.0016` n `13`; crypto_alt avg `-0.6252` n `239`; crypto_major avg `-0.9793` n `8`; equity avg `-0.3105` n `162`; fx avg `-0.0005` n `6`; index avg `-0.0421` n `27`; metal avg `-0.1221` n `20`; unknown avg `-0.0479` n `1258`
- 4h: commodity avg `0.1191` n `13`; crypto_alt avg `-0.0119` n `239`; crypto_major avg `-1.5802` n `8`; equity avg `0.1083` n `162`; fx avg `0.0167` n `6`; index avg `0.0031` n `27`; metal avg `0.0558` n `20`; unknown avg `205.7087` n `1216`
- 24h: commodity avg `-0.0278` n `13`; crypto_alt avg `-8.7682` n `239`; crypto_major avg `-8.9863` n `8`; equity avg `-1.6147` n `162`; fx avg `0.031` n `6`; index avg `-0.1602` n `27`; metal avg `-0.5592` n `20`; unknown avg `47.1141` n `1070`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1415`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1205`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1142`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1121`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1115`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0899`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0888`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0859`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0846`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0829`, n `668`, weak_sample_signal
