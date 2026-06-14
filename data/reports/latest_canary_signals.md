# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-14T10:22:32.836509+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0191` n `12`; crypto_alt avg `0.2144` n `228`; crypto_major avg `0.2144` n `8`; equity avg `0.0805` n `74`; fx avg `0.0127` n `6`; index avg `0.0634` n `23`; metal avg `0.0091` n `18`; unknown avg `0.1228` n `645`
- 1h: commodity avg `-0.0624` n `12`; crypto_alt avg `0.5461` n `228`; crypto_major avg `0.6069` n `8`; equity avg `0.2714` n `74`; fx avg `0.0115` n `6`; index avg `0.0662` n `23`; metal avg `0.0112` n `18`; unknown avg `0.1637` n `629`
- 4h: commodity avg `-0.1963` n `12`; crypto_alt avg `0.1032` n `228`; crypto_major avg `0.2097` n `8`; equity avg `0.3719` n `74`; fx avg `0.0023` n `6`; index avg `0.1361` n `23`; metal avg `0.0198` n `18`; unknown avg `2.1525` n `625`
- 24h: commodity avg `-0.7289` n `12`; crypto_alt avg `0.588` n `228`; crypto_major avg `1.3057` n `8`; equity avg `0.9855` n `74`; fx avg `-0.018` n `6`; index avg `0.3661` n `23`; metal avg `0.3019` n `18`; unknown avg `-0.9182` n `592`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1129`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0961`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.088`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0707`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0706`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0666`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0639`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.062`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0611`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.061`, n `668`, weak_sample_signal
