# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-10T12:37:33.784638+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0388` n `12`; crypto_alt avg `1.6077` n `228`; crypto_major avg `1.3527` n `8`; equity avg `1.4682` n `74`; fx avg `-0.0091` n `6`; index avg `0.663` n `23`; metal avg `0.928` n `18`; unknown avg `0.3089` n `547`
- 1h: commodity avg `-0.1857` n `12`; crypto_alt avg `1.7137` n `228`; crypto_major avg `1.3264` n `8`; equity avg `1.4746` n `74`; fx avg `-0.0196` n `6`; index avg `0.7027` n `23`; metal avg `0.3777` n `18`; unknown avg `0.0932` n `547`
- 4h: commodity avg `0.9059` n `12`; crypto_alt avg `0.7248` n `228`; crypto_major avg `0.9214` n `8`; equity avg `0.6805` n `74`; fx avg `-0.0435` n `6`; index avg `0.2341` n `23`; metal avg `0.3568` n `18`; unknown avg `0.1283` n `547`
- 24h: commodity avg `0.4649` n `12`; crypto_alt avg `-1.0717` n `228`; crypto_major avg `-2.6857` n `8`; equity avg `-3.5303` n `74`; fx avg `-0.1317` n `6`; index avg `-2.032` n `23`; metal avg `-3.4399` n `18`; unknown avg `0.2915` n `535`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1075`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.091`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0892`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0872`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0783`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0747`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0636`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0632`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.059`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0507`, n `668`, weak_sample_signal
