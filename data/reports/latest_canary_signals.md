# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-26T00:22:29.731472+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0048` n `13`; crypto_alt avg `0.5595` n `239`; crypto_major avg `0.6563` n `8`; equity avg `0.7191` n `168`; fx avg `-0.0299` n `6`; index avg `0.0801` n `27`; metal avg `0.0081` n `20`; unknown avg `1.5134` n `1265`
- 1h: commodity avg `-0.0138` n `13`; crypto_alt avg `1.0561` n `239`; crypto_major avg `1.0455` n `8`; equity avg `1.2385` n `168`; fx avg `-0.038` n `6`; index avg `0.1223` n `27`; metal avg `0.0186` n `20`; unknown avg `1.8936` n `1251`
- 4h: commodity avg `0.051` n `13`; crypto_alt avg `1.0347` n `239`; crypto_major avg `0.8797` n `8`; equity avg `1.5701` n `168`; fx avg `-0.0616` n `6`; index avg `0.1395` n `27`; metal avg `0.1193` n `20`; unknown avg `207.2769` n `1143`
- 24h: commodity avg `0.3924` n `13`; crypto_alt avg `3.5209` n `239`; crypto_major avg `2.2108` n `8`; equity avg `1.4095` n `168`; fx avg `-0.0619` n `6`; index avg `0.1082` n `27`; metal avg `0.3611` n `20`; unknown avg `770.9077` n `1017`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1858`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1289`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1274`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1227`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1169`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1038`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1026`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0871`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0849`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0794`, n `668`, weak_sample_signal
