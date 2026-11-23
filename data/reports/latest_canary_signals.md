# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-23T13:52:36.321479+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.245` n `13`; crypto_alt avg `-0.2721` n `239`; crypto_major avg `-0.226` n `8`; equity avg `-0.336` n `166`; fx avg `-0.0652` n `6`; index avg `-0.0673` n `27`; metal avg `-0.1209` n `20`; unknown avg `170.2757` n `1266`
- 1h: commodity avg `-0.3601` n `13`; crypto_alt avg `-0.1214` n `239`; crypto_major avg `-0.0304` n `8`; equity avg `0.1493` n `166`; fx avg `-0.0705` n `6`; index avg `0.0107` n `27`; metal avg `-0.0527` n `20`; unknown avg `37.9547` n `1260`
- 4h: commodity avg `-0.5771` n `13`; crypto_alt avg `-0.2409` n `239`; crypto_major avg `0.0492` n `8`; equity avg `-0.7686` n `166`; fx avg `-0.1591` n `6`; index avg `-0.0952` n `27`; metal avg `-0.2325` n `20`; unknown avg `0.0497` n `1252`
- 24h: commodity avg `-1.2534` n `13`; crypto_alt avg `0.3877` n `239`; crypto_major avg `1.2038` n `8`; equity avg `1.3911` n `166`; fx avg `0.0606` n `6`; index avg `-0.0331` n `27`; metal avg `0.1784` n `20`; unknown avg `-0.3996` n `1061`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `-0.1528`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1505`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1402`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1389`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1377`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1291`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1273`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1256`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1255`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1202`, n `668`, weak_sample_signal
