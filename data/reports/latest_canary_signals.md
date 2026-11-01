# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-01T15:22:37.561365+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0186` n `13`; crypto_alt avg `-0.0673` n `238`; crypto_major avg `-0.0869` n `8`; equity avg `-0.0051` n `156`; fx avg `-0.0139` n `6`; index avg `0.0071` n `27`; metal avg `-0.0015` n `20`; unknown avg `0.2709` n `1263`
- 1h: commodity avg `-0.0098` n `13`; crypto_alt avg `-0.1696` n `238`; crypto_major avg `-0.0676` n `8`; equity avg `0.0003` n `156`; fx avg `0.0015` n `6`; index avg `0.0279` n `27`; metal avg `-0.0055` n `20`; unknown avg `2.6319` n `1257`
- 4h: commodity avg `0.0289` n `13`; crypto_alt avg `0.0416` n `238`; crypto_major avg `-0.0407` n `8`; equity avg `0.0` n `156`; fx avg `-0.003` n `6`; index avg `0.0478` n `27`; metal avg `-0.0059` n `20`; unknown avg `0.0437` n `1253`
- 24h: commodity avg `0.0565` n `13`; crypto_alt avg `-0.0504` n `238`; crypto_major avg `0.4237` n `8`; equity avg `0.4552` n `156`; fx avg `-0.0248` n `6`; index avg `0.0856` n `27`; metal avg `0.0467` n `20`; unknown avg `3.7708` n `1018`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `0.1476`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1448`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1421`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1408`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1406`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1246`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1013`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.095`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0825`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0807`, n `668`, weak_sample_signal
