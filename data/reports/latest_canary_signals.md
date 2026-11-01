# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-01T16:22:29.619319+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0038` n `13`; crypto_alt avg `0.0294` n `238`; crypto_major avg `0.0188` n `8`; equity avg `0.0298` n `156`; fx avg `0.0111` n `6`; index avg `0.0236` n `27`; metal avg `0.0016` n `20`; unknown avg `-0.0428` n `1263`
- 1h: commodity avg `-0.0721` n `13`; crypto_alt avg `-0.2736` n `238`; crypto_major avg `-0.0711` n `8`; equity avg `0.0254` n `156`; fx avg `0.0173` n `6`; index avg `0.0099` n `27`; metal avg `-0.0008` n `20`; unknown avg `-0.2884` n `1243`
- 4h: commodity avg `-0.0784` n `13`; crypto_alt avg `0.1877` n `238`; crypto_major avg `0.2311` n `8`; equity avg `0.0822` n `156`; fx avg `0.0238` n `6`; index avg `0.0619` n `27`; metal avg `0.0068` n `20`; unknown avg `-0.3367` n `1245`
- 24h: commodity avg `0.0225` n `13`; crypto_alt avg `-0.6142` n `238`; crypto_major avg `0.184` n `8`; equity avg `0.4655` n `156`; fx avg `0.0097` n `6`; index avg `0.0975` n `27`; metal avg `0.039` n `20`; unknown avg `1.4443` n `1010`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `0.1498`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1462`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1436`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.143`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1414`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1283`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.102`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0945`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0836`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0813`, n `668`, weak_sample_signal
