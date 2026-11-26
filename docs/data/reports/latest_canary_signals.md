# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-26T10:37:28.081669+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0206` n `13`; crypto_alt avg `0.0161` n `239`; crypto_major avg `-0.1603` n `8`; equity avg `-0.0428` n `168`; fx avg `0.0059` n `6`; index avg `-0.0005` n `27`; metal avg `-0.025` n `20`; unknown avg `-0.0854` n `1267`
- 1h: commodity avg `0.043` n `13`; crypto_alt avg `-0.0665` n `239`; crypto_major avg `-0.2912` n `8`; equity avg `-0.1363` n `168`; fx avg `0.0201` n `6`; index avg `-0.0106` n `27`; metal avg `-0.1449` n `20`; unknown avg `0.5122` n `1259`
- 4h: commodity avg `0.0508` n `13`; crypto_alt avg `0.1445` n `239`; crypto_major avg `-0.0902` n `8`; equity avg `-0.0526` n `168`; fx avg `0.0722` n `6`; index avg `-0.0017` n `27`; metal avg `0.0239` n `20`; unknown avg `174.814` n `1153`
- 24h: commodity avg `0.4166` n `13`; crypto_alt avg `3.6835` n `239`; crypto_major avg `3.3965` n `8`; equity avg `3.6904` n `168`; fx avg `0.1098` n `6`; index avg `0.3127` n `27`; metal avg `0.6533` n `20`; unknown avg `250.9935` n `997`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1254`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.125`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1208`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.112`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1097`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.109`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.1068`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1041`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0921`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0877`, n `668`, weak_sample_signal
