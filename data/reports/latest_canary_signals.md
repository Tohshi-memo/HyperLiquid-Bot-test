# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-08T19:37:27.908941+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0143` n `13`; crypto_alt avg `0.1105` n `239`; crypto_major avg `0.0661` n `8`; equity avg `0.0581` n `158`; fx avg `0.0056` n `6`; index avg `-0.0116` n `27`; metal avg `0.0006` n `20`; unknown avg `0.6878` n `1254`
- 1h: commodity avg `0.0416` n `13`; crypto_alt avg `-0.0654` n `239`; crypto_major avg `-0.1307` n `8`; equity avg `0.061` n `158`; fx avg `-0.0014` n `6`; index avg `0.0146` n `27`; metal avg `0.0163` n `20`; unknown avg `-0.148` n `1246`
- 4h: commodity avg `-0.1215` n `13`; crypto_alt avg `-0.1737` n `239`; crypto_major avg `-0.2261` n `8`; equity avg `0.4816` n `158`; fx avg `0.0139` n `6`; index avg `0.0489` n `27`; metal avg `0.0388` n `20`; unknown avg `0.439` n `1186`
- 24h: commodity avg `-0.121` n `13`; crypto_alt avg `-1.3692` n `239`; crypto_major avg `-0.2372` n `8`; equity avg `0.4872` n `158`; fx avg `0.0589` n `6`; index avg `0.0188` n `27`; metal avg `-0.0112` n `20`; unknown avg `-0.2696` n `1038`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2056`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1561`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1473`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1176`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1146`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1094`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.109`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1079`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1038`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0964`, n `668`, weak_sample_signal
