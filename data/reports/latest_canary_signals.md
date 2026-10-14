# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-14T14:52:27.816196+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.9114` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-1.5598` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 1h_index_leads_crypto: score `1.237` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0002` n `13`; crypto_alt avg `0.0838` n `235`; crypto_major avg `0.0008` n `8`; equity avg `-0.0606` n `151`; fx avg `-0.0019` n `6`; index avg `-0.0221` n `26`; metal avg `-0.0831` n `20`; unknown avg `0.794` n `1136`
- 1h: commodity avg `-0.1137` n `13`; crypto_alt avg `-1.2372` n `235`; crypto_major avg `-1.3096` n `8`; equity avg `-0.4401` n `151`; fx avg `-0.03` n `6`; index avg `-0.0726` n `26`; metal avg `-0.1255` n `20`; unknown avg `-0.1268` n `1110`
- 4h: commodity avg `-0.2483` n `13`; crypto_alt avg `-2.2454` n `235`; crypto_major avg `-2.1804` n `8`; equity avg `-2.0394` n `151`; fx avg `-0.1071` n `6`; index avg `-0.269` n `26`; metal avg `-0.6206` n `20`; unknown avg `3.1501` n `1102`
- 24h: commodity avg `0.1267` n `13`; crypto_alt avg `-2.9126` n `235`; crypto_major avg `-2.4954` n `8`; equity avg `-2.0124` n `151`; fx avg `-0.1446` n `6`; index avg `-0.2517` n `26`; metal avg `-0.822` n `20`; unknown avg `1263.0864` n `981`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1023`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0936`, n `666`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0933`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.08`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0778`, n `666`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0703`, n `666`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0679`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0618`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0593`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0571`, n `666`, weak_sample_signal
