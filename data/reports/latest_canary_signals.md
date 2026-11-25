# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-25T13:07:29.603453+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1199` n `13`; crypto_alt avg `-0.1222` n `239`; crypto_major avg `-0.0431` n `8`; equity avg `0.013` n `168`; fx avg `-0.0152` n `6`; index avg `0.0098` n `27`; metal avg `0.0099` n `20`; unknown avg `-0.026` n `1255`
- 1h: commodity avg `0.1668` n `13`; crypto_alt avg `-0.1466` n `239`; crypto_major avg `0.1639` n `8`; equity avg `0.1964` n `168`; fx avg `-0.0016` n `6`; index avg `0.0387` n `27`; metal avg `0.2012` n `20`; unknown avg `114.0513` n `1259`
- 4h: commodity avg `0.3361` n `13`; crypto_alt avg `-1.4583` n `239`; crypto_major avg `-0.6545` n `8`; equity avg `-1.0538` n `168`; fx avg `-0.0145` n `6`; index avg `-0.1656` n `27`; metal avg `-0.1439` n `20`; unknown avg `114.873` n `1187`
- 24h: commodity avg `0.5082` n `13`; crypto_alt avg `-2.2295` n `239`; crypto_major avg `-3.1696` n `8`; equity avg `-5.0633` n `168`; fx avg `-0.0616` n `6`; index avg `-0.4348` n `27`; metal avg `-1.0541` n `20`; unknown avg `463.6652` n `1069`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1389`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1299`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1248`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1096`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1065`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0904`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0884`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0875`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0735`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0708`, n `668`, weak_sample_signal
