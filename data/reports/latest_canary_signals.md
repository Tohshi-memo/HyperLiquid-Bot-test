# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-08T13:48:37.899631+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.7733` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-1.6949` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.018` n `13`; crypto_alt avg `-0.1805` n `235`; crypto_major avg `-0.2157` n `8`; equity avg `-0.0566` n `150`; fx avg `0.009` n `6`; index avg `0.0038` n `26`; metal avg `0.0156` n `20`; unknown avg `-0.1081` n `1077`
- 1h: commodity avg `-0.066` n `13`; crypto_alt avg `0.0007` n `235`; crypto_major avg `-0.2498` n `8`; equity avg `-0.0998` n `150`; fx avg `0.009` n `6`; index avg `0.0363` n `26`; metal avg `0.0521` n `20`; unknown avg `20.0004` n `1073`
- 4h: commodity avg `0.0353` n `13`; crypto_alt avg `-1.6854` n `235`; crypto_major avg `-1.7683` n `8`; equity avg `-0.5157` n `150`; fx avg `0.0235` n `6`; index avg `0.005` n `26`; metal avg `-0.0734` n `20`; unknown avg `2.5684` n `1067`
- 24h: commodity avg `0.6542` n `13`; crypto_alt avg `-0.0977` n `235`; crypto_major avg `-2.4897` n `8`; equity avg `-1.2016` n `150`; fx avg `0.0595` n `6`; index avg `-0.0554` n `26`; metal avg `0.1177` n `20`; unknown avg `0.2973` n `970`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `0.1528`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1378`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1371`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1354`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1325`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1323`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1308`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1258`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1257`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1174`, n `668`, weak_sample_signal
