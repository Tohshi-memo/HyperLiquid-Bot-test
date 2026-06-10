# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-10T12:07:31.634861+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0935` n `12`; crypto_alt avg `-0.0869` n `228`; crypto_major avg `-0.1535` n `8`; equity avg `-0.0022` n `74`; fx avg `-0.0009` n `6`; index avg `-0.0272` n `23`; metal avg `-0.4143` n `18`; unknown avg `-0.0383` n `547`
- 1h: commodity avg `0.3582` n `12`; crypto_alt avg `-0.0731` n `228`; crypto_major avg `-0.0028` n `8`; equity avg `-0.2468` n `74`; fx avg `-0.0113` n `6`; index avg `-0.0809` n `23`; metal avg `-0.3842` n `18`; unknown avg `0.0294` n `547`
- 4h: commodity avg `0.8995` n `12`; crypto_alt avg `-0.9746` n `228`; crypto_major avg `-0.6148` n `8`; equity avg `-0.9752` n `74`; fx avg `-0.0625` n `6`; index avg `-0.4853` n `23`; metal avg `-0.3586` n `18`; unknown avg `0.1756` n `547`
- 24h: commodity avg `0.5306` n `12`; crypto_alt avg `-2.7108` n `228`; crypto_major avg `-4.1031` n `8`; equity avg `-4.8712` n `74`; fx avg `-0.0957` n `6`; index avg `-2.6238` n `23`; metal avg `-4.2614` n `18`; unknown avg `0.2345` n `535`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `-0.108`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0959`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0875`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0862`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0797`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0762`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0633`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0588`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0551`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0475`, n `668`, weak_sample_signal
