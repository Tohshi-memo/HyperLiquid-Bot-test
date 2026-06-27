# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-27T18:22:31.284069+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.009` n `12`; crypto_alt avg `-0.0057` n `228`; crypto_major avg `-0.0546` n `8`; equity avg `0.0097` n `88`; fx avg `0.0` n `6`; index avg `0.0034` n `23`; metal avg `0.0017` n `20`; unknown avg `-0.0206` n `764`
- 1h: commodity avg `-0.0062` n `12`; crypto_alt avg `-0.2602` n `228`; crypto_major avg `-0.3475` n `8`; equity avg `0.011` n `88`; fx avg `0.0011` n `6`; index avg `0.008` n `23`; metal avg `0.0038` n `20`; unknown avg `-0.0394` n `764`
- 4h: commodity avg `-0.1809` n `12`; crypto_alt avg `-0.474` n `228`; crypto_major avg `-0.6086` n `8`; equity avg `-0.1668` n `88`; fx avg `0.005` n `6`; index avg `-0.0293` n `23`; metal avg `-0.0337` n `20`; unknown avg `0.0923` n `764`
- 24h: commodity avg `0.3053` n `12`; crypto_alt avg `-0.3272` n `228`; crypto_major avg `-0.4035` n `8`; equity avg `0.4904` n `88`; fx avg `0.077` n `6`; index avg `-0.0785` n `23`; metal avg `0.0641` n `20`; unknown avg `0.0249` n `700`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.2089`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1671`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1355`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1122`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1054`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0946`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0888`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0839`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0836`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0794`, n `668`, weak_sample_signal
