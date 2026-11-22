# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-22T07:52:32.216657+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0247` n `13`; crypto_alt avg `0.1493` n `239`; crypto_major avg `0.0091` n `8`; equity avg `0.0085` n `166`; fx avg `-0.0016` n `6`; index avg `-0.0013` n `27`; metal avg `0.0006` n `20`; unknown avg `0.0079` n `1261`
- 1h: commodity avg `0.004` n `13`; crypto_alt avg `0.0888` n `239`; crypto_major avg `0.1756` n `8`; equity avg `-0.0336` n `166`; fx avg `-0.0104` n `6`; index avg `0.0051` n `27`; metal avg `0.0141` n `20`; unknown avg `0.3479` n `1257`
- 4h: commodity avg `0.0048` n `13`; crypto_alt avg `0.2903` n `239`; crypto_major avg `-0.036` n `8`; equity avg `-0.0802` n `166`; fx avg `-0.0159` n `6`; index avg `0.0049` n `27`; metal avg `0.0321` n `20`; unknown avg `1.4142` n `1221`
- 24h: commodity avg `0.0054` n `13`; crypto_alt avg `1.733` n `239`; crypto_major avg `2.1568` n `8`; equity avg `0.6654` n `166`; fx avg `0.0597` n `6`; index avg `0.108` n `27`; metal avg `0.0828` n `20`; unknown avg `235.0909` n `1072`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1435`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1312`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1206`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1108`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1103`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1092`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1023`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0988`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0983`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0975`, n `668`, weak_sample_signal
