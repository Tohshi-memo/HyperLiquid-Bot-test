# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-19T04:07:28.532257+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.04` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0116` n `13`; crypto_alt avg `0.5065` n `239`; crypto_major avg `0.5743` n `8`; equity avg `0.395` n `164`; fx avg `0.0091` n `6`; index avg `0.0539` n `27`; metal avg `0.125` n `20`; unknown avg `1.2062` n `1248`
- 1h: commodity avg `0.0054` n `13`; crypto_alt avg `1.397` n `239`; crypto_major avg `1.4354` n `8`; equity avg `0.9892` n `164`; fx avg `0.0132` n `6`; index avg `0.1625` n `27`; metal avg `0.2749` n `20`; unknown avg `22.8202` n `1243`
- 4h: commodity avg `0.0194` n `13`; crypto_alt avg `1.0528` n `239`; crypto_major avg `0.9657` n `8`; equity avg `0.5213` n `164`; fx avg `-0.0052` n `6`; index avg `0.0833` n `27`; metal avg `-0.089` n `20`; unknown avg `13.0561` n `1243`
- 24h: commodity avg `0.0389` n `13`; crypto_alt avg `0.6059` n `239`; crypto_major avg `-0.6437` n `8`; equity avg `0.1463` n `164`; fx avg `-0.111` n `6`; index avg `0.1248` n `27`; metal avg `-0.5102` n `20`; unknown avg `47.9954` n `1117`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.1291`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1172`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0977`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0882`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0739`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0698`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0658`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.058`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0547`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.054`, n `668`, weak_sample_signal
