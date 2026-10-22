# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-22T19:52:30.376882+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0192` n `13`; crypto_alt avg `-0.1118` n `237`; crypto_major avg `-0.0673` n `8`; equity avg `0.331` n `151`; fx avg `0.0002` n `6`; index avg `0.0537` n `26`; metal avg `0.0326` n `20`; unknown avg `405.0975` n `1233`
- 1h: commodity avg `-0.0077` n `13`; crypto_alt avg `-0.1542` n `237`; crypto_major avg `-0.0301` n `8`; equity avg `0.2189` n `151`; fx avg `-0.0077` n `6`; index avg `0.022` n `26`; metal avg `-0.033` n `20`; unknown avg `392.1125` n `1223`
- 4h: commodity avg `0.2586` n `13`; crypto_alt avg `-0.3071` n `237`; crypto_major avg `-0.4404` n `8`; equity avg `-0.8658` n `151`; fx avg `0.0102` n `6`; index avg `-0.1031` n `26`; metal avg `-0.2006` n `20`; unknown avg `2.6619` n `1215`
- 24h: commodity avg `0.5645` n `13`; crypto_alt avg `-5.3507` n `237`; crypto_major avg `-3.9003` n `8`; equity avg `-5.606` n `151`; fx avg `-0.1685` n `6`; index avg `-0.6785` n `26`; metal avg `-0.9777` n `20`; unknown avg `3.4907` n `926`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.2085`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1874`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1561`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1492`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1432`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.14`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1305`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1238`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1098`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1011`, n `668`, weak_sample_signal
