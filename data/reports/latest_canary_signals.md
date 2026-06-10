# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-10T09:07:29.691171+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1259` n `12`; crypto_alt avg `-0.0898` n `228`; crypto_major avg `0.0099` n `8`; equity avg `-0.1519` n `74`; fx avg `0.0342` n `6`; index avg `0.0252` n `23`; metal avg `-0.0297` n `18`; unknown avg `-0.0826` n `547`
- 1h: commodity avg `-0.5127` n `12`; crypto_alt avg `-0.2886` n `228`; crypto_major avg `-0.3788` n `8`; equity avg `-0.5693` n `74`; fx avg `-0.023` n `6`; index avg `-0.2452` n `23`; metal avg `0.0817` n `18`; unknown avg `0.0456` n `547`
- 4h: commodity avg `-0.0955` n `12`; crypto_alt avg `-0.037` n `228`; crypto_major avg `-0.2955` n `8`; equity avg `-0.4108` n `74`; fx avg `0.0237` n `6`; index avg `-0.2651` n `23`; metal avg `0.252` n `18`; unknown avg `-0.2622` n `537`
- 24h: commodity avg `-0.6422` n `12`; crypto_alt avg `-1.5402` n `228`; crypto_major avg `-3.9003` n `8`; equity avg `-4.3048` n `74`; fx avg `0.088` n `6`; index avg `-2.3308` n `23`; metal avg `-3.3218` n `18`; unknown avg `0.334` n `535`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1104`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0865`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0824`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0745`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0703`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0679`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0614`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0518`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0511`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.049`, n `668`, weak_sample_signal
