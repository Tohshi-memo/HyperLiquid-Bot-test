# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-03T11:37:22.682612+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0197` n `12`; crypto_alt avg `-0.494` n `228`; crypto_major avg `-0.418` n `8`; equity avg `-0.0119` n `72`; fx avg `-0.0171` n `6`; index avg `-0.0066` n `23`; metal avg `0.055` n `18`; unknown avg `-0.0027` n `420`
- 1h: commodity avg `-0.1634` n `12`; crypto_alt avg `0.0263` n `228`; crypto_major avg `-0.1367` n `8`; equity avg `0.3432` n `72`; fx avg `-0.0076` n `6`; index avg `0.0511` n `23`; metal avg `0.059` n `18`; unknown avg `0.953` n `420`
- 4h: commodity avg `0.2875` n `12`; crypto_alt avg `0.2545` n `228`; crypto_major avg `-0.1388` n `8`; equity avg `0.0982` n `72`; fx avg `-0.0177` n `6`; index avg `0.0359` n `23`; metal avg `0.1558` n `18`; unknown avg `0.9478` n `420`
- 24h: commodity avg `1.737` n `12`; crypto_alt avg `-0.6314` n `228`; crypto_major avg `-3.2308` n `8`; equity avg `0.6682` n `72`; fx avg `0.0347` n `6`; index avg `0.9046` n `23`; metal avg `-1.3141` n `18`; unknown avg `0.8587` n `409`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1023`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0703`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0703`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0636`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0635`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0614`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0607`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0597`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0496`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0473`, n `668`, weak_sample_signal
