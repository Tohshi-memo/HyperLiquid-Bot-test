# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-26T12:22:23.765327+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0016` n `12`; crypto_alt avg `0.3031` n `231`; crypto_major avg `0.4148` n `8`; equity avg `0.0106` n `122`; fx avg `-0.0056` n `6`; index avg `0.0115` n `25`; metal avg `-0.0289` n `20`; unknown avg `0.0149` n `797`
- 1h: commodity avg `0.0166` n `12`; crypto_alt avg `-0.2203` n `231`; crypto_major avg `-0.245` n `8`; equity avg `-0.266` n `122`; fx avg `-0.0006` n `6`; index avg `-0.018` n `25`; metal avg `-0.0151` n `20`; unknown avg `0.1212` n `797`
- 4h: commodity avg `0.0291` n `12`; crypto_alt avg `-0.1002` n `231`; crypto_major avg `-0.0439` n `8`; equity avg `0.0122` n `122`; fx avg `-0.005` n `6`; index avg `0.0252` n `25`; metal avg `-0.043` n `20`; unknown avg `-0.0667` n `797`
- 24h: commodity avg `-0.1321` n `12`; crypto_alt avg `-0.697` n `231`; crypto_major avg `-0.3397` n `8`; equity avg `0.1737` n `122`; fx avg `-0.0105` n `6`; index avg `-0.0489` n `25`; metal avg `0.1404` n `20`; unknown avg `0.6351` n `779`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1868`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.143`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.125`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1196`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.103`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0924`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0912`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0826`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0744`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.072`, n `668`, weak_sample_signal
