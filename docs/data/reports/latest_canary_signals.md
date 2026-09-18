# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-18T02:22:54.789466+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0063` n `12`; crypto_alt avg `0.0173` n `234`; crypto_major avg `0.0588` n `8`; equity avg `0.0758` n `140`; fx avg `-0.0094` n `6`; index avg `0.0106` n `26`; metal avg `-0.0047` n `20`; unknown avg `0.0474` n `919`
- 1h: commodity avg `-0.0116` n `12`; crypto_alt avg `0.6781` n `234`; crypto_major avg `0.2964` n `8`; equity avg `0.0967` n `140`; fx avg `0.0183` n `6`; index avg `0.0059` n `26`; metal avg `-0.0451` n `20`; unknown avg `-0.2772` n `917`
- 4h: commodity avg `-0.0436` n `12`; crypto_alt avg `2.1376` n `234`; crypto_major avg `1.4257` n `8`; equity avg `-0.0495` n `140`; fx avg `0.0884` n `6`; index avg `-0.0699` n `26`; metal avg `0.1511` n `20`; unknown avg `-0.1688` n `869`
- 24h: commodity avg `-0.2649` n `12`; crypto_alt avg `4.7764` n `234`; crypto_major avg `2.8353` n `8`; equity avg `1.7308` n `139`; fx avg `0.0535` n `6`; index avg `0.2282` n `26`; metal avg `0.5059` n `20`; unknown avg `2.0865` n `765`

## Correlations

- market_context_score -> commodity_forward_1h_return_pct: corr `0.1293`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1264`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1095`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1071`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1037`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1009`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1005`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0992`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0985`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0979`, n `668`, weak_sample_signal
