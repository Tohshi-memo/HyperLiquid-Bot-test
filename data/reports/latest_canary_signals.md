# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-28T22:37:23.608789+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0037` n `13`; crypto_alt avg `0.1942` n `239`; crypto_major avg `0.2228` n `8`; equity avg `0.0756` n `168`; fx avg `0.0068` n `6`; index avg `0.0072` n `27`; metal avg `0.0002` n `20`; unknown avg `-0.1229` n `1266`
- 1h: commodity avg `0.0987` n `13`; crypto_alt avg `0.4349` n `239`; crypto_major avg `0.4795` n `8`; equity avg `0.0847` n `168`; fx avg `0.0042` n `6`; index avg `0.0132` n `27`; metal avg `0.0194` n `20`; unknown avg `1.0311` n `1254`
- 4h: commodity avg `0.2672` n `13`; crypto_alt avg `0.2007` n `239`; crypto_major avg `0.2803` n `8`; equity avg `0.2361` n `168`; fx avg `-0.0033` n `6`; index avg `0.0328` n `27`; metal avg `0.0423` n `20`; unknown avg `2.3522` n `1182`
- 24h: commodity avg `0.0994` n `13`; crypto_alt avg `-2.9661` n `239`; crypto_major avg `-0.5712` n `8`; equity avg `0.1227` n `168`; fx avg `-0.0059` n `6`; index avg `0.0069` n `27`; metal avg `0.033` n `20`; unknown avg `2.1872` n `1087`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1613`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1454`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.128`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1251`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0861`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0855`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0807`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0726`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0617`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0581`, n `668`, weak_sample_signal
