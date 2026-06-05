# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-05T17:52:28.529235+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.011` n `12`; crypto_alt avg `-0.0905` n `228`; crypto_major avg `-0.0333` n `8`; equity avg `-0.2478` n `74`; fx avg `-0.0002` n `6`; index avg `-0.0679` n `23`; metal avg `-0.086` n `18`; unknown avg `-0.2347` n `424`
- 1h: commodity avg `0.0709` n `12`; crypto_alt avg `-0.4624` n `228`; crypto_major avg `-0.7476` n `8`; equity avg `-0.2163` n `74`; fx avg `-0.0236` n `6`; index avg `-0.2532` n `23`; metal avg `0.0112` n `18`; unknown avg `-0.3543` n `424`
- 4h: commodity avg `-1.0215` n `12`; crypto_alt avg `-1.1884` n `228`; crypto_major avg `-1.4752` n `8`; equity avg `-2.2489` n `74`; fx avg `-0.1524` n `6`; index avg `-1.2907` n `23`; metal avg `-1.7454` n `18`; unknown avg `-1.3652` n `424`
- 24h: commodity avg `-1.4934` n `12`; crypto_alt avg `-8.0375` n `228`; crypto_major avg `-6.6059` n `8`; equity avg `-6.2666` n `74`; fx avg `-0.0585` n `6`; index avg `-3.5347` n `23`; metal avg `-4.0616` n `18`; unknown avg `-1.9801` n `404`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1183`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1137`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0899`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0829`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0754`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0719`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0613`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0613`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0598`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0597`, n `668`, weak_sample_signal
