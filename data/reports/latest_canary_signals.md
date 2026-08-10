# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-10T23:52:40.481218+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0013` n `12`; crypto_alt avg `0.0637` n `230`; crypto_major avg `-0.0055` n `8`; equity avg `0.007` n `113`; fx avg `-0.0103` n `6`; index avg `0.0025` n `25`; metal avg `-0.0165` n `20`; unknown avg `0.0179` n `785`
- 1h: commodity avg `-0.0034` n `12`; crypto_alt avg `0.0397` n `230`; crypto_major avg `-0.074` n `8`; equity avg `-0.1523` n `113`; fx avg `-0.0035` n `6`; index avg `-0.0225` n `25`; metal avg `-0.0356` n `20`; unknown avg `-0.0878` n `785`
- 4h: commodity avg `-0.0138` n `12`; crypto_alt avg `-0.3718` n `230`; crypto_major avg `-0.364` n `8`; equity avg `-0.4752` n `113`; fx avg `-0.0038` n `6`; index avg `-0.0335` n `25`; metal avg `-0.0157` n `20`; unknown avg `1.5184` n `785`
- 24h: commodity avg `0.79` n `12`; crypto_alt avg `-0.2526` n `230`; crypto_major avg `-0.3923` n `8`; equity avg `-1.7935` n `113`; fx avg `0.2672` n `6`; index avg `-0.0919` n `25`; metal avg `0.3466` n `20`; unknown avg `103.6747` n `752`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1908`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.181`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1805`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1728`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1531`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1416`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.119`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1188`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1133`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1121`, n `668`, weak_sample_signal
