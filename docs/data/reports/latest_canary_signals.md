# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-18T15:52:25.659840+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0796` n `12`; crypto_alt avg `0.2929` n `228`; crypto_major avg `-0.0542` n `8`; equity avg `-0.202` n `66`; fx avg `-0.0073` n `5`; index avg `-0.035` n `23`; metal avg `-0.0524` n `18`; unknown avg `-0.0068` n `384`
- 1h: commodity avg `0.3001` n `12`; crypto_alt avg `-0.0188` n `228`; crypto_major avg `-0.2288` n `8`; equity avg `-0.3166` n `66`; fx avg `0.0034` n `5`; index avg `-0.2288` n `23`; metal avg `-0.0336` n `18`; unknown avg `-0.089` n `384`
- 4h: commodity avg `0.6144` n `12`; crypto_alt avg `-0.5602` n `228`; crypto_major avg `-1.0386` n `8`; equity avg `-1.5253` n `66`; fx avg `-0.0082` n `5`; index avg `-0.4434` n `23`; metal avg `-0.0812` n `18`; unknown avg `0.306` n `383`
- 24h: commodity avg `0.8531` n `12`; crypto_alt avg `-2.7106` n `228`; crypto_major avg `-2.1216` n `8`; equity avg `-0.8681` n `66`; fx avg `0.0543` n `5`; index avg `-0.4249` n `23`; metal avg `0.3432` n `18`; unknown avg `-0.3576` n `363`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1594`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1555`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1495`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.12`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1195`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1149`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1144`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.11`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1065`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1016`, n `668`, weak_sample_signal
