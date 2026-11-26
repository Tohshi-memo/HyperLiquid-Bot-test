# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-26T07:22:29.909131+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0457` n `13`; crypto_alt avg `0.0609` n `239`; crypto_major avg `0.126` n `8`; equity avg `0.1046` n `168`; fx avg `0.0154` n `6`; index avg `0.0257` n `27`; metal avg `0.0461` n `20`; unknown avg `197.5064` n `1265`
- 1h: commodity avg `-0.2218` n `13`; crypto_alt avg `-0.0125` n `239`; crypto_major avg `0.0554` n `8`; equity avg `0.2041` n `168`; fx avg `0.0167` n `6`; index avg `0.0293` n `27`; metal avg `0.0439` n `20`; unknown avg `258.9666` n `1257`
- 4h: commodity avg `-0.2914` n `13`; crypto_alt avg `-0.4325` n `239`; crypto_major avg `-0.4827` n `8`; equity avg `-0.4303` n `168`; fx avg `-0.0005` n `6`; index avg `-0.0303` n `27`; metal avg `-0.0784` n `20`; unknown avg `1.9175` n `1221`
- 24h: commodity avg `0.5157` n `13`; crypto_alt avg `2.782` n `239`; crypto_major avg `2.6595` n `8`; equity avg `2.9754` n `168`; fx avg `0.0826` n `6`; index avg `0.2467` n `27`; metal avg `0.7644` n `20`; unknown avg `758.9835` n `1033`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `-0.126`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.12`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1184`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.1114`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1071`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1064`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1058`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1041`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0854`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.083`, n `668`, weak_sample_signal
