# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-15T05:07:27.059790+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0134` n `12`; crypto_alt avg `-0.1127` n `230`; crypto_major avg `-0.1935` n `8`; equity avg `-0.0897` n `93`; fx avg `-0.0073` n `6`; index avg `-0.0314` n `25`; metal avg `-0.0106` n `20`; unknown avg `-0.0187` n `767`
- 1h: commodity avg `-0.0407` n `12`; crypto_alt avg `-0.2175` n `230`; crypto_major avg `-0.1457` n `8`; equity avg `-0.2731` n `93`; fx avg `0.005` n `6`; index avg `-0.0465` n `25`; metal avg `0.0159` n `20`; unknown avg `-0.0175` n `767`
- 4h: commodity avg `-0.0389` n `12`; crypto_alt avg `-0.0884` n `230`; crypto_major avg `0.1875` n `8`; equity avg `1.0572` n `93`; fx avg `0.0445` n `6`; index avg `0.126` n `25`; metal avg `-0.12` n `20`; unknown avg `-0.2557` n `767`
- 24h: commodity avg `0.0618` n `12`; crypto_alt avg `1.5461` n `230`; crypto_major avg `2.8714` n `8`; equity avg `1.9877` n `92`; fx avg `0.1412` n `6`; index avg `0.5254` n `25`; metal avg `0.3029` n `20`; unknown avg `0.3838` n `740`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1166`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1036`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.095`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.081`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0683`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.064`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0548`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0535`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0465`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0451`, n `668`, weak_sample_signal
