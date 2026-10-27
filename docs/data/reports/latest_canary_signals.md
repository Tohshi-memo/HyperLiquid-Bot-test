# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-27T01:22:26.422302+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0239` n `13`; crypto_alt avg `-0.385` n `237`; crypto_major avg `-0.3268` n `8`; equity avg `-0.2298` n `154`; fx avg `0.0132` n `6`; index avg `-0.0224` n `27`; metal avg `-0.0209` n `20`; unknown avg `3.5718` n `1238`
- 1h: commodity avg `0.0204` n `13`; crypto_alt avg `-0.4997` n `237`; crypto_major avg `-0.2315` n `8`; equity avg `-0.3284` n `154`; fx avg `0.0223` n `6`; index avg `-0.0267` n `27`; metal avg `-0.1037` n `20`; unknown avg `1.6077` n `1234`
- 4h: commodity avg `-0.0606` n `13`; crypto_alt avg `0.3167` n `237`; crypto_major avg `0.4507` n `8`; equity avg `0.3895` n `154`; fx avg `0.0017` n `6`; index avg `0.1359` n `27`; metal avg `-0.0875` n `20`; unknown avg `1.2981` n `1210`
- 24h: commodity avg `0.0407` n `13`; crypto_alt avg `0.0073` n `237`; crypto_major avg `0.4283` n `8`; equity avg `1.7581` n `153`; fx avg `-0.0165` n `6`; index avg `0.1364` n `27`; metal avg `-0.086` n `20`; unknown avg `1000.5418` n `1002`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.2235`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1988`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1953`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1402`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.126`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1168`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1162`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1089`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1048`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0767`, n `668`, weak_sample_signal
