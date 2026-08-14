# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-14T02:44:26.963240+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0626` n `12`; crypto_alt avg `-0.0762` n `230`; crypto_major avg `0.01` n `8`; equity avg `0.0636` n `113`; fx avg `-0.0172` n `6`; index avg `0.0022` n `25`; metal avg `0.092` n `20`; unknown avg `-0.1041` n `787`
- 1h: commodity avg `0.0451` n `12`; crypto_alt avg `-0.0239` n `230`; crypto_major avg `-0.0143` n `8`; equity avg `0.1074` n `113`; fx avg `-0.021` n `6`; index avg `0.0407` n `25`; metal avg `0.0621` n `20`; unknown avg `-0.1306` n `787`
- 4h: commodity avg `0.0609` n `12`; crypto_alt avg `-0.0629` n `230`; crypto_major avg `-0.1548` n `8`; equity avg `-0.3183` n `113`; fx avg `-0.056` n `6`; index avg `-0.0493` n `25`; metal avg `-0.1457` n `20`; unknown avg `0.6818` n `787`
- 24h: commodity avg `-0.2802` n `12`; crypto_alt avg `0.412` n `230`; crypto_major avg `0.4956` n `8`; equity avg `0.9214` n `113`; fx avg `-0.0073` n `6`; index avg `0.2409` n `25`; metal avg `-0.5124` n `20`; unknown avg `1.1117` n `754`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2454`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.2082`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1973`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1865`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1733`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1645`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.162`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1554`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1476`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1464`, n `668`, weak_sample_signal
