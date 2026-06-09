# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-09T19:52:30.689197+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1259` n `12`; crypto_alt avg `-0.0544` n `228`; crypto_major avg `-0.0938` n `8`; equity avg `-0.0366` n `74`; fx avg `-0.0165` n `6`; index avg `0.0937` n `23`; metal avg `-0.0002` n `18`; unknown avg `-0.0678` n `547`
- 1h: commodity avg `0.2296` n `12`; crypto_alt avg `0.2093` n `228`; crypto_major avg `0.0796` n `8`; equity avg `-0.12` n `74`; fx avg `-0.02` n `6`; index avg `0.0498` n `23`; metal avg `-0.2288` n `18`; unknown avg `0.0179` n `547`
- 4h: commodity avg `0.4076` n `12`; crypto_alt avg `0.9904` n `228`; crypto_major avg `0.6375` n `8`; equity avg `0.4073` n `74`; fx avg `-0.0608` n `6`; index avg `0.1741` n `23`; metal avg `-0.3044` n `18`; unknown avg `-0.1256` n `547`
- 24h: commodity avg `-0.7987` n `12`; crypto_alt avg `-1.9493` n `228`; crypto_major avg `-2.6957` n `8`; equity avg `-2.0517` n `74`; fx avg `0.0855` n `6`; index avg `-1.1751` n `23`; metal avg `-1.4629` n `18`; unknown avg `-1.4383` n `503`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1183`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0984`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0762`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0729`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0726`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0571`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0523`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.047`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0456`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0437`, n `668`, weak_sample_signal
