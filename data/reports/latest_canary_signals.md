# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-04T04:26:34.374716+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0062` n `12`; crypto_alt avg `0.1126` n `230`; crypto_major avg `0.1482` n `8`; equity avg `0.0373` n `107`; fx avg `0.0005` n `6`; index avg `0.0279` n `25`; metal avg `0.048` n `20`; unknown avg `-0.0567` n `781`
- 1h: commodity avg `0.0276` n `12`; crypto_alt avg `0.1753` n `230`; crypto_major avg `0.211` n `8`; equity avg `0.249` n `107`; fx avg `0.035` n `6`; index avg `0.0352` n `25`; metal avg `0.0287` n `20`; unknown avg `-0.1535` n `781`
- 4h: commodity avg `0.0757` n `12`; crypto_alt avg `0.332` n `230`; crypto_major avg `0.4686` n `8`; equity avg `0.0881` n `107`; fx avg `0.0216` n `6`; index avg `-0.0343` n `25`; metal avg `0.1796` n `20`; unknown avg `-0.3126` n `780`
- 24h: commodity avg `0.3232` n `12`; crypto_alt avg `1.1258` n `230`; crypto_major avg `1.0954` n `8`; equity avg `1.5488` n `107`; fx avg `0.041` n `6`; index avg `0.0923` n `25`; metal avg `0.0102` n `20`; unknown avg `0.2257` n `763`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1475`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1185`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1149`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0967`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0919`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0917`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0891`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0813`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0811`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0782`, n `668`, weak_sample_signal
