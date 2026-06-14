# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-14T04:52:31.287314+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0003` n `12`; crypto_alt avg `-0.2107` n `228`; crypto_major avg `-0.1126` n `8`; equity avg `-0.0427` n `74`; fx avg `-0.0032` n `6`; index avg `-0.0317` n `23`; metal avg `0.0015` n `18`; unknown avg `0.0949` n `645`
- 1h: commodity avg `-0.044` n `12`; crypto_alt avg `-0.524` n `228`; crypto_major avg `-0.3262` n `8`; equity avg `-0.0615` n `74`; fx avg `-0.01` n `6`; index avg `0.0028` n `23`; metal avg `0.0134` n `18`; unknown avg `-0.113` n `645`
- 4h: commodity avg `-0.0694` n `12`; crypto_alt avg `-0.248` n `228`; crypto_major avg `-0.2024` n `8`; equity avg `0.0425` n `74`; fx avg `-0.0069` n `6`; index avg `-0.0436` n `23`; metal avg `-0.0018` n `18`; unknown avg `-1.1585` n `629`
- 24h: commodity avg `-0.7519` n `12`; crypto_alt avg `1.0801` n `228`; crypto_major avg `1.4048` n `8`; equity avg `0.6522` n `74`; fx avg `-0.0153` n `6`; index avg `0.2792` n `23`; metal avg `0.3107` n `18`; unknown avg `-1.344` n `603`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0972`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0962`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0879`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0689`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0645`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0618`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0612`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0605`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0584`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0579`, n `668`, weak_sample_signal
