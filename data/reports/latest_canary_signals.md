# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-18T12:07:24.900670+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0115` n `12`; crypto_alt avg `0.1771` n `230`; crypto_major avg `0.1671` n `8`; equity avg `0.0273` n `96`; fx avg `-0.001` n `6`; index avg `-0.0032` n `25`; metal avg `-0.008` n `20`; unknown avg `0.0849` n `770`
- 1h: commodity avg `-0.0216` n `12`; crypto_alt avg `0.2201` n `230`; crypto_major avg `0.1393` n `8`; equity avg `0.0207` n `96`; fx avg `0.0005` n `6`; index avg `0.0001` n `25`; metal avg `-0.0115` n `20`; unknown avg `0.0716` n `770`
- 4h: commodity avg `0.138` n `12`; crypto_alt avg `0.0962` n `230`; crypto_major avg `0.1279` n `8`; equity avg `-0.0623` n `96`; fx avg `-0.0122` n `6`; index avg `0.041` n `25`; metal avg `-0.0129` n `20`; unknown avg `0.0259` n `769`
- 24h: commodity avg `0.6424` n `12`; crypto_alt avg `-0.272` n `230`; crypto_major avg `0.353` n `8`; equity avg `0.9016` n `96`; fx avg `0.0319` n `6`; index avg `0.1931` n `25`; metal avg `0.3324` n `20`; unknown avg `0.1224` n `737`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1355`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1129`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1034`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0969`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0939`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0892`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0886`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0869`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0847`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0845`, n `668`, weak_sample_signal
