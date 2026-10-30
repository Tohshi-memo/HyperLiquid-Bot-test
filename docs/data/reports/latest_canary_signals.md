# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-30T21:22:25.298189+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0154` n `13`; crypto_alt avg `0.2773` n `238`; crypto_major avg `0.114` n `8`; equity avg `-0.0394` n `156`; fx avg `-0.0384` n `6`; index avg `-0.0238` n `27`; metal avg `-0.0012` n `20`; unknown avg `0.0221` n `1261`
- 1h: commodity avg `-0.1071` n `13`; crypto_alt avg `0.5648` n `238`; crypto_major avg `0.1731` n `8`; equity avg `-0.0295` n `156`; fx avg `-0.0012` n `6`; index avg `-0.0285` n `27`; metal avg `-0.0006` n `20`; unknown avg `-0.0578` n `1229`
- 4h: commodity avg `-0.4528` n `13`; crypto_alt avg `0.2958` n `238`; crypto_major avg `-0.2396` n `8`; equity avg `0.6583` n `156`; fx avg `-0.0063` n `6`; index avg `0.0244` n `27`; metal avg `-0.046` n `20`; unknown avg `1.3359` n `1149`
- 24h: commodity avg `0.0469` n `13`; crypto_alt avg `-0.3889` n `238`; crypto_major avg `-1.7875` n `8`; equity avg `-3.1374` n `156`; fx avg `-0.1095` n `6`; index avg `-0.3058` n `27`; metal avg `-0.9773` n `20`; unknown avg `0.8886` n `1014`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1721`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1648`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1493`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1454`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1409`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1238`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1225`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1096`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0867`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0749`, n `668`, weak_sample_signal
