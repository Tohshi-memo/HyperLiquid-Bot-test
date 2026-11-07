# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-07T14:37:32.305648+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.003` n `13`; crypto_alt avg `0.046` n `239`; crypto_major avg `0.0312` n `8`; equity avg `-0.0196` n `158`; fx avg `0.002` n `6`; index avg `-0.0012` n `27`; metal avg `-0.0025` n `20`; unknown avg `-0.2088` n `1261`
- 1h: commodity avg `0.0055` n `13`; crypto_alt avg `-0.0988` n `239`; crypto_major avg `0.088` n `8`; equity avg `-0.0839` n `158`; fx avg `-0.0345` n `6`; index avg `0.0004` n `27`; metal avg `-0.0017` n `20`; unknown avg `0.082` n `1255`
- 4h: commodity avg `0.0181` n `13`; crypto_alt avg `0.1703` n `239`; crypto_major avg `0.0754` n `8`; equity avg `0.0347` n `158`; fx avg `0.0121` n `6`; index avg `0.0251` n `27`; metal avg `-0.0021` n `20`; unknown avg `-0.1559` n `1249`
- 24h: commodity avg `0.2883` n `13`; crypto_alt avg `-1.5576` n `239`; crypto_major avg `-0.3185` n `8`; equity avg `0.2876` n `158`; fx avg `-0.0225` n `6`; index avg `-0.0124` n `27`; metal avg `0.1709` n `20`; unknown avg `0.3504` n `1117`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2128`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1612`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1587`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1323`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1187`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.108`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.107`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1064`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1015`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1006`, n `668`, weak_sample_signal
