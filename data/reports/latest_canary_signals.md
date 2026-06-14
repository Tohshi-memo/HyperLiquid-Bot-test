# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-14T08:37:28.919895+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.013` n `12`; crypto_alt avg `0.0473` n `228`; crypto_major avg `0.0686` n `8`; equity avg `0.0024` n `74`; fx avg `-0.0099` n `6`; index avg `-0.0134` n `23`; metal avg `-0.0007` n `18`; unknown avg `-0.1337` n `645`
- 1h: commodity avg `-0.1563` n `12`; crypto_alt avg `0.2812` n `228`; crypto_major avg `0.1125` n `8`; equity avg `0.1574` n `74`; fx avg `-0.0115` n `6`; index avg `0.0385` n `23`; metal avg `0.0289` n `18`; unknown avg `54.5969` n `645`
- 4h: commodity avg `-0.2747` n `12`; crypto_alt avg `0.0559` n `228`; crypto_major avg `-0.1257` n `8`; equity avg `0.2224` n `74`; fx avg `-0.01` n `6`; index avg `-0.0115` n `23`; metal avg `0.0318` n `18`; unknown avg `8.2501` n `625`
- 24h: commodity avg `-0.9178` n `12`; crypto_alt avg `0.4294` n `228`; crypto_major avg `0.7143` n `8`; equity avg `0.7407` n `74`; fx avg `-0.0108` n `6`; index avg `0.2413` n `23`; metal avg `0.2456` n `18`; unknown avg `-0.6065` n `599`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1192`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1029`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0979`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0762`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0737`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0725`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0675`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0648`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0642`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0619`, n `668`, weak_sample_signal
