# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-03T12:37:25.502040+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0223` n `12`; crypto_alt avg `0.3936` n `228`; crypto_major avg `0.263` n `8`; equity avg `-0.2118` n `72`; fx avg `0.0487` n `6`; index avg `-0.0754` n `23`; metal avg `-0.3723` n `18`; unknown avg `-0.0904` n `420`
- 1h: commodity avg `-0.0407` n `12`; crypto_alt avg `-0.0271` n `228`; crypto_major avg `-0.0895` n `8`; equity avg `-0.3701` n `72`; fx avg `0.0046` n `6`; index avg `-0.1377` n `23`; metal avg `-0.5237` n `18`; unknown avg `-0.3453` n `420`
- 4h: commodity avg `-0.0376` n `12`; crypto_alt avg `0.3309` n `228`; crypto_major avg `0.031` n `8`; equity avg `-0.2088` n `72`; fx avg `0.0138` n `6`; index avg `-0.089` n `23`; metal avg `-0.3531` n `18`; unknown avg `-0.7303` n `420`
- 24h: commodity avg `1.7243` n `12`; crypto_alt avg `-0.7606` n `228`; crypto_major avg `-3.1871` n `8`; equity avg `0.3446` n `72`; fx avg `0.0427` n `6`; index avg `0.7281` n `23`; metal avg `-1.9111` n `18`; unknown avg `-0.1196` n `409`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1135`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0746`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0664`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0657`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0638`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0632`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0623`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0588`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0517`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0436`, n `668`, weak_sample_signal
