# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-27T12:00:09.690226+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0101` n `12`; crypto_alt avg `0.1064` n `228`; crypto_major avg `0.0168` n `8`; equity avg `-0.0013` n `88`; fx avg `-0.0018` n `6`; index avg `-0.0018` n `23`; metal avg `0.0019` n `20`; unknown avg `0.0504` n `764`
- 1h: commodity avg `0.0356` n `12`; crypto_alt avg `0.2028` n `228`; crypto_major avg `0.0535` n `8`; equity avg `-0.0556` n `88`; fx avg `-0.0024` n `6`; index avg `-0.0084` n `23`; metal avg `-0.0049` n `20`; unknown avg `0.2379` n `764`
- 4h: commodity avg `0.0681` n `12`; crypto_alt avg `-0.0807` n `228`; crypto_major avg `-0.3872` n `8`; equity avg `-0.0349` n `88`; fx avg `0.0104` n `6`; index avg `-0.0252` n `23`; metal avg `-0.0147` n `20`; unknown avg `0.0736` n `764`
- 24h: commodity avg `0.0798` n `12`; crypto_alt avg `2.1132` n `228`; crypto_major avg `2.0699` n `8`; equity avg `1.8251` n `87`; fx avg `0.0362` n `6`; index avg `0.0633` n `23`; metal avg `0.3751` n `20`; unknown avg `0.2357` n `700`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.206`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1619`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1357`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1095`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.101`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0928`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0889`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0851`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0806`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0776`, n `668`, weak_sample_signal
