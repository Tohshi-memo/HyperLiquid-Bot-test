# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-18T12:07:30.323770+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0524` n `12`; crypto_alt avg `-0.0525` n `234`; crypto_major avg `-0.1356` n `8`; equity avg `-0.1613` n `140`; fx avg `0.004` n `6`; index avg `-0.015` n `26`; metal avg `-0.0365` n `20`; unknown avg `0.518` n `926`
- 1h: commodity avg `0.0509` n `12`; crypto_alt avg `0.2391` n `234`; crypto_major avg `0.0277` n `8`; equity avg `-0.2929` n `140`; fx avg `-0.0186` n `6`; index avg `-0.0437` n `26`; metal avg `-0.0652` n `20`; unknown avg `0.168` n `923`
- 4h: commodity avg `0.1462` n `12`; crypto_alt avg `0.0936` n `234`; crypto_major avg `0.2917` n `8`; equity avg `-0.5605` n `140`; fx avg `-0.0051` n `6`; index avg `-0.1173` n `26`; metal avg `-0.1306` n `20`; unknown avg `0.6945` n `917`
- 24h: commodity avg `0.1159` n `12`; crypto_alt avg `5.2497` n `234`; crypto_major avg `4.2012` n `8`; equity avg `1.1439` n `140`; fx avg `0.2111` n `6`; index avg `0.0836` n `26`; metal avg `0.4401` n `20`; unknown avg `0.8535` n `729`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.136`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1283`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1235`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1194`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1171`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1148`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1126`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1102`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1069`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1056`, n `668`, weak_sample_signal
