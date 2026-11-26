# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-26T11:22:32.384571+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0127` n `13`; crypto_alt avg `0.226` n `239`; crypto_major avg `0.3158` n `8`; equity avg `0.248` n `168`; fx avg `-0.0172` n `6`; index avg `0.0361` n `27`; metal avg `0.0915` n `20`; unknown avg `-0.0709` n `1265`
- 1h: commodity avg `0.1961` n `13`; crypto_alt avg `0.1717` n `239`; crypto_major avg `-0.1706` n `8`; equity avg `0.0887` n `168`; fx avg `-0.0235` n `6`; index avg `0.0232` n `27`; metal avg `0.024` n `20`; unknown avg `-0.1716` n `1263`
- 4h: commodity avg `0.2345` n `13`; crypto_alt avg `0.4272` n `239`; crypto_major avg `-0.0245` n `8`; equity avg `-0.0308` n `168`; fx avg `0.0168` n `6`; index avg `-0.0028` n `27`; metal avg `-0.0027` n `20`; unknown avg `175.4405` n `1151`
- 24h: commodity avg `0.535` n `13`; crypto_alt avg `4.1404` n `239`; crypto_major avg `3.5388` n `8`; equity avg `3.7173` n `168`; fx avg `0.0731` n `6`; index avg `0.3526` n `27`; metal avg `0.6917` n `20`; unknown avg `237.6288` n `1055`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1276`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1263`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1193`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1171`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1116`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1109`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.1052`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1037`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0933`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0887`, n `668`, weak_sample_signal
