# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-17T22:22:29.970433+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0152` n `13`; crypto_alt avg `0.1123` n `236`; crypto_major avg `0.1571` n `8`; equity avg `0.024` n `151`; fx avg `-0.0013` n `6`; index avg `0.0054` n `26`; metal avg `0.0022` n `20`; unknown avg `0.0557` n `1193`
- 1h: commodity avg `-0.0048` n `13`; crypto_alt avg `-0.9989` n `236`; crypto_major avg `-0.7536` n `8`; equity avg `-0.7181` n `151`; fx avg `-0.0028` n `6`; index avg `-0.1049` n `26`; metal avg `-0.0745` n `20`; unknown avg `0.6463` n `1191`
- 4h: commodity avg `-0.0522` n `13`; crypto_alt avg `-0.8885` n `236`; crypto_major avg `-0.6356` n `8`; equity avg `-0.9348` n `151`; fx avg `0.0015` n `6`; index avg `-0.1076` n `26`; metal avg `-0.0718` n `20`; unknown avg `0.3036` n `1139`
- 24h: commodity avg `0.0278` n `13`; crypto_alt avg `-2.5334` n `236`; crypto_major avg `-1.3867` n `8`; equity avg `-0.9084` n `151`; fx avg `-0.0303` n `6`; index avg `-0.1162` n `26`; metal avg `-0.1138` n `20`; unknown avg `4.3604` n `1049`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1668`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1397`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1086`, n `666`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1082`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0978`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.097`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0803`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0795`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0724`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0677`, n `668`, weak_sample_signal
