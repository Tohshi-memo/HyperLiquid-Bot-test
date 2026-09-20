# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-20T23:22:31.808356+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0259` n `12`; crypto_alt avg `0.2532` n `234`; crypto_major avg `0.2876` n `8`; equity avg `0.0694` n `140`; fx avg `-0.0085` n `6`; index avg `0.0014` n `26`; metal avg `-0.007` n `20`; unknown avg `20.8238` n `943`
- 1h: commodity avg `-0.077` n `12`; crypto_alt avg `-0.0611` n `234`; crypto_major avg `0.4362` n `8`; equity avg `0.2469` n `140`; fx avg `-0.0018` n `6`; index avg `0.042` n `26`; metal avg `-0.0078` n `20`; unknown avg `6.5883` n `941`
- 4h: commodity avg `-0.3218` n `12`; crypto_alt avg `0.8711` n `234`; crypto_major avg `0.6493` n `8`; equity avg `0.5164` n `140`; fx avg `0.0681` n `6`; index avg `0.1058` n `26`; metal avg `0.046` n `20`; unknown avg `2.3656` n `853`
- 24h: commodity avg `-0.0219` n `12`; crypto_alt avg `1.1433` n `234`; crypto_major avg `0.5556` n `8`; equity avg `0.4023` n `140`; fx avg `0.0592` n `6`; index avg `0.0641` n `26`; metal avg `0.0226` n `20`; unknown avg `3.8573` n `757`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1851`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1622`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1531`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1282`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.092`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0773`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0772`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0749`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0643`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0613`, n `668`, weak_sample_signal
