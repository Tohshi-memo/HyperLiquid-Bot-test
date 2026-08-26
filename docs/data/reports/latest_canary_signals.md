# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-26T11:07:24.223807+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0155` n `12`; crypto_alt avg `-0.0603` n `231`; crypto_major avg `-0.0862` n `8`; equity avg `0.0569` n `122`; fx avg `0.0007` n `6`; index avg `0.0286` n `25`; metal avg `-0.0027` n `20`; unknown avg `-0.0019` n `797`
- 1h: commodity avg `0.0626` n `12`; crypto_alt avg `0.914` n `231`; crypto_major avg `1.0961` n `8`; equity avg `0.1604` n `122`; fx avg `-0.0045` n `6`; index avg `0.032` n `25`; metal avg `0.0084` n `20`; unknown avg `0.2001` n `797`
- 4h: commodity avg `0.0375` n `12`; crypto_alt avg `-0.0128` n `231`; crypto_major avg `0.2051` n `8`; equity avg `0.089` n `122`; fx avg `-0.0156` n `6`; index avg `0.0017` n `25`; metal avg `-0.0467` n `20`; unknown avg `-0.0039` n `797`
- 24h: commodity avg `-0.2624` n `12`; crypto_alt avg `-1.3669` n `231`; crypto_major avg `-0.9791` n `8`; equity avg `0.4342` n `122`; fx avg `-0.0228` n `6`; index avg `0.0044` n `25`; metal avg `0.1645` n `20`; unknown avg `0.6296` n `779`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1849`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1417`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1309`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1192`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1027`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0933`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0922`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0883`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.078`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0754`, n `668`, weak_sample_signal
