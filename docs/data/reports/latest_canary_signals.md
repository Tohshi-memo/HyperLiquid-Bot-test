# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-27T06:22:29.881428+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.017` n `13`; crypto_alt avg `-0.0038` n `239`; crypto_major avg `-0.0642` n `8`; equity avg `0.0889` n `168`; fx avg `-0.0077` n `6`; index avg `0.0058` n `27`; metal avg `0.0841` n `20`; unknown avg `1.1115` n `1261`
- 1h: commodity avg `-0.0544` n `13`; crypto_alt avg `0.1896` n `239`; crypto_major avg `-0.0174` n `8`; equity avg `0.2195` n `168`; fx avg `0.0074` n `6`; index avg `-0.002` n `27`; metal avg `0.1251` n `20`; unknown avg `0.7617` n `1239`
- 4h: commodity avg `0.1511` n `13`; crypto_alt avg `0.6678` n `239`; crypto_major avg `1.1984` n `8`; equity avg `2.1728` n `168`; fx avg `0.0171` n `6`; index avg `0.1455` n `27`; metal avg `0.4878` n `20`; unknown avg `64.2903` n `1235`
- 24h: commodity avg `0.4184` n `13`; crypto_alt avg `2.2888` n `239`; crypto_major avg `2.7908` n `8`; equity avg `4.2569` n `168`; fx avg `0.0313` n `6`; index avg `0.358` n `27`; metal avg `1.175` n `20`; unknown avg `223.1593` n `991`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1142`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1084`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.107`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1017`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0977`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0959`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0861`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0834`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0828`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.078`, n `668`, weak_sample_signal
