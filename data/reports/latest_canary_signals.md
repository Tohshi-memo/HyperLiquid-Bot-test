# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-08T17:07:26.071191+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0024` n `13`; crypto_alt avg `-0.0293` n `239`; crypto_major avg `0.0639` n `8`; equity avg `0.0176` n `158`; fx avg `0.0059` n `6`; index avg `0.0023` n `27`; metal avg `-0.002` n `20`; unknown avg `0.104` n `1226`
- 1h: commodity avg `0.0068` n `13`; crypto_alt avg `-0.6173` n `239`; crypto_major avg `-0.3255` n `8`; equity avg `-0.0345` n `158`; fx avg `0.0126` n `6`; index avg `0.0028` n `27`; metal avg `-0.0054` n `20`; unknown avg `0.0721` n `1224`
- 4h: commodity avg `0.0129` n `13`; crypto_alt avg `-0.768` n `239`; crypto_major avg `-0.4613` n `8`; equity avg `-0.1857` n `158`; fx avg `0.0191` n `6`; index avg `-0.007` n `27`; metal avg `-0.0398` n `20`; unknown avg `0.4987` n `1202`
- 24h: commodity avg `0.05` n `13`; crypto_alt avg `-1.7992` n `239`; crypto_major avg `-0.2201` n `8`; equity avg `0.167` n `158`; fx avg `0.0716` n `6`; index avg `-0.0165` n `27`; metal avg `-0.0502` n `20`; unknown avg `8.2129` n `1052`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2085`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1638`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1514`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1208`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1194`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1162`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1133`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.109`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1076`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1073`, n `668`, weak_sample_signal
