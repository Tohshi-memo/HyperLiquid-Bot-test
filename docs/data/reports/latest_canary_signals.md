# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-05T14:07:23.836538+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.2595` n `12`; crypto_alt avg `-0.7482` n `228`; crypto_major avg `-0.5036` n `8`; equity avg `-0.1862` n `74`; fx avg `-0.0206` n `6`; index avg `0.0086` n `23`; metal avg `-0.5193` n `18`; unknown avg `-0.6597` n `424`
- 1h: commodity avg `-0.368` n `12`; crypto_alt avg `-1.2709` n `228`; crypto_major avg `-1.8267` n `8`; equity avg `-1.8333` n `74`; fx avg `-0.0524` n `6`; index avg `-1.0318` n `23`; metal avg `-1.1608` n `18`; unknown avg `-0.2767` n `424`
- 4h: commodity avg `-0.8051` n `12`; crypto_alt avg `-2.1201` n `228`; crypto_major avg `-2.008` n `8`; equity avg `-2.5541` n `74`; fx avg `-0.0662` n `6`; index avg `-1.3587` n `23`; metal avg `-2.0636` n `18`; unknown avg `0.7126` n `424`
- 24h: commodity avg `-0.8682` n `12`; crypto_alt avg `-7.3929` n `228`; crypto_major avg `-6.1255` n `8`; equity avg `-3.5341` n `74`; fx avg `0.0365` n `6`; index avg `-1.263` n `23`; metal avg `-2.9258` n `18`; unknown avg `-0.5843` n `404`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.095`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0929`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0889`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0885`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0879`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0847`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0846`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0803`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0777`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0719`, n `668`, weak_sample_signal
