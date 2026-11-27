# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-27T22:37:23.756067+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0202` n `13`; crypto_alt avg `0.0604` n `239`; crypto_major avg `0.0022` n `8`; equity avg `0.0519` n `168`; fx avg `-0.0007` n `6`; index avg `-0.005` n `27`; metal avg `0.0063` n `20`; unknown avg `126.129` n `1265`
- 1h: commodity avg `0.0092` n `13`; crypto_alt avg `-0.239` n `239`; crypto_major avg `-0.5087` n `8`; equity avg `-0.1312` n `168`; fx avg `-0.0058` n `6`; index avg `-0.0361` n `27`; metal avg `0.0205` n `20`; unknown avg `0.1016` n `1243`
- 4h: commodity avg `0.061` n `13`; crypto_alt avg `0.1963` n `239`; crypto_major avg `-0.1647` n `8`; equity avg `0.0887` n `168`; fx avg `-0.0041` n `6`; index avg `0.0074` n `27`; metal avg `0.2129` n `20`; unknown avg `172.2792` n `1170`
- 24h: commodity avg `-0.4683` n `13`; crypto_alt avg `0.1189` n `239`; crypto_major avg `-0.1034` n `8`; equity avg `3.1386` n `168`; fx avg `-0.1609` n `6`; index avg `0.3087` n `27`; metal avg `0.989` n `20`; unknown avg `273.5628` n `999`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1344`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1308`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.1065`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1024`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0939`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0869`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0708`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0698`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0687`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0677`, n `668`, weak_sample_signal
