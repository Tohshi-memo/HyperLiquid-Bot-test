# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-07T20:22:22.518508+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0184` n `13`; crypto_alt avg `-0.1314` n `239`; crypto_major avg `-0.0895` n `8`; equity avg `-0.0116` n `158`; fx avg `0.0005` n `6`; index avg `0.0002` n `27`; metal avg `-0.0054` n `20`; unknown avg `-0.1459` n `1262`
- 1h: commodity avg `0.0345` n `13`; crypto_alt avg `-0.1081` n `239`; crypto_major avg `-0.1624` n `8`; equity avg `-0.0348` n `158`; fx avg `0.0129` n `6`; index avg `0.0025` n `27`; metal avg `0.0024` n `20`; unknown avg `0.4071` n `1248`
- 4h: commodity avg `0.0447` n `13`; crypto_alt avg `-0.0347` n `239`; crypto_major avg `-0.0541` n `8`; equity avg `0.085` n `158`; fx avg `0.0082` n `6`; index avg `0.0113` n `27`; metal avg `-0.0129` n `20`; unknown avg `0.3546` n `1217`
- 24h: commodity avg `-0.0006` n `13`; crypto_alt avg `-1.5268` n `239`; crypto_major avg `-0.5665` n `8`; equity avg `-0.0324` n `158`; fx avg `0.0021` n `6`; index avg `0.0304` n `27`; metal avg `0.0157` n `20`; unknown avg `22.0228` n `1083`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.213`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1647`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1622`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1288`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1228`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1089`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1061`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1057`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1056`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1029`, n `668`, weak_sample_signal
