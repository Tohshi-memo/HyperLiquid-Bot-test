# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-09T05:22:25.231540+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0831` n `13`; crypto_alt avg `0.0039` n `239`; crypto_major avg `0.0206` n `8`; equity avg `0.0796` n `158`; fx avg `-0.003` n `6`; index avg `-0.0059` n `27`; metal avg `-0.0006` n `20`; unknown avg `-0.0148` n `1263`
- 1h: commodity avg `-0.1897` n `13`; crypto_alt avg `-0.2606` n `239`; crypto_major avg `-0.3303` n `8`; equity avg `-0.1346` n `158`; fx avg `-0.0116` n `6`; index avg `-0.0104` n `27`; metal avg `-0.014` n `20`; unknown avg `24.1249` n `1255`
- 4h: commodity avg `0.1482` n `13`; crypto_alt avg `-0.114` n `239`; crypto_major avg `-0.1985` n `8`; equity avg `0.9092` n `158`; fx avg `-0.0739` n `6`; index avg `0.0764` n `27`; metal avg `0.0778` n `20`; unknown avg `3.9067` n `1234`
- 24h: commodity avg `0.0348` n `13`; crypto_alt avg `-2.0419` n `239`; crypto_major avg `-2.6825` n `8`; equity avg `0.1808` n `158`; fx avg `-0.0979` n `6`; index avg `0.0343` n `27`; metal avg `0.4868` n `20`; unknown avg `1.4789` n `984`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1686`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1598`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1546`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1466`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1358`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1253`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1205`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1191`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1126`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1118`, n `668`, weak_sample_signal
