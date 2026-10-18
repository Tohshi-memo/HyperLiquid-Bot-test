# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-18T16:52:37.632870+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `-1.5134` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `1.4714` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0069` n `13`; crypto_alt avg `0.0049` n `237`; crypto_major avg `0.0126` n `8`; equity avg `0.0125` n `151`; fx avg `0.0031` n `6`; index avg `0.0072` n `26`; metal avg `-0.0057` n `20`; unknown avg `-0.2338` n `1194`
- 1h: commodity avg `0.0139` n `13`; crypto_alt avg `-0.1358` n `237`; crypto_major avg `-0.1353` n `8`; equity avg `0.009` n `151`; fx avg `-0.0035` n `6`; index avg `0.018` n `26`; metal avg `-0.0006` n `20`; unknown avg `-0.1888` n `1162`
- 4h: commodity avg `0.0427` n `13`; crypto_alt avg `-1.6222` n `237`; crypto_major avg `-1.566` n `8`; equity avg `-0.615` n `151`; fx avg `0.0014` n `6`; index avg `-0.0946` n `26`; metal avg `-0.0526` n `20`; unknown avg `-0.4555` n `1159`
- 24h: commodity avg `0.0205` n `13`; crypto_alt avg `-2.7107` n `236`; crypto_major avg `-1.1106` n `8`; equity avg `-0.8369` n `151`; fx avg `-0.0159` n `6`; index avg `-0.1019` n `26`; metal avg `-0.0456` n `20`; unknown avg `0.6157` n `1017`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.2112`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1409`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1286`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1138`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1082`, n `666`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0822`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0817`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0799`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.066`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0632`, n `668`, weak_sample_signal
