# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-11T14:37:25.953069+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0983` n `13`; crypto_alt avg `0.0566` n `239`; crypto_major avg `0.05` n `8`; equity avg `-0.3527` n `161`; fx avg `-0.0011` n `6`; index avg `-0.0394` n `27`; metal avg `-0.1521` n `20`; unknown avg `0.0523` n `1243`
- 1h: commodity avg `0.1166` n `13`; crypto_alt avg `0.027` n `239`; crypto_major avg `0.019` n `8`; equity avg `-0.5007` n `161`; fx avg `-0.0118` n `6`; index avg `-0.0661` n `27`; metal avg `-0.2374` n `20`; unknown avg `19.2031` n `1237`
- 4h: commodity avg `0.1064` n `13`; crypto_alt avg `0.0977` n `239`; crypto_major avg `-0.315` n `8`; equity avg `-0.2204` n `161`; fx avg `-0.0282` n `6`; index avg `-0.025` n `27`; metal avg `-0.3126` n `20`; unknown avg `0.2565` n `1231`
- 24h: commodity avg `1.2428` n `13`; crypto_alt avg `-0.6578` n `239`; crypto_major avg `-0.7836` n `8`; equity avg `3.2033` n `161`; fx avg `-0.2344` n `6`; index avg `0.27` n `27`; metal avg `0.1878` n `20`; unknown avg `1.9342` n `1155`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.275`, n `668`, moderate_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1418`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1376`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1347`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1265`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1173`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1059`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1052`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1044`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0965`, n `668`, weak_sample_signal
