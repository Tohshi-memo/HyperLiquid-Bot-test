# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-07T13:37:14.858930+00:00`
- Correlation status: `ready`
- Asset price records: `554`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0907` n `12`; crypto_alt avg `-0.474` n `228`; crypto_major avg `-0.4118` n `8`; equity avg `-0.1465` n `65`; fx avg `0.0024` n `5`; index avg `-0.1918` n `23`; metal avg `0.0423` n `18`; unknown avg `0.8116` n `365`
- 1h: commodity avg `0.0879` n `12`; crypto_alt avg `-0.4152` n `228`; crypto_major avg `-0.5074` n `8`; equity avg `-0.0523` n `65`; fx avg `0.0199` n `5`; index avg `-0.2519` n `23`; metal avg `-0.0622` n `18`; unknown avg `0.9357` n `365`
- 4h: commodity avg `-0.5975` n `12`; crypto_alt avg `0.3039` n `228`; crypto_major avg `-0.4156` n `8`; equity avg `-0.2898` n `65`; fx avg `-0.0069` n `5`; index avg `-0.2869` n `23`; metal avg `0.2412` n `18`; unknown avg `1.6561` n `357`
- 24h: commodity avg `-1.5339` n `12`; crypto_alt avg `1.1381` n `228`; crypto_major avg `-1.3892` n `8`; equity avg `1.7174` n `65`; fx avg `0.1161` n `5`; index avg `0.6162` n `23`; metal avg `1.9953` n `18`; unknown avg `1.2351` n `353`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.134`, n `550`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1253`, n `550`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1063`, n `550`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0805`, n `546`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0767`, n `546`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0761`, n `546`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0749`, n `546`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0713`, n `550`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0686`, n `550`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0685`, n `546`, weak_sample_signal
