# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-06T06:37:26.659774+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0584` n `13`; crypto_alt avg `0.3942` n `239`; crypto_major avg `0.2827` n `8`; equity avg `0.2336` n `158`; fx avg `-0.0111` n `6`; index avg `0.014` n `27`; metal avg `0.0166` n `20`; unknown avg `0.6983` n `1254`
- 1h: commodity avg `0.1346` n `13`; crypto_alt avg `0.3927` n `239`; crypto_major avg `0.1719` n `8`; equity avg `-0.1281` n `158`; fx avg `-0.0428` n `6`; index avg `-0.0807` n `27`; metal avg `0.0229` n `20`; unknown avg `0.6124` n `1228`
- 4h: commodity avg `0.0397` n `13`; crypto_alt avg `0.1927` n `239`; crypto_major avg `-0.5805` n `8`; equity avg `-0.8352` n `158`; fx avg `-0.0499` n `6`; index avg `-0.1526` n `27`; metal avg `-0.1963` n `20`; unknown avg `0.5024` n `1216`
- 24h: commodity avg `1.4848` n `13`; crypto_alt avg `-3.9676` n `239`; crypto_major avg `-5.5375` n `8`; equity avg `-5.77` n `158`; fx avg `0.0024` n `6`; index avg `-0.7615` n `27`; metal avg `-0.433` n `20`; unknown avg `232.2133` n `1031`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2393`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1731`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1646`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1631`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1619`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1555`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1474`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.145`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.136`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1138`, n `668`, weak_sample_signal
