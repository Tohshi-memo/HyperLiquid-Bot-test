# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-14T17:22:34.666397+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0781` n `12`; crypto_alt avg `0.1813` n `233`; crypto_major avg `0.1935` n `8`; equity avg `0.0675` n `136`; fx avg `0.003` n `6`; index avg `-0.003` n `27`; metal avg `-0.0321` n `20`; unknown avg `0.4869` n `908`
- 1h: commodity avg `-0.0955` n `12`; crypto_alt avg `0.3392` n `233`; crypto_major avg `0.0708` n `8`; equity avg `0.2067` n `136`; fx avg `0.0269` n `6`; index avg `0.0189` n `27`; metal avg `0.0463` n `20`; unknown avg `0.5143` n `878`
- 4h: commodity avg `-0.2011` n `12`; crypto_alt avg `1.1439` n `233`; crypto_major avg `1.1457` n `8`; equity avg `1.3997` n `136`; fx avg `-0.0142` n `6`; index avg `0.1398` n `27`; metal avg `0.1567` n `20`; unknown avg `1.2738` n `864`
- 24h: commodity avg `0.3522` n `12`; crypto_alt avg `-0.0823` n `233`; crypto_major avg `1.6199` n `8`; equity avg `-0.1894` n `136`; fx avg `0.071` n `6`; index avg `-0.1396` n `27`; metal avg `-0.3212` n `20`; unknown avg `1.0586` n `672`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1044`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1041`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1007`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1005`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0936`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0771`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0738`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0732`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0666`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0629`, n `668`, weak_sample_signal
