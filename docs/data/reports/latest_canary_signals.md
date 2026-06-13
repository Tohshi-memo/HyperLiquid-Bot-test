# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-13T16:07:30.848666+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0925` n `12`; crypto_alt avg `-0.3115` n `228`; crypto_major avg `-0.3136` n `8`; equity avg `-0.1068` n `74`; fx avg `-0.0013` n `6`; index avg `0.0133` n `23`; metal avg `-0.1456` n `18`; unknown avg `0.0633` n `644`
- 1h: commodity avg `0.0249` n `12`; crypto_alt avg `-0.0545` n `228`; crypto_major avg `-0.2034` n `8`; equity avg `-0.0051` n `74`; fx avg `-0.0045` n `6`; index avg `0.0582` n `23`; metal avg `-0.1201` n `18`; unknown avg `-2.1188` n `644`
- 4h: commodity avg `-0.0617` n `12`; crypto_alt avg `0.2915` n `228`; crypto_major avg `0.5036` n `8`; equity avg `0.2652` n `74`; fx avg `-0.0145` n `6`; index avg `0.2012` n `23`; metal avg `-0.0662` n `18`; unknown avg `-2.1317` n `644`
- 24h: commodity avg `-0.5844` n `12`; crypto_alt avg `2.0101` n `228`; crypto_major avg `0.696` n `8`; equity avg `0.8307` n `74`; fx avg `0.0064` n `6`; index avg `0.8766` n `23`; metal avg `0.6523` n `18`; unknown avg `-1.8923` n `611`

## Correlations

- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0821`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0776`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0766`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0699`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.068`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0636`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0594`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0569`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0567`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0541`, n `668`, weak_sample_signal
