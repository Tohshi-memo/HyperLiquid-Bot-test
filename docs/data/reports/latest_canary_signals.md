# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-28T19:07:31.361500+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0279` n `13`; crypto_alt avg `-0.1105` n `239`; crypto_major avg `-0.066` n `8`; equity avg `-0.0117` n `168`; fx avg `0.0267` n `6`; index avg `0.0107` n `27`; metal avg `0.0035` n `20`; unknown avg `0.8085` n `1254`
- 1h: commodity avg `0.1227` n `13`; crypto_alt avg `0.2033` n `239`; crypto_major avg `0.2524` n `8`; equity avg `0.1814` n `168`; fx avg `0.0188` n `6`; index avg `0.0193` n `27`; metal avg `0.0176` n `20`; unknown avg `24.8302` n `1258`
- 4h: commodity avg `0.0756` n `13`; crypto_alt avg `-0.4973` n `239`; crypto_major avg `-0.0387` n `8`; equity avg `0.0934` n `168`; fx avg `0.0131` n `6`; index avg `0.0106` n `27`; metal avg `-0.007` n `20`; unknown avg `40.9386` n `1213`
- 24h: commodity avg `0.0861` n `13`; crypto_alt avg `-3.122` n `239`; crypto_major avg `-1.2726` n `8`; equity avg `-0.0323` n `168`; fx avg `0.0018` n `6`; index avg `-0.011` n `27`; metal avg `0.2062` n `20`; unknown avg `72.6965` n `1063`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1616`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1464`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.126`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1253`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.085`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0809`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0803`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0801`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0672`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0543`, n `668`, weak_sample_signal
