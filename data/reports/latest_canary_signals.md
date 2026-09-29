# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-29T22:22:32.699542+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0366` n `12`; crypto_alt avg `-0.1194` n `234`; crypto_major avg `0.063` n `8`; equity avg `0.0363` n `142`; fx avg `0.0004` n `6`; index avg `0.0233` n `26`; metal avg `-0.0001` n `20`; unknown avg `1.7247` n `962`
- 1h: commodity avg `-0.0658` n `12`; crypto_alt avg `-0.0808` n `234`; crypto_major avg `0.2017` n `8`; equity avg `0.1094` n `142`; fx avg `0.0118` n `6`; index avg `0.0519` n `26`; metal avg `0.0301` n `20`; unknown avg `0.5244` n `934`
- 4h: commodity avg `-0.1397` n `12`; crypto_alt avg `0.0709` n `234`; crypto_major avg `0.1926` n `8`; equity avg `0.2432` n `142`; fx avg `0.0017` n `6`; index avg `0.0951` n `26`; metal avg `0.1576` n `20`; unknown avg `2.3853` n `872`
- 24h: commodity avg `-1.0013` n `12`; crypto_alt avg `1.5552` n `234`; crypto_major avg `0.4927` n `8`; equity avg `0.8259` n `142`; fx avg `-0.1729` n `6`; index avg `0.1114` n `26`; metal avg `0.2553` n `20`; unknown avg `3099.8808` n `834`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1925`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1894`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1777`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1473`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1351`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1326`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1265`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1217`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1169`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1095`, n `668`, weak_sample_signal
