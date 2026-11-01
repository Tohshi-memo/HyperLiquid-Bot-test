# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-01T13:07:27.874408+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0078` n `13`; crypto_alt avg `0.2033` n `238`; crypto_major avg `0.0709` n `8`; equity avg `0.0299` n `156`; fx avg `0.0044` n `6`; index avg `0.0025` n `27`; metal avg `0.0107` n `20`; unknown avg `0.0289` n `1257`
- 1h: commodity avg `-0.0037` n `13`; crypto_alt avg `0.1912` n `238`; crypto_major avg `-0.1442` n `8`; equity avg `-0.0391` n `156`; fx avg `0.0069` n `6`; index avg `-0.0026` n `27`; metal avg `0.0038` n `20`; unknown avg `0.2382` n `1257`
- 4h: commodity avg `-0.0251` n `13`; crypto_alt avg `0.0961` n `238`; crypto_major avg `-0.2524` n `8`; equity avg `0.0002` n `156`; fx avg `-0.0049` n `6`; index avg `0.0009` n `27`; metal avg `0.0284` n `20`; unknown avg `0.2751` n `1237`
- 24h: commodity avg `-0.0162` n `13`; crypto_alt avg `0.7421` n `238`; crypto_major avg `0.2975` n `8`; equity avg `0.5885` n `156`; fx avg `-0.0158` n `6`; index avg `0.0443` n `27`; metal avg `0.0794` n `20`; unknown avg `3.4179` n `1018`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1464`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1385`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1325`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.131`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1309`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1146`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0967`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0931`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0838`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0815`, n `668`, weak_sample_signal
