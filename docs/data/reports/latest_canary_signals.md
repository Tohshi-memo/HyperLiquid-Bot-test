# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-31T22:30:44.037242+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0649` n `12`; crypto_alt avg `0.0564` n `228`; crypto_major avg `0.1295` n `8`; equity avg `0.0425` n `69`; fx avg `0.0008` n `6`; index avg `0.0318` n `23`; metal avg `0.0435` n `18`; unknown avg `0.6531` n `421`
- 1h: commodity avg `0.575` n `12`; crypto_alt avg `0.6937` n `228`; crypto_major avg `0.4334` n `8`; equity avg `-0.0477` n `69`; fx avg `0.0005` n `6`; index avg `0.0955` n `23`; metal avg `-0.0277` n `18`; unknown avg `0.6763` n `421`
- 4h: commodity avg `0.3429` n `12`; crypto_alt avg `1.5706` n `228`; crypto_major avg `1.0337` n `8`; equity avg `0.0883` n `69`; fx avg `-0.0177` n `6`; index avg `0.2054` n `23`; metal avg `-0.0278` n `18`; unknown avg `1.5052` n `421`
- 24h: commodity avg `0.9339` n `12`; crypto_alt avg `1.0428` n `228`; crypto_major avg `0.8377` n `8`; equity avg `0.8316` n `69`; fx avg `-0.0353` n `6`; index avg `0.3535` n `23`; metal avg `-0.1446` n `18`; unknown avg `1.833` n `401`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `0.3177`, n `668`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.2256`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1672`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1648`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1325`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.131`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1167`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0976`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0941`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0916`, n `668`, weak_sample_signal
