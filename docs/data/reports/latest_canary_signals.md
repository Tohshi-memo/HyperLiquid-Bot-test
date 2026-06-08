# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-08T11:07:28.072429+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0565` n `12`; crypto_alt avg `0.2847` n `228`; crypto_major avg `0.0884` n `8`; equity avg `0.0249` n `74`; fx avg `0.0029` n `6`; index avg `-0.0225` n `23`; metal avg `-0.0322` n `18`; unknown avg `-0.0069` n `517`
- 1h: commodity avg `-0.2636` n `12`; crypto_alt avg `0.1936` n `228`; crypto_major avg `-0.2552` n `8`; equity avg `-0.0336` n `74`; fx avg `0.0501` n `6`; index avg `0.0124` n `23`; metal avg `0.0154` n `18`; unknown avg `-0.0488` n `517`
- 4h: commodity avg `-0.5118` n `12`; crypto_alt avg `1.1721` n `228`; crypto_major avg `0.2058` n `8`; equity avg `0.8523` n `74`; fx avg `0.0357` n `6`; index avg `0.373` n `23`; metal avg `0.1877` n `18`; unknown avg `-0.1754` n `517`
- 24h: commodity avg `0.4881` n `12`; crypto_alt avg `1.2941` n `228`; crypto_major avg `1.8259` n `8`; equity avg `1.3` n `74`; fx avg `-0.2662` n `6`; index avg `0.5414` n `23`; metal avg `-0.6871` n `18`; unknown avg `-2.4375` n `506`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.124`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1229`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1223`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1001`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0971`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0956`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0903`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0803`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0762`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0649`, n `668`, weak_sample_signal
