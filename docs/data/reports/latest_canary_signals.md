# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-08T13:52:28.834831+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0003` n `13`; crypto_alt avg `-0.218` n `239`; crypto_major avg `-0.1616` n `8`; equity avg `-0.0456` n `158`; fx avg `-0.0176` n `6`; index avg `-0.0037` n `27`; metal avg `-0.004` n `20`; unknown avg `0.0555` n `1262`
- 1h: commodity avg `0.0018` n `13`; crypto_alt avg `-0.4012` n `239`; crypto_major avg `-0.1445` n `8`; equity avg `0.0311` n `158`; fx avg `-0.0137` n `6`; index avg `-0.0002` n `27`; metal avg `-0.0054` n `20`; unknown avg `0.9487` n `1256`
- 4h: commodity avg `0.012` n `13`; crypto_alt avg `-0.5768` n `239`; crypto_major avg `0.0804` n `8`; equity avg `0.038` n `158`; fx avg `-0.0086` n `6`; index avg `-0.0008` n `27`; metal avg `-0.0099` n `20`; unknown avg `5.5581` n `1250`
- 24h: commodity avg `0.1016` n `13`; crypto_alt avg `-1.9185` n `239`; crypto_major avg `-0.3355` n `8`; equity avg `0.1364` n `158`; fx avg `0.0042` n `6`; index avg `0.0033` n `27`; metal avg `-0.0401` n `20`; unknown avg `6.1475` n `1097`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.208`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1641`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1495`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1205`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1186`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1171`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1128`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1061`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1054`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1049`, n `668`, weak_sample_signal
