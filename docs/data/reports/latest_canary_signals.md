# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-18T12:22:37.117281+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0952` n `12`; crypto_alt avg `0.101` n `234`; crypto_major avg `0.0776` n `8`; equity avg `-0.0814` n `140`; fx avg `0.0022` n `6`; index avg `-0.0268` n `26`; metal avg `-0.092` n `20`; unknown avg `1.0973` n `928`
- 1h: commodity avg `0.1421` n `12`; crypto_alt avg `0.4001` n `234`; crypto_major avg `0.0385` n `8`; equity avg `-0.2969` n `140`; fx avg `-0.0155` n `6`; index avg `-0.0405` n `26`; metal avg `-0.1663` n `20`; unknown avg `1.1935` n `923`
- 4h: commodity avg `0.2064` n `12`; crypto_alt avg `0.1577` n `234`; crypto_major avg `0.1467` n `8`; equity avg `-0.7343` n `140`; fx avg `-0.0163` n `6`; index avg `-0.1451` n `26`; metal avg `-0.1966` n `20`; unknown avg `0.8319` n `917`
- 24h: commodity avg `0.2853` n `12`; crypto_alt avg `4.8308` n `234`; crypto_major avg `3.5527` n `8`; equity avg `0.8204` n `140`; fx avg `0.2582` n `6`; index avg `-0.0052` n `26`; metal avg `0.1409` n `20`; unknown avg `0.9494` n `729`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1369`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1281`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1237`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1167`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1157`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1148`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1124`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1095`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.107`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1058`, n `668`, weak_sample_signal
