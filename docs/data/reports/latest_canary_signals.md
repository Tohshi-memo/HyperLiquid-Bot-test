# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-11T17:37:28.810296+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0164` n `12`; crypto_alt avg `-0.0388` n `230`; crypto_major avg `0.0747` n `8`; equity avg `0.0554` n `113`; fx avg `0.0036` n `6`; index avg `0.0071` n `25`; metal avg `-0.0258` n `20`; unknown avg `0.0004` n `785`
- 1h: commodity avg `0.1029` n `12`; crypto_alt avg `-0.0225` n `230`; crypto_major avg `0.1577` n `8`; equity avg `-0.0361` n `113`; fx avg `0.0041` n `6`; index avg `-0.0494` n `25`; metal avg `-0.0636` n `20`; unknown avg `-0.0363` n `785`
- 4h: commodity avg `0.2266` n `12`; crypto_alt avg `-1.1272` n `230`; crypto_major avg `-0.4459` n `8`; equity avg `-0.0545` n `113`; fx avg `-0.0053` n `6`; index avg `-0.0888` n `25`; metal avg `-0.1394` n `20`; unknown avg `-0.0989` n `785`
- 24h: commodity avg `0.1845` n `12`; crypto_alt avg `-2.1045` n `230`; crypto_major avg `-0.3307` n `8`; equity avg `0.0751` n `113`; fx avg `-0.0618` n `6`; index avg `0.0546` n `25`; metal avg `-0.0384` n `20`; unknown avg `-0.326` n `753`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2081`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.2006`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1997`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1929`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1803`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1495`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1382`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1268`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0875`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0871`, n `668`, weak_sample_signal
