# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-10T06:22:25.792149+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.2302` n `12`; crypto_alt avg `0.1979` n `228`; crypto_major avg `0.066` n `8`; equity avg `0.1403` n `74`; fx avg `0.0046` n `6`; index avg `0.0035` n `23`; metal avg `-0.017` n `18`; unknown avg `-0.3841` n `547`
- 1h: commodity avg `-0.3774` n `12`; crypto_alt avg `0.3952` n `228`; crypto_major avg `0.2618` n `8`; equity avg `0.6598` n `74`; fx avg `0.0242` n `6`; index avg `0.2625` n `23`; metal avg `0.9143` n `18`; unknown avg `-0.5372` n `537`
- 4h: commodity avg `-0.687` n `12`; crypto_alt avg `-0.5957` n `228`; crypto_major avg `-0.6484` n `8`; equity avg `-0.2575` n `74`; fx avg `0.0717` n `6`; index avg `-0.4009` n `23`; metal avg `0.4053` n `18`; unknown avg `-0.8` n `537`
- 24h: commodity avg `-1.0055` n `12`; crypto_alt avg `-2.1459` n `228`; crypto_major avg `-4.3733` n `8`; equity avg `-3.783` n `74`; fx avg `0.217` n `6`; index avg `-1.8975` n `23`; metal avg `-2.6907` n `18`; unknown avg `-0.2172` n `535`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `-0.112`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0863`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0807`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0705`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0662`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0651`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0651`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0614`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0578`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0574`, n `668`, weak_sample_signal
