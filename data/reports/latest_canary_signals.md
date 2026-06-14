# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-14T02:52:36.388765+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0394` n `12`; crypto_alt avg `-0.1814` n `228`; crypto_major avg `-0.1694` n `8`; equity avg `0.0197` n `74`; fx avg `-0.0049` n `6`; index avg `0.0005` n `23`; metal avg `0.0002` n `18`; unknown avg `1.1469` n `629`
- 1h: commodity avg `0.0342` n `12`; crypto_alt avg `-0.2915` n `228`; crypto_major avg `-0.1108` n `8`; equity avg `0.0299` n `74`; fx avg `-0.0026` n `6`; index avg `-0.0541` n `23`; metal avg `-0.0046` n `18`; unknown avg `1.0177` n `629`
- 4h: commodity avg `-0.2635` n `12`; crypto_alt avg `-0.3262` n `228`; crypto_major avg `0.058` n `8`; equity avg `0.0943` n `74`; fx avg `-0.0196` n `6`; index avg `-0.0797` n `23`; metal avg `0.0059` n `18`; unknown avg `2.1907` n `629`
- 24h: commodity avg `-0.6292` n `12`; crypto_alt avg `1.5023` n `228`; crypto_major avg `1.5489` n `8`; equity avg `0.4049` n `74`; fx avg `-0.0199` n `6`; index avg `0.2085` n `23`; metal avg `0.2677` n `18`; unknown avg `0.8965` n `595`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.093`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0925`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0706`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0671`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0643`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0612`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0598`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0595`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0579`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0576`, n `668`, weak_sample_signal
