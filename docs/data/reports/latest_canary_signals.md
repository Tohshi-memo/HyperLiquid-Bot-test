# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-07T00:37:32.734287+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0065` n `13`; crypto_alt avg `0.0614` n `239`; crypto_major avg `-0.0423` n `8`; equity avg `-0.0213` n `158`; fx avg `-0.0055` n `6`; index avg `0.0053` n `27`; metal avg `-0.0025` n `20`; unknown avg `0.0103` n `1261`
- 1h: commodity avg `0.0122` n `13`; crypto_alt avg `0.2021` n `239`; crypto_major avg `0.0487` n `8`; equity avg `0.0599` n `158`; fx avg `-0.0154` n `6`; index avg `0.0098` n `27`; metal avg `0.0112` n `20`; unknown avg `-0.18` n `1249`
- 4h: commodity avg `0.0501` n `13`; crypto_alt avg `-0.1715` n `239`; crypto_major avg `0.1246` n `8`; equity avg `-0.0304` n `158`; fx avg `0.0057` n `6`; index avg `-0.0228` n `27`; metal avg `0.0139` n `20`; unknown avg `-0.4191` n `1171`
- 24h: commodity avg `0.1173` n `13`; crypto_alt avg `0.8471` n `239`; crypto_major avg `-0.3562` n `8`; equity avg `1.4172` n `158`; fx avg `-0.0955` n `6`; index avg `0.2094` n `27`; metal avg `-0.0679` n `20`; unknown avg `8.2241` n `1022`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2143`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1671`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1619`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1417`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1177`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1136`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1116`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1111`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1032`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1024`, n `668`, weak_sample_signal
