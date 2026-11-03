# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-03T02:22:26.721346+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.046` n `13`; crypto_alt avg `0.0653` n `239`; crypto_major avg `0.0945` n `8`; equity avg `-0.0129` n `157`; fx avg `-0.0051` n `6`; index avg `0.0121` n `27`; metal avg `-0.0289` n `20`; unknown avg `0.2354` n `1264`
- 1h: commodity avg `-0.016` n `13`; crypto_alt avg `-0.4227` n `239`; crypto_major avg `-0.312` n `8`; equity avg `0.0993` n `157`; fx avg `-0.0352` n `6`; index avg `-0.007` n `27`; metal avg `-0.1316` n `20`; unknown avg `18.8523` n `1258`
- 4h: commodity avg `0.0701` n `13`; crypto_alt avg `-0.4807` n `239`; crypto_major avg `-0.0528` n `8`; equity avg `0.4376` n `157`; fx avg `-0.0771` n `6`; index avg `0.0786` n `27`; metal avg `-0.1092` n `20`; unknown avg `-0.3756` n `1246`
- 24h: commodity avg `-1.1126` n `13`; crypto_alt avg `-3.1894` n `238`; crypto_major avg `-1.951` n `8`; equity avg `-3.0891` n `157`; fx avg `0.038` n `6`; index avg `-0.1528` n `27`; metal avg `-0.0034` n `20`; unknown avg `12.5802` n `1000`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `0.1682`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1674`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1592`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1552`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1271`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1182`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1153`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1144`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.11`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.106`, n `668`, weak_sample_signal
