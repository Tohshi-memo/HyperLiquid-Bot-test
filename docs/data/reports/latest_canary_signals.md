# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-03T17:52:25.085114+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0034` n `12`; crypto_alt avg `0.0217` n `229`; crypto_major avg `-0.0327` n `8`; equity avg `-0.0037` n `88`; fx avg `0.0006` n `6`; index avg `-0.0043` n `25`; metal avg `-0.0018` n `20`; unknown avg `1.0778` n `765`
- 1h: commodity avg `0.0299` n `12`; crypto_alt avg `0.2368` n `229`; crypto_major avg `0.3933` n `8`; equity avg `0.0566` n `88`; fx avg `0.001` n `6`; index avg `0.0219` n `25`; metal avg `-0.0031` n `20`; unknown avg `1.1166` n `765`
- 4h: commodity avg `0.0098` n `12`; crypto_alt avg `0.1802` n `229`; crypto_major avg `0.2209` n `8`; equity avg `0.0707` n `88`; fx avg `-0.0325` n `6`; index avg `-0.0109` n `25`; metal avg `0.0274` n `20`; unknown avg `1.861` n `765`
- 24h: commodity avg `0.2123` n `12`; crypto_alt avg `2.7234` n `229`; crypto_major avg `2.3643` n `8`; equity avg `2.6809` n `88`; fx avg `-0.0311` n `6`; index avg `0.7526` n `25`; metal avg `0.7299` n `20`; unknown avg `10.2694` n `739`

## Correlations

- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1028`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0975`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0797`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0777`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0745`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0737`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0719`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0678`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.065`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0542`, n `668`, weak_sample_signal
