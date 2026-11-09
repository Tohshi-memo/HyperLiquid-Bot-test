# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-09T21:02:00.161062+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0489` n `13`; crypto_alt avg `-0.0803` n `239`; crypto_major avg `-0.107` n `8`; equity avg `-0.0952` n `160`; fx avg `0.011` n `6`; index avg `-0.0257` n `27`; metal avg `-0.0149` n `20`; unknown avg `3.2983` n `1229`
- 1h: commodity avg `0.2385` n `13`; crypto_alt avg `-0.0828` n `239`; crypto_major avg `0.1371` n `8`; equity avg `-0.1513` n `160`; fx avg `0.0258` n `6`; index avg `-0.0011` n `27`; metal avg `-0.0073` n `20`; unknown avg `6.5688` n `1225`
- 4h: commodity avg `-0.1015` n `13`; crypto_alt avg `-0.2702` n `239`; crypto_major avg `0.0133` n `8`; equity avg `-0.041` n `160`; fx avg `0.0014` n `6`; index avg `0.0769` n `27`; metal avg `0.2444` n `20`; unknown avg `4.983` n `1215`
- 24h: commodity avg `-0.2939` n `13`; crypto_alt avg `0.5222` n `239`; crypto_major avg `-2.134` n `8`; equity avg `4.1498` n `160`; fx avg `-0.1237` n `6`; index avg `0.5468` n `27`; metal avg `0.6574` n `20`; unknown avg `6.4248` n `1064`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.166`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1485`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1376`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1353`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1331`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.121`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1164`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1054`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1044`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1032`, n `668`, weak_sample_signal
