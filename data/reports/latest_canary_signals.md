# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-16T15:22:25.759793+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0016` n `12`; crypto_alt avg `0.0747` n `230`; crypto_major avg `0.0745` n `8`; equity avg `0.0105` n `94`; fx avg `0.004` n `6`; index avg `-0.0079` n `25`; metal avg `0.0824` n `20`; unknown avg `-0.0219` n `768`
- 1h: commodity avg `-0.4122` n `12`; crypto_alt avg `-0.2368` n `230`; crypto_major avg `-0.2867` n `8`; equity avg `-0.4074` n `94`; fx avg `-0.0377` n `6`; index avg `-0.0393` n `25`; metal avg `0.0814` n `20`; unknown avg `-0.1213` n `768`
- 4h: commodity avg `-0.1279` n `12`; crypto_alt avg `0.3958` n `230`; crypto_major avg `0.1381` n `8`; equity avg `-1.256` n `94`; fx avg `0.0162` n `6`; index avg `-0.0615` n `25`; metal avg `-0.157` n `20`; unknown avg `-0.0214` n `768`
- 24h: commodity avg `-0.0047` n `12`; crypto_alt avg `-0.8479` n `230`; crypto_major avg `-1.5223` n `8`; equity avg `-2.475` n `94`; fx avg `-0.0727` n `6`; index avg `-0.2075` n `25`; metal avg `-0.1994` n `20`; unknown avg `-0.2758` n `746`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1421`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.102`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1012`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.097`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0938`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.083`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0798`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0775`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0734`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0703`, n `668`, weak_sample_signal
