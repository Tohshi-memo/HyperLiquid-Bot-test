# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-10T04:37:17.775883+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0036` n `12`; crypto_alt avg `0.1093` n `228`; crypto_major avg `0.091` n `8`; equity avg `0.0129` n `65`; fx avg `0.0006` n `5`; index avg `-0.0019` n `23`; metal avg `0.0129` n `18`; unknown avg `0.4192` n `376`
- 1h: commodity avg `-0.0879` n `12`; crypto_alt avg `0.0212` n `228`; crypto_major avg `0.1079` n `8`; equity avg `0.1061` n `65`; fx avg `0.0006` n `5`; index avg `0.0257` n `23`; metal avg `0.0851` n `18`; unknown avg `0.0056` n `376`
- 4h: commodity avg `-0.1442` n `12`; crypto_alt avg `-0.0973` n `228`; crypto_major avg `0.0429` n `8`; equity avg `0.3011` n `65`; fx avg `0.0034` n `5`; index avg `0.0837` n `23`; metal avg `0.1812` n `18`; unknown avg `-0.0544` n `376`
- 24h: commodity avg `0.1995` n `12`; crypto_alt avg `-1.6147` n `228`; crypto_major avg `-0.7101` n `8`; equity avg `1.0088` n `65`; fx avg `-0.0068` n `5`; index avg `0.2932` n `23`; metal avg `0.347` n `18`; unknown avg `-0.1481` n `355`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1364`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1165`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.101`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0974`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0899`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0894`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0802`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0744`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0742`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0729`, n `668`, weak_sample_signal
