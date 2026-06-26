# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-26T20:52:29.073481+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0298` n `12`; crypto_alt avg `0.0808` n `228`; crypto_major avg `0.1052` n `8`; equity avg `0.0614` n `88`; fx avg `0.0138` n `6`; index avg `-0.0082` n `23`; metal avg `0.056` n `20`; unknown avg `-0.1175` n `764`
- 1h: commodity avg `0.1367` n `12`; crypto_alt avg `-0.3759` n `228`; crypto_major avg `-0.5418` n `8`; equity avg `-0.0313` n `88`; fx avg `0.0191` n `6`; index avg `-0.0638` n `23`; metal avg `-0.0657` n `20`; unknown avg `-0.7009` n `764`
- 4h: commodity avg `0.0505` n `12`; crypto_alt avg `-0.0611` n `228`; crypto_major avg `-0.2287` n `8`; equity avg `-0.1914` n `87`; fx avg `0.0063` n `6`; index avg `-0.1896` n `23`; metal avg `-0.1561` n `20`; unknown avg `-0.4228` n `764`
- 24h: commodity avg `-0.2593` n `12`; crypto_alt avg `2.3806` n `228`; crypto_major avg `2.2952` n `8`; equity avg `-0.5944` n `87`; fx avg `-0.0657` n `6`; index avg `-0.3756` n `23`; metal avg `0.5734` n `20`; unknown avg `-0.3783` n `700`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.2232`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2163`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1681`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1136`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1088`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1075`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1045`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1029`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.099`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0983`, n `668`, weak_sample_signal
