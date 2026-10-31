# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-31T01:52:29.148663+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0014` n `13`; crypto_alt avg `-0.2403` n `238`; crypto_major avg `-0.2086` n `8`; equity avg `-0.0285` n `156`; fx avg `0.0037` n `6`; index avg `-0.0001` n `27`; metal avg `-0.0025` n `20`; unknown avg `0.0253` n `1262`
- 1h: commodity avg `-0.02` n `13`; crypto_alt avg `-0.4357` n `238`; crypto_major avg `-0.2026` n `8`; equity avg `-0.0129` n `156`; fx avg `0.0051` n `6`; index avg `-0.0007` n `27`; metal avg `-0.0047` n `20`; unknown avg `7.657` n `1256`
- 4h: commodity avg `-0.1342` n `13`; crypto_alt avg `0.8324` n `238`; crypto_major avg `0.6847` n `8`; equity avg `0.3089` n `156`; fx avg `0.02` n `6`; index avg `0.027` n `27`; metal avg `0.0285` n `20`; unknown avg `4.1623` n `1249`
- 24h: commodity avg `-0.4389` n `13`; crypto_alt avg `4.7684` n `238`; crypto_major avg `1.7731` n `8`; equity avg `-1.5078` n `156`; fx avg `-0.1197` n `6`; index avg `-0.022` n `27`; metal avg `-0.6048` n `20`; unknown avg `3.6622` n `1018`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1524`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1471`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1352`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1317`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1231`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1215`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1159`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1104`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0946`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0777`, n `668`, weak_sample_signal
