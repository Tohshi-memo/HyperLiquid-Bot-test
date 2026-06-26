# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-26T19:12:43.628813+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.022` n `12`; crypto_alt avg `0.4788` n `228`; crypto_major avg `0.5631` n `8`; equity avg `0.3331` n `88`; fx avg `-0.0017` n `6`; index avg `0.0129` n `23`; metal avg `0.0037` n `20`; unknown avg `-0.3732` n `764`
- 1h: commodity avg `-0.1469` n `12`; crypto_alt avg `0.0551` n `228`; crypto_major avg `-0.0443` n `8`; equity avg `-0.2063` n `88`; fx avg `-0.0024` n `6`; index avg `-0.0802` n `23`; metal avg `-0.0655` n `20`; unknown avg `-0.5114` n `764`
- 4h: commodity avg `-0.0523` n `12`; crypto_alt avg `1.5181` n `228`; crypto_major avg `1.238` n `8`; equity avg `0.4801` n `87`; fx avg `-0.002` n `6`; index avg `0.0377` n `23`; metal avg `-0.0435` n `20`; unknown avg `-0.3817` n `764`
- 24h: commodity avg `-0.6202` n `12`; crypto_alt avg `3.0553` n `228`; crypto_major avg `2.8467` n `8`; equity avg `-0.3558` n `87`; fx avg `-0.0759` n `6`; index avg `-0.2698` n `23`; metal avg `0.4913` n `20`; unknown avg `0.0272` n `700`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.2156`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2139`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1577`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1136`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1081`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1076`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1038`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.103`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.096`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0939`, n `668`, weak_sample_signal
