# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-18T18:07:27.729669+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0534` n `12`; crypto_alt avg `-0.0533` n `230`; crypto_major avg `-0.0116` n `8`; equity avg `-0.0414` n `96`; fx avg `0.0027` n `6`; index avg `-0.0027` n `25`; metal avg `-0.0178` n `20`; unknown avg `-0.0271` n `770`
- 1h: commodity avg `0.1241` n `12`; crypto_alt avg `0.2111` n `230`; crypto_major avg `0.2684` n `8`; equity avg `0.0211` n `96`; fx avg `0.0041` n `6`; index avg `0.0034` n `25`; metal avg `-0.0126` n `20`; unknown avg `-0.0671` n `770`
- 4h: commodity avg `0.145` n `12`; crypto_alt avg `0.5548` n `230`; crypto_major avg `0.6376` n `8`; equity avg `-0.0455` n `96`; fx avg `-0.0499` n `6`; index avg `-0.0178` n `25`; metal avg `-0.0568` n `20`; unknown avg `0.0488` n `770`
- 24h: commodity avg `0.2777` n `12`; crypto_alt avg `-0.685` n `230`; crypto_major avg `0.1869` n `8`; equity avg `-1.1643` n `96`; fx avg `-0.1108` n `6`; index avg `-0.0568` n `25`; metal avg `-0.0151` n `20`; unknown avg `-0.087` n `737`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1336`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1124`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1023`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0955`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0915`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0904`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0878`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0826`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0785`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0774`, n `668`, weak_sample_signal
