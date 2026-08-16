# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-16T08:52:25.731688+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0165` n `12`; crypto_alt avg `0.0011` n `230`; crypto_major avg `0.0149` n `8`; equity avg `0.0246` n `114`; fx avg `0.0012` n `6`; index avg `0.0011` n `25`; metal avg `-0.0043` n `20`; unknown avg `0.0017` n `791`
- 1h: commodity avg `0.0252` n `12`; crypto_alt avg `0.0332` n `230`; crypto_major avg `0.0463` n `8`; equity avg `0.0334` n `114`; fx avg `-0.0069` n `6`; index avg `-0.0002` n `25`; metal avg `0.0044` n `20`; unknown avg `-0.0642` n `791`
- 4h: commodity avg `0.0231` n `12`; crypto_alt avg `0.2833` n `230`; crypto_major avg `0.0575` n `8`; equity avg `0.1177` n `114`; fx avg `0.0026` n `6`; index avg `0.0194` n `25`; metal avg `0.0207` n `20`; unknown avg `-0.0621` n `759`
- 24h: commodity avg `0.1482` n `12`; crypto_alt avg `-0.0157` n `230`; crypto_major avg `0.2665` n `8`; equity avg `0.4041` n `114`; fx avg `-0.0088` n `6`; index avg `0.0523` n `25`; metal avg `0.0344` n `20`; unknown avg `-0.0087` n `759`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2076`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1834`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1806`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1771`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.176`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1507`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1452`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1441`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1423`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1374`, n `668`, weak_sample_signal
