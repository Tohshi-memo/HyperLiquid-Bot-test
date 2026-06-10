# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-10T06:52:28.169237+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1558` n `12`; crypto_alt avg `0.2758` n `228`; crypto_major avg `0.213` n `8`; equity avg `0.0366` n `74`; fx avg `-0.0188` n `6`; index avg `-0.0314` n `23`; metal avg `0.0028` n `18`; unknown avg `0.0633` n `547`
- 1h: commodity avg `0.1474` n `12`; crypto_alt avg `0.4453` n `228`; crypto_major avg `0.1351` n `8`; equity avg `0.5329` n `74`; fx avg `-0.0006` n `6`; index avg `0.2312` n `23`; metal avg `0.368` n `18`; unknown avg `-0.336` n `537`
- 4h: commodity avg `-0.3613` n `12`; crypto_alt avg `0.2032` n `228`; crypto_major avg `-0.0772` n `8`; equity avg `0.069` n `74`; fx avg `0.0421` n `6`; index avg `-0.2552` n `23`; metal avg `0.6805` n `18`; unknown avg `-0.6615` n `537`
- 24h: commodity avg `-0.7905` n `12`; crypto_alt avg `-1.5893` n `228`; crypto_major avg `-3.9441` n `8`; equity avg `-3.4606` n `74`; fx avg `0.163` n `6`; index avg `-1.6923` n `23`; metal avg `-2.6775` n `18`; unknown avg `0.0423` n `535`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1135`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0877`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0826`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0721`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0698`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0645`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0642`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0637`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0636`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0617`, n `668`, weak_sample_signal
