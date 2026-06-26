# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-26T19:52:29.489224+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0273` n `12`; crypto_alt avg `-0.0274` n `228`; crypto_major avg `0.0172` n `8`; equity avg `0.0575` n `88`; fx avg `-0.0044` n `6`; index avg `-0.0027` n `23`; metal avg `0.0405` n `20`; unknown avg `0.0373` n `764`
- 1h: commodity avg `0.0889` n `12`; crypto_alt avg `0.4037` n `228`; crypto_major avg `0.662` n `8`; equity avg `0.4162` n `88`; fx avg `-0.0125` n `6`; index avg `-0.0071` n `23`; metal avg `0.0478` n `20`; unknown avg `0.0541` n `764`
- 4h: commodity avg `-0.0872` n `12`; crypto_alt avg `0.9136` n `228`; crypto_major avg `0.6489` n `8`; equity avg `-0.0874` n `87`; fx avg `-0.0345` n `6`; index avg `-0.0931` n `23`; metal avg `-0.0777` n `20`; unknown avg `-0.0828` n `764`
- 24h: commodity avg `-0.4689` n `12`; crypto_alt avg `3.1945` n `228`; crypto_major avg `3.1071` n `8`; equity avg `-0.2715` n `87`; fx avg `-0.0828` n `6`; index avg `-0.2705` n `23`; metal avg `0.635` n `20`; unknown avg `0.0032` n `700`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.2193`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.215`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1633`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1125`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1078`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1073`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.103`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1019`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0966`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0957`, n `668`, weak_sample_signal
