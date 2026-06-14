# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-14T16:07:28.758897+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1193` n `12`; crypto_alt avg `0.053` n `228`; crypto_major avg `0.0432` n `8`; equity avg `-0.044` n `74`; fx avg `0.0058` n `6`; index avg `0.0159` n `23`; metal avg `0.0004` n `18`; unknown avg `0.0699` n `645`
- 1h: commodity avg `-0.044` n `12`; crypto_alt avg `0.1654` n `228`; crypto_major avg `0.0909` n `8`; equity avg `-0.0025` n `74`; fx avg `0.0258` n `6`; index avg `0.1197` n `23`; metal avg `-0.0587` n `18`; unknown avg `-0.0217` n `645`
- 4h: commodity avg `0.2793` n `12`; crypto_alt avg `-0.714` n `228`; crypto_major avg `-0.6321` n `8`; equity avg `-0.2589` n `74`; fx avg `-0.0276` n `6`; index avg `0.1182` n `23`; metal avg `-0.1577` n `18`; unknown avg `-0.0538` n `645`
- 24h: commodity avg `-0.1814` n `12`; crypto_alt avg `-1.3049` n `228`; crypto_major avg `-0.5677` n `8`; equity avg `0.4483` n `74`; fx avg `-0.0091` n `6`; index avg `0.1816` n `23`; metal avg `-0.0422` n `18`; unknown avg `1.4738` n `592`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1391`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1134`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1069`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1043`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0726`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0701`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0676`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.062`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0602`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0586`, n `668`, weak_sample_signal
