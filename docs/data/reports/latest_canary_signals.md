# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-08T20:07:26.590788+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.003` n `13`; crypto_alt avg `-0.3288` n `239`; crypto_major avg `-0.1706` n `8`; equity avg `-0.2869` n `158`; fx avg `0.0015` n `6`; index avg `-0.0242` n `27`; metal avg `-0.0041` n `20`; unknown avg `3.9501` n `1240`
- 1h: commodity avg `0.0111` n `13`; crypto_alt avg `-0.2408` n `239`; crypto_major avg `-0.1226` n `8`; equity avg `-0.1599` n `158`; fx avg `-0.0074` n `6`; index avg `-0.0171` n `27`; metal avg `0.006` n `20`; unknown avg `1.023` n `1234`
- 4h: commodity avg `-0.1446` n `13`; crypto_alt avg `-0.5177` n `239`; crypto_major avg `-0.3893` n `8`; equity avg `0.0987` n `158`; fx avg `-0.0155` n `6`; index avg `0.0189` n `27`; metal avg `0.0271` n `20`; unknown avg `0.4314` n `1186`
- 24h: commodity avg `-0.0869` n `13`; crypto_alt avg `-1.7883` n `239`; crypto_major avg `-0.366` n `8`; equity avg `0.2172` n `158`; fx avg `0.0428` n `6`; index avg `-0.0093` n `27`; metal avg `-0.0199` n `20`; unknown avg `0.0311` n `1032`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.205`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1565`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1476`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1166`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1144`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1095`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.109`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1066`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1035`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0944`, n `668`, weak_sample_signal
