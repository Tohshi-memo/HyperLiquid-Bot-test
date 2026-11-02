# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-02T00:52:28.368471+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0008` n `13`; crypto_alt avg `0.1899` n `238`; crypto_major avg `0.1144` n `8`; equity avg `0.0503` n `156`; fx avg `0.0291` n `6`; index avg `0.0458` n `27`; metal avg `0.0501` n `20`; unknown avg `-0.1892` n `1263`
- 1h: commodity avg `0.0747` n `13`; crypto_alt avg `-0.3589` n `238`; crypto_major avg `-0.2053` n `8`; equity avg `0.1833` n `156`; fx avg `0.1168` n `6`; index avg `0.1602` n `27`; metal avg `-0.0058` n `20`; unknown avg `2.645` n `1249`
- 4h: commodity avg `0.0477` n `13`; crypto_alt avg `-0.0923` n `238`; crypto_major avg `0.2173` n `8`; equity avg `0.4211` n `156`; fx avg `0.1163` n `6`; index avg `0.194` n `27`; metal avg `0.1342` n `20`; unknown avg `5.1526` n `1219`
- 24h: commodity avg `-0.033` n `13`; crypto_alt avg `-0.6419` n `238`; crypto_major avg `-0.0796` n `8`; equity avg `0.7175` n `156`; fx avg `0.1141` n `6`; index avg `0.2667` n `27`; metal avg `0.1655` n `20`; unknown avg `3.5125` n `1128`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1632`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1625`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1564`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1557`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1298`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1212`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1206`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1083`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1028`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1005`, n `668`, weak_sample_signal
