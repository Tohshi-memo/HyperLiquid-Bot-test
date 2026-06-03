# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-03T19:37:34.879044+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0758` n `12`; crypto_alt avg `0.1399` n `228`; crypto_major avg `0.1295` n `8`; equity avg `0.118` n `73`; fx avg `0.018` n `6`; index avg `0.0808` n `23`; metal avg `0.0413` n `18`; unknown avg `0.7188` n `419`
- 1h: commodity avg `0.0357` n `12`; crypto_alt avg `0.1534` n `228`; crypto_major avg `-0.1951` n `8`; equity avg `-0.1668` n `73`; fx avg `0.047` n `6`; index avg `-0.0021` n `23`; metal avg `0.1111` n `18`; unknown avg `-0.1752` n `419`
- 4h: commodity avg `0.0691` n `12`; crypto_alt avg `-0.7227` n `228`; crypto_major avg `-0.7435` n `8`; equity avg `-0.2616` n `73`; fx avg `0.0091` n `6`; index avg `0.0073` n `23`; metal avg `-0.2904` n `18`; unknown avg `0.4933` n `419`
- 24h: commodity avg `0.9022` n `12`; crypto_alt avg `2.352` n `228`; crypto_major avg `-1.2836` n `8`; equity avg `-1.7897` n `72`; fx avg `0.06` n `6`; index avg `-0.1564` n `23`; metal avg `-1.8643` n `18`; unknown avg `1.0617` n `409`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1343`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1071`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0989`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0961`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0843`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0687`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0604`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0562`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0528`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0465`, n `668`, weak_sample_signal
