# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-27T15:07:26.374952+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0112` n `12`; crypto_alt avg `0.1383` n `228`; crypto_major avg `0.1919` n `8`; equity avg `0.0254` n `88`; fx avg `0.0097` n `6`; index avg `0.0076` n `23`; metal avg `-0.013` n `20`; unknown avg `-0.0474` n `764`
- 1h: commodity avg `-0.0407` n `12`; crypto_alt avg `0.3109` n `228`; crypto_major avg `0.3235` n `8`; equity avg `0.0178` n `88`; fx avg `0.0069` n `6`; index avg `0.0051` n `23`; metal avg `-0.0081` n `20`; unknown avg `-0.0652` n `764`
- 4h: commodity avg `0.0751` n `12`; crypto_alt avg `0.8291` n `228`; crypto_major avg `0.8773` n `8`; equity avg `0.0995` n `88`; fx avg `0.0067` n `6`; index avg `0.0121` n `23`; metal avg `-0.0047` n `20`; unknown avg `0.2662` n `764`
- 24h: commodity avg `0.3975` n `12`; crypto_alt avg `1.6907` n `228`; crypto_major avg `1.6345` n `8`; equity avg `1.2813` n `87`; fx avg `0.0806` n `6`; index avg `0.0244` n `23`; metal avg `0.0785` n `20`; unknown avg `0.3063` n `700`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.2059`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1632`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.136`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1101`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1044`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0927`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0889`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0794`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0784`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.077`, n `668`, weak_sample_signal
