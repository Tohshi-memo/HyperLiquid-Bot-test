# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-27T23:37:30.802416+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.016` n `13`; crypto_alt avg `0.2451` n `239`; crypto_major avg `0.1994` n `8`; equity avg `0.0559` n `168`; fx avg `-0.0073` n `6`; index avg `0.0095` n `27`; metal avg `0.0171` n `20`; unknown avg `2.7416` n `1263`
- 1h: commodity avg `0.0218` n `13`; crypto_alt avg `0.3452` n `239`; crypto_major avg `0.239` n `8`; equity avg `0.0884` n `168`; fx avg `-0.0122` n `6`; index avg `0.009` n `27`; metal avg `0.0078` n `20`; unknown avg `162.4817` n `1251`
- 4h: commodity avg `0.1032` n `13`; crypto_alt avg `0.1017` n `239`; crypto_major avg `-0.5216` n `8`; equity avg `-0.003` n `168`; fx avg `-0.0171` n `6`; index avg `0.0009` n `27`; metal avg `0.1932` n `20`; unknown avg `1.6141` n `1159`
- 24h: commodity avg `-0.5032` n `13`; crypto_alt avg `0.7997` n `239`; crypto_major avg `0.4709` n `8`; equity avg `3.4516` n `168`; fx avg `-0.1921` n `6`; index avg `0.3249` n `27`; metal avg `1.0636` n `20`; unknown avg `214.5753` n `989`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1362`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1319`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.1086`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1022`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1004`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0868`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0689`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0678`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0636`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0629`, n `668`, weak_sample_signal
