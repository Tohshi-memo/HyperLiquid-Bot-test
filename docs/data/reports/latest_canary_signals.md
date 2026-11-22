# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-22T13:07:28.053486+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0054` n `13`; crypto_alt avg `-0.0714` n `239`; crypto_major avg `-0.124` n `8`; equity avg `0.0314` n `166`; fx avg `-0.0005` n `6`; index avg `0.0054` n `27`; metal avg `-0.0088` n `20`; unknown avg `0.3005` n `1253`
- 1h: commodity avg `-0.0226` n `13`; crypto_alt avg `-0.1241` n `239`; crypto_major avg `-0.3416` n `8`; equity avg `-0.0789` n `166`; fx avg `0.0013` n `6`; index avg `0.0194` n `27`; metal avg `-0.037` n `20`; unknown avg `0.7531` n `1257`
- 4h: commodity avg `0.0221` n `13`; crypto_alt avg `0.9397` n `239`; crypto_major avg `0.9326` n `8`; equity avg `0.5323` n `166`; fx avg `-0.0038` n `6`; index avg `0.0697` n `27`; metal avg `0.069` n `20`; unknown avg `63.9604` n `1149`
- 24h: commodity avg `-0.0054` n `13`; crypto_alt avg `1.7703` n `239`; crypto_major avg `1.7107` n `8`; equity avg `1.4751` n `166`; fx avg `0.0035` n `6`; index avg `0.1866` n `27`; metal avg `0.0794` n `20`; unknown avg `0.5546` n `1086`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `-0.1428`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1427`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1352`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1292`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1257`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1199`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1156`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1145`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1134`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1134`, n `668`, weak_sample_signal
