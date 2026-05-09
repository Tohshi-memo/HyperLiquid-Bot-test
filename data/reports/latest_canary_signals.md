# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-09T10:22:16.531470+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0401` n `12`; crypto_alt avg `0.1196` n `228`; crypto_major avg `0.0145` n `8`; equity avg `-0.0017` n `65`; fx avg `0.0042` n `5`; index avg `-0.0023` n `23`; metal avg `-0.0191` n `18`; unknown avg `-0.1104` n `376`
- 1h: commodity avg `-0.0386` n `12`; crypto_alt avg `-0.1943` n `228`; crypto_major avg `-0.237` n `8`; equity avg `0.027` n `65`; fx avg `0.0042` n `5`; index avg `-0.074` n `23`; metal avg `-0.0425` n `18`; unknown avg `0.0193` n `376`
- 4h: commodity avg `-0.0285` n `12`; crypto_alt avg `-1.1177` n `228`; crypto_major avg `-0.4688` n `8`; equity avg `0.0635` n `65`; fx avg `0.0051` n `5`; index avg `0.0287` n `23`; metal avg `-0.045` n `18`; unknown avg `-0.0371` n `376`
- 24h: commodity avg `-0.2691` n `12`; crypto_alt avg `3.1003` n `228`; crypto_major avg `2.0874` n `8`; equity avg `2.7807` n `65`; fx avg `-0.0457` n `5`; index avg `1.15` n `23`; metal avg `-0.1494` n `18`; unknown avg `0.4441` n `355`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1195`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1148`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0913`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0834`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0821`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.08`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0775`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0672`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0668`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0661`, n `668`, weak_sample_signal
