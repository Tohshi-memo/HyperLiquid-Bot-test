# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-27T03:22:32.454061+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0049` n `12`; crypto_alt avg `0.1228` n `228`; crypto_major avg `0.201` n `8`; equity avg `0.0378` n `88`; fx avg `0.0013` n `6`; index avg `0.0088` n `23`; metal avg `-0.0076` n `20`; unknown avg `-0.0236` n `764`
- 1h: commodity avg `0.143` n `12`; crypto_alt avg `-0.0456` n `228`; crypto_major avg `-0.0975` n `8`; equity avg `0.0413` n `88`; fx avg `0.0` n `6`; index avg `0.008` n `23`; metal avg `0.0027` n `20`; unknown avg `4.768` n `764`
- 4h: commodity avg `0.006` n `12`; crypto_alt avg `0.3927` n `228`; crypto_major avg `0.298` n `8`; equity avg `0.2151` n `88`; fx avg `-0.0357` n `6`; index avg `0.0491` n `23`; metal avg `0.0207` n `20`; unknown avg `-0.1675` n `764`
- 24h: commodity avg `-0.081` n `12`; crypto_alt avg `3.5458` n `228`; crypto_major avg `3.3551` n `8`; equity avg `2.3174` n `87`; fx avg `-0.0212` n `6`; index avg `0.2217` n `23`; metal avg `1.3411` n `20`; unknown avg `0.276` n `700`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2128`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.2083`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1632`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1139`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1129`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.108`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1039`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1032`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0961`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0958`, n `668`, weak_sample_signal
