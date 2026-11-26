# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-26T12:52:27.146835+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0799` n `13`; crypto_alt avg `-0.0` n `239`; crypto_major avg `0.0986` n `8`; equity avg `0.0325` n `168`; fx avg `0.0` n `6`; index avg `0.0025` n `27`; metal avg `-0.028` n `20`; unknown avg `0.6278` n `1267`
- 1h: commodity avg `0.0273` n `13`; crypto_alt avg `-0.0346` n `239`; crypto_major avg `0.1729` n `8`; equity avg `0.2079` n `168`; fx avg `0.0114` n `6`; index avg `0.0214` n `27`; metal avg `0.0478` n `20`; unknown avg `3.011` n `1255`
- 4h: commodity avg `0.2264` n `13`; crypto_alt avg `0.2019` n `239`; crypto_major avg `-0.1835` n `8`; equity avg `0.0605` n `168`; fx avg `0.0214` n `6`; index avg `0.0004` n `27`; metal avg `-0.1091` n `20`; unknown avg `80.8798` n `1251`
- 24h: commodity avg `0.5018` n `13`; crypto_alt avg `4.634` n `239`; crypto_major avg `3.8407` n `8`; equity avg `4.5694` n `168`; fx avg `0.0789` n `6`; index avg `0.4396` n `27`; metal avg `0.7586` n `20`; unknown avg `190.7796` n `1057`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1285`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1272`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1169`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1136`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1128`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.112`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1029`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.1027`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0886`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.085`, n `668`, weak_sample_signal
