# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-27T17:51:51.663200+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0453` n `12`; crypto_alt avg `-0.023` n `228`; crypto_major avg `-0.0254` n `8`; equity avg `-0.0001` n `88`; fx avg `0.0029` n `6`; index avg `0.001` n `23`; metal avg `-0.0001` n `20`; unknown avg `-0.0431` n `764`
- 1h: commodity avg `-0.0521` n `12`; crypto_alt avg `-0.665` n `228`; crypto_major avg `-0.6533` n `8`; equity avg `-0.1028` n `88`; fx avg `0.0028` n `6`; index avg `-0.0161` n `23`; metal avg `-0.0439` n `20`; unknown avg `0.2194` n `764`
- 4h: commodity avg `-0.1818` n `12`; crypto_alt avg `-0.0529` n `228`; crypto_major avg `-0.1` n `8`; equity avg `-0.1432` n `88`; fx avg `0.0041` n `6`; index avg `-0.01` n `23`; metal avg `-0.0421` n `20`; unknown avg `0.0164` n `764`
- 24h: commodity avg `0.1956` n `12`; crypto_alt avg `-0.1494` n `228`; crypto_major avg `0.0249` n `8`; equity avg `0.2948` n `87`; fx avg `0.0837` n `6`; index avg `-0.1484` n `23`; metal avg `-0.0116` n `20`; unknown avg `0.1377` n `700`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.2078`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.166`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1352`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1115`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1056`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0944`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0888`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0839`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0828`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0809`, n `668`, weak_sample_signal
