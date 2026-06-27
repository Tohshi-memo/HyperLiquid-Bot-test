# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-27T14:52:29.064744+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0258` n `12`; crypto_alt avg `0.1113` n `228`; crypto_major avg `0.0719` n `8`; equity avg `-0.01` n `88`; fx avg `-0.0014` n `6`; index avg `0.0002` n `23`; metal avg `-0.0009` n `20`; unknown avg `0.0169` n `764`
- 1h: commodity avg `-0.0445` n `12`; crypto_alt avg `0.1591` n `228`; crypto_major avg `0.1767` n `8`; equity avg `-0.0062` n `88`; fx avg `-0.0022` n `6`; index avg `0.0183` n `23`; metal avg `0.0038` n `20`; unknown avg `-0.0385` n `764`
- 4h: commodity avg `0.0728` n `12`; crypto_alt avg `0.5549` n `228`; crypto_major avg `0.6272` n `8`; equity avg `0.0677` n `88`; fx avg `-0.0127` n `6`; index avg `-0.0005` n `23`; metal avg `0.0239` n `20`; unknown avg `0.2585` n `764`
- 24h: commodity avg `0.3105` n `12`; crypto_alt avg `1.6289` n `228`; crypto_major avg `1.3995` n `8`; equity avg `0.995` n `87`; fx avg `0.0318` n `6`; index avg `-0.0369` n `23`; metal avg `-0.0254` n `20`; unknown avg `0.2545` n `700`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.2058`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1633`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.136`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1101`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1042`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0927`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0889`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0799`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0782`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0762`, n `668`, weak_sample_signal
