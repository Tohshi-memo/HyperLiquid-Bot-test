# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-10T13:07:35.354891+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0487` n `12`; crypto_alt avg `-0.1407` n `228`; crypto_major avg `-0.2319` n `8`; equity avg `-0.3345` n `74`; fx avg `-0.0082` n `6`; index avg `-0.0667` n `23`; metal avg `0.2924` n `18`; unknown avg `-0.2623` n `547`
- 1h: commodity avg `-0.0381` n `12`; crypto_alt avg `1.1522` n `228`; crypto_major avg `0.7795` n `8`; equity avg `0.9035` n `74`; fx avg `-0.0053` n `6`; index avg `0.5406` n `23`; metal avg `0.852` n `18`; unknown avg `0.0304` n `547`
- 4h: commodity avg `1.3853` n `12`; crypto_alt avg `0.4516` n `228`; crypto_major avg `0.5409` n `8`; equity avg `0.4881` n `74`; fx avg `-0.0448` n `6`; index avg `0.2975` n `23`; metal avg `0.406` n `18`; unknown avg `0.1729` n `547`
- 24h: commodity avg `0.6037` n `12`; crypto_alt avg `-1.7285` n `228`; crypto_major avg `-3.2389` n `8`; equity avg `-4.0433` n `74`; fx avg `-0.1058` n `6`; index avg `-2.1627` n `23`; metal avg `-3.4663` n `18`; unknown avg `0.9582` n `535`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1074`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0872`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0865`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0753`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0714`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0691`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.065`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0596`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0566`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0553`, n `668`, weak_sample_signal
