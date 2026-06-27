# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-27T10:07:31.323071+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0127` n `12`; crypto_alt avg `0.062` n `228`; crypto_major avg `0.085` n `8`; equity avg `-0.0068` n `88`; fx avg `-0.0108` n `6`; index avg `0.005` n `23`; metal avg `0.0052` n `20`; unknown avg `-0.0082` n `764`
- 1h: commodity avg `0.0534` n `12`; crypto_alt avg `-0.0565` n `228`; crypto_major avg `-0.2275` n `8`; equity avg `-0.0143` n `88`; fx avg `0.0006` n `6`; index avg `-0.0021` n `23`; metal avg `-0.0136` n `20`; unknown avg `-0.0672` n `764`
- 4h: commodity avg `0.108` n `12`; crypto_alt avg `-0.1445` n `228`; crypto_major avg `-0.0326` n `8`; equity avg `0.223` n `88`; fx avg `-0.0126` n `6`; index avg `0.0172` n `23`; metal avg `-0.0216` n `20`; unknown avg `-0.0423` n `748`
- 24h: commodity avg `0.2009` n `12`; crypto_alt avg `1.6162` n `228`; crypto_major avg `1.437` n `8`; equity avg `1.8265` n `87`; fx avg `0.0181` n `6`; index avg `0.0818` n `23`; metal avg `0.4249` n `20`; unknown avg `-0.0092` n `700`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.2058`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1604`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1355`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1078`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.101`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0925`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0889`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0833`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0788`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0743`, n `668`, weak_sample_signal
