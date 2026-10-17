# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-17T12:37:31.694908+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.007` n `13`; crypto_alt avg `-0.0748` n `236`; crypto_major avg `-0.0404` n `8`; equity avg `-0.0091` n `151`; fx avg `-0.0124` n `6`; index avg `0.0025` n `26`; metal avg `0.0019` n `20`; unknown avg `0.0348` n `1193`
- 1h: commodity avg `0.0136` n `13`; crypto_alt avg `-0.4` n `236`; crypto_major avg `-0.3092` n `8`; equity avg `-0.1287` n `151`; fx avg `0.0069` n `6`; index avg `-0.0421` n `26`; metal avg `-0.0068` n `20`; unknown avg `2.9128` n `1185`
- 4h: commodity avg `-0.0007` n `13`; crypto_alt avg `-0.6556` n `236`; crypto_major avg `-0.4895` n `8`; equity avg `-0.065` n `151`; fx avg `0.0229` n `6`; index avg `-0.021` n `26`; metal avg `-0.0041` n `20`; unknown avg `3.0587` n `1183`
- 24h: commodity avg `0.555` n `13`; crypto_alt avg `-3.1314` n `236`; crypto_major avg `-1.8957` n `8`; equity avg `-3.3624` n `151`; fx avg `0.0284` n `6`; index avg `-0.5694` n `26`; metal avg `-0.2061` n `20`; unknown avg `10.786` n `954`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.179`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1462`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1206`, n `666`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1163`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1017`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.097`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0749`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0716`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0685`, n `666`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0638`, n `666`, weak_sample_signal
