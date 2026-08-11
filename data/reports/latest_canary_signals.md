# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-11T16:41:41.455360+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0105` n `12`; crypto_alt avg `-0.039` n `230`; crypto_major avg `-0.0973` n `8`; equity avg `-0.0525` n `113`; fx avg `-0.0137` n `6`; index avg `-0.0034` n `25`; metal avg `-0.019` n `20`; unknown avg `-0.0762` n `785`
- 1h: commodity avg `-0.0526` n `12`; crypto_alt avg `0.3043` n `230`; crypto_major avg `0.2393` n `8`; equity avg `-0.139` n `113`; fx avg `-0.0165` n `6`; index avg `-0.0056` n `25`; metal avg `0.0537` n `20`; unknown avg `0.0443` n `785`
- 4h: commodity avg `0.0212` n `12`; crypto_alt avg `-1.1705` n `230`; crypto_major avg `-0.8003` n `8`; equity avg `-0.001` n `113`; fx avg `-0.011` n `6`; index avg `-0.0691` n `25`; metal avg `-0.0659` n `20`; unknown avg `0.1367` n `785`
- 24h: commodity avg `0.1881` n `12`; crypto_alt avg `-1.939` n `230`; crypto_major avg `-0.2695` n `8`; equity avg `0.1037` n `113`; fx avg `-0.0653` n `6`; index avg `0.0921` n `25`; metal avg `0.035` n `20`; unknown avg `-0.2831` n `753`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.2135`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2074`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1996`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.192`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1797`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1395`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1365`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.117`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0874`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0869`, n `668`, weak_sample_signal
