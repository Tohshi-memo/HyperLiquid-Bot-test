# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-04T07:22:32.520986+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.46` - Polymarket crypto volume is unusually high.
- 4h_commodity_crypto_divergence: score `2.0242` - Commodity perps and crypto are moving differently; check macro-linked stress.

## Class Returns

- 15m: commodity avg `-0.05` n `13`; crypto_alt avg `0.3575` n `239`; crypto_major avg `0.3241` n `8`; equity avg `0.0608` n `158`; fx avg `0.0034` n `6`; index avg `0.0001` n `27`; metal avg `0.0417` n `20`; unknown avg `0.2314` n `1262`
- 1h: commodity avg `0.0149` n `13`; crypto_alt avg `0.4801` n `239`; crypto_major avg `0.3075` n `8`; equity avg `0.0999` n `158`; fx avg `0.0203` n `6`; index avg `0.0286` n `27`; metal avg `-0.0342` n `20`; unknown avg `159.6971` n `1254`
- 4h: commodity avg `0.2627` n `13`; crypto_alt avg `3.1262` n `239`; crypto_major avg `2.2869` n `8`; equity avg `2.8081` n `158`; fx avg `0.0705` n `6`; index avg `0.4324` n `27`; metal avg `0.9483` n `20`; unknown avg `1.9514` n `1234`
- 24h: commodity avg `-0.2344` n `13`; crypto_alt avg `2.8863` n `239`; crypto_major avg `1.4562` n `8`; equity avg `2.5213` n `158`; fx avg `0.1509` n `6`; index avg `0.1431` n `27`; metal avg `0.7954` n `20`; unknown avg `191.8892` n `1051`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2274`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1531`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.145`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1398`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1362`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.134`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1328`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1259`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1231`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1222`, n `668`, weak_sample_signal
