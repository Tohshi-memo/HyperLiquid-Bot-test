# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-05T02:22:23.401343+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0538` n `12`; crypto_alt avg `-0.7137` n `228`; crypto_major avg `-0.5838` n `8`; equity avg `0.0209` n `74`; fx avg `-0.0103` n `6`; index avg `0.0713` n `23`; metal avg `0.2246` n `18`; unknown avg `-0.1206` n `424`
- 1h: commodity avg `0.1608` n `12`; crypto_alt avg `-0.3702` n `228`; crypto_major avg `-0.2744` n `8`; equity avg `0.7837` n `74`; fx avg `0.005` n `6`; index avg `0.2815` n `23`; metal avg `0.1732` n `18`; unknown avg `0.6867` n `424`
- 4h: commodity avg `0.1505` n `12`; crypto_alt avg `-0.6387` n `228`; crypto_major avg `-0.4933` n `8`; equity avg `-0.623` n `74`; fx avg `0.1433` n `6`; index avg `-0.5384` n `23`; metal avg `-0.8086` n `18`; unknown avg `-0.3722` n `424`
- 24h: commodity avg `-0.0012` n `12`; crypto_alt avg `-3.049` n `228`; crypto_major avg `-2.2348` n `8`; equity avg `-0.4767` n `73`; fx avg `0.2252` n `6`; index avg `-0.134` n `23`; metal avg `-0.2427` n `18`; unknown avg `-0.8514` n `402`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1358`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.12`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1116`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1072`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1071`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0936`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0881`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0807`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0763`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0728`, n `668`, weak_sample_signal
