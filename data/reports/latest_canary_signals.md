# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-07T08:07:26.805992+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0133` n `13`; crypto_alt avg `-0.0349` n `239`; crypto_major avg `0.0277` n `8`; equity avg `0.0307` n `158`; fx avg `-0.0144` n `6`; index avg `0.0079` n `27`; metal avg `-0.0008` n `20`; unknown avg `0.1586` n `1241`
- 1h: commodity avg `-0.0093` n `13`; crypto_alt avg `0.0261` n `239`; crypto_major avg `0.1332` n `8`; equity avg `0.067` n `158`; fx avg `-0.0136` n `6`; index avg `0.01` n `27`; metal avg `0.0006` n `20`; unknown avg `0.1745` n `1237`
- 4h: commodity avg `0.0404` n `13`; crypto_alt avg `0.1142` n `239`; crypto_major avg `0.2411` n `8`; equity avg `-0.055` n `158`; fx avg `-0.0391` n `6`; index avg `0.0166` n `27`; metal avg `-0.0082` n `20`; unknown avg `16.2085` n `1197`
- 24h: commodity avg `-0.2427` n `13`; crypto_alt avg `0.1555` n `239`; crypto_major avg `0.4861` n `8`; equity avg `1.0301` n `158`; fx avg `0.0046` n `6`; index avg `0.1929` n `27`; metal avg `0.1412` n `20`; unknown avg `8.1331` n `1036`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.213`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1592`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1516`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1362`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1172`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1138`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1101`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1095`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0976`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0968`, n `668`, weak_sample_signal
