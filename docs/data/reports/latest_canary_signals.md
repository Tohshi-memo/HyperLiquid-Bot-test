# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-18T06:08:08.625826+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0225` n `12`; crypto_alt avg `0.1018` n `234`; crypto_major avg `0.1556` n `8`; equity avg `0.1242` n `140`; fx avg `-0.0025` n `6`; index avg `0.0102` n `26`; metal avg `0.0868` n `20`; unknown avg `0.1036` n `881`
- 1h: commodity avg `-0.057` n `12`; crypto_alt avg `-0.1302` n `234`; crypto_major avg `0.0858` n `8`; equity avg `0.1581` n `140`; fx avg `-0.0622` n `6`; index avg `0.0065` n `26`; metal avg `0.145` n `20`; unknown avg `7.7821` n `881`
- 4h: commodity avg `-0.0624` n `12`; crypto_alt avg `1.2827` n `234`; crypto_major avg `1.438` n `8`; equity avg `0.9414` n `140`; fx avg `0.0564` n `6`; index avg `0.1379` n `26`; metal avg `0.2995` n `20`; unknown avg `4.9733` n `863`
- 24h: commodity avg `-0.1932` n `12`; crypto_alt avg `5.0004` n `234`; crypto_major avg `3.8402` n `8`; equity avg `2.4294` n `140`; fx avg `0.1123` n `6`; index avg `0.3667` n `26`; metal avg `0.6365` n `20`; unknown avg `4.6481` n `741`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1228`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.121`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1104`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.11`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1094`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1067`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1055`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1054`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1021`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1015`, n `668`, weak_sample_signal
