# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-22T15:52:25.681654+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0107` n `12`; crypto_alt avg `-0.1768` n `230`; crypto_major avg `-0.2314` n `8`; equity avg `0.0109` n `121`; fx avg `0.009` n `6`; index avg `0.0047` n `25`; metal avg `0.002` n `20`; unknown avg `-0.0351` n `794`
- 1h: commodity avg `-0.0063` n `12`; crypto_alt avg `-0.0307` n `230`; crypto_major avg `-0.0615` n `8`; equity avg `-0.0417` n `121`; fx avg `0.0149` n `6`; index avg `0.0083` n `25`; metal avg `0.0113` n `20`; unknown avg `0.1147` n `794`
- 4h: commodity avg `-0.056` n `12`; crypto_alt avg `-0.7331` n `230`; crypto_major avg `-0.5219` n `8`; equity avg `-0.0632` n `121`; fx avg `-0.0133` n `6`; index avg `0.0035` n `25`; metal avg `0.0161` n `20`; unknown avg `0.1164` n `794`
- 24h: commodity avg `-0.0929` n `12`; crypto_alt avg `-0.3351` n `230`; crypto_major avg `1.7726` n `8`; equity avg `-0.8295` n `121`; fx avg `0.0614` n `6`; index avg `-0.1288` n `25`; metal avg `-0.1015` n `20`; unknown avg `1.7318` n `777`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `0.1555`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.145`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1353`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.132`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1232`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1222`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1197`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1195`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1157`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0951`, n `668`, weak_sample_signal
