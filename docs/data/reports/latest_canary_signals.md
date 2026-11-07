# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-07T05:07:27.224073+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0104` n `13`; crypto_alt avg `0.0296` n `239`; crypto_major avg `0.067` n `8`; equity avg `-0.0376` n `158`; fx avg `0.0007` n `6`; index avg `-0.0014` n `27`; metal avg `-0.0063` n `20`; unknown avg `0.519` n `1257`
- 1h: commodity avg `0.0128` n `13`; crypto_alt avg `0.0603` n `239`; crypto_major avg `-0.0803` n `8`; equity avg `0.0149` n `158`; fx avg `-0.0056` n `6`; index avg `0.0037` n `27`; metal avg `-0.0004` n `20`; unknown avg `0.2138` n `1245`
- 4h: commodity avg `-0.1138` n `13`; crypto_alt avg `-0.4835` n `239`; crypto_major avg `-0.3946` n `8`; equity avg `-0.2056` n `158`; fx avg `0.002` n `6`; index avg `-0.0154` n `27`; metal avg `-0.005` n `20`; unknown avg `1.4748` n `1233`
- 24h: commodity avg `-0.1859` n `13`; crypto_alt avg `0.6248` n `239`; crypto_major avg `0.1437` n `8`; equity avg `1.0589` n `158`; fx avg `-0.0549` n `6`; index avg `0.1338` n `27`; metal avg `0.1954` n `20`; unknown avg `9.2106` n `1006`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2126`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1643`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1558`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1368`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.115`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1126`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1096`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1091`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1009`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0975`, n `668`, weak_sample_signal
