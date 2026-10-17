# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-17T21:52:26.492514+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 1h_index_leads_crypto: score `1.1099` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0093` n `13`; crypto_alt avg `0.3962` n `236`; crypto_major avg `0.2895` n `8`; equity avg `0.6014` n `151`; fx avg `-0.0016` n `6`; index avg `0.0319` n `26`; metal avg `0.0248` n `20`; unknown avg `3.9031` n `1193`
- 1h: commodity avg `0.0291` n `13`; crypto_alt avg `-1.6458` n `236`; crypto_major avg `-1.245` n `8`; equity avg `-1.0641` n `151`; fx avg `-0.0047` n `6`; index avg `-0.1351` n `26`; metal avg `-0.0913` n `20`; unknown avg `1.9191` n `1185`
- 4h: commodity avg `-0.0018` n `13`; crypto_alt avg `-0.6753` n `236`; crypto_major avg `-0.6497` n `8`; equity avg `-0.9023` n `151`; fx avg `-0.0092` n `6`; index avg `-0.1198` n `26`; metal avg `-0.0751` n `20`; unknown avg `1.3693` n `1131`
- 24h: commodity avg `0.0162` n `13`; crypto_alt avg `-2.6526` n `236`; crypto_major avg `-1.527` n `8`; equity avg `-1.1106` n `151`; fx avg `-0.0329` n `6`; index avg `-0.1579` n `26`; metal avg `-0.1335` n `20`; unknown avg `4.4238` n `1049`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1678`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1369`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1095`, n `666`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1066`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0979`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0968`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.08`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0774`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0725`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0676`, n `668`, weak_sample_signal
