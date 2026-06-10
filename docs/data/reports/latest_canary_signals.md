# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-10T10:37:35.774863+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0307` n `12`; crypto_alt avg `0.2737` n `228`; crypto_major avg `0.3234` n `8`; equity avg `0.1658` n `74`; fx avg `-0.0214` n `6`; index avg `0.059` n `23`; metal avg `0.0321` n `18`; unknown avg `0.023` n `547`
- 1h: commodity avg `0.2607` n `12`; crypto_alt avg `0.2105` n `228`; crypto_major avg `0.1699` n `8`; equity avg `0.0559` n `74`; fx avg `-0.0154` n `6`; index avg `-0.0055` n `23`; metal avg `-0.0388` n `18`; unknown avg `0.0994` n `547`
- 4h: commodity avg `0.6663` n `12`; crypto_alt avg `0.1158` n `228`; crypto_major avg `0.1449` n `8`; equity avg `-0.767` n `74`; fx avg `-0.0303` n `6`; index avg `-0.4026` n `23`; metal avg `-0.5906` n `18`; unknown avg `0.1278` n `547`
- 24h: commodity avg `-0.2246` n `12`; crypto_alt avg `-1.1087` n `228`; crypto_major avg `-3.2979` n `8`; equity avg `-4.1623` n `74`; fx avg `-0.0201` n `6`; index avg `-2.2682` n `23`; metal avg `-3.5108` n `18`; unknown avg `0.0143` n `535`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1099`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0949`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0882`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0848`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0799`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0789`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0639`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0574`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0573`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0486`, n `668`, weak_sample_signal
