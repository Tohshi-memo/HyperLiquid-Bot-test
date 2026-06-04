# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-04T06:52:21.365147+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1358` n `12`; crypto_alt avg `-0.3345` n `228`; crypto_major avg `-0.4415` n `8`; equity avg `-0.0386` n `73`; fx avg `-0.0056` n `6`; index avg `-0.0033` n `23`; metal avg `-0.0057` n `18`; unknown avg `-0.1401` n `424`
- 1h: commodity avg `-0.0104` n `12`; crypto_alt avg `0.3378` n `228`; crypto_major avg `-0.2996` n `8`; equity avg `0.1156` n `73`; fx avg `0.0153` n `6`; index avg `0.0512` n `23`; metal avg `0.0036` n `18`; unknown avg `-0.4106` n `404`
- 4h: commodity avg `0.0596` n `12`; crypto_alt avg `0.2657` n `228`; crypto_major avg `-0.0301` n `8`; equity avg `0.4196` n `73`; fx avg `0.034` n `6`; index avg `0.1933` n `23`; metal avg `-0.17` n `18`; unknown avg `0.1775` n `404`
- 24h: commodity avg `-0.2591` n `12`; crypto_alt avg `-4.3472` n `228`; crypto_major avg `-3.9029` n `8`; equity avg `-3.656` n `73`; fx avg `-0.045` n `6`; index avg `-1.0307` n `23`; metal avg `-1.2178` n `18`; unknown avg `-0.1101` n `403`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1782`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1673`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1459`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1416`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0999`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.092`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0901`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0764`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0709`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0664`, n `668`, weak_sample_signal
