# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-12T18:07:29.664622+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1473` n `13`; crypto_alt avg `-0.1677` n `239`; crypto_major avg `-0.1291` n `8`; equity avg `-0.4001` n `162`; fx avg `0.0109` n `6`; index avg `-0.0455` n `27`; metal avg `0.0229` n `20`; unknown avg `0.4218` n `1257`
- 1h: commodity avg `0.3141` n `13`; crypto_alt avg `0.3645` n `239`; crypto_major avg `0.3427` n `8`; equity avg `0.0055` n `162`; fx avg `-0.0087` n `6`; index avg `-0.0069` n `27`; metal avg `0.0347` n `20`; unknown avg `5.5701` n `1253`
- 4h: commodity avg `0.3735` n `13`; crypto_alt avg `0.3179` n `239`; crypto_major avg `0.3234` n `8`; equity avg `1.7017` n `162`; fx avg `-0.062` n `6`; index avg `0.1661` n `27`; metal avg `-0.0667` n `20`; unknown avg `57.3894` n `1229`
- 24h: commodity avg `0.4464` n `13`; crypto_alt avg `-3.284` n `239`; crypto_major avg `-3.3378` n `8`; equity avg `-2.9396` n `162`; fx avg `-0.1412` n `6`; index avg `-0.1471` n `27`; metal avg `-0.7838` n `20`; unknown avg `17.353` n `1139`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1376`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1288`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1075`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0969`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0957`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0931`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0928`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.088`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0876`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0819`, n `668`, weak_sample_signal
