# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-30T01:07:23.150891+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0009` n `12`; crypto_alt avg `-0.0729` n `231`; crypto_major avg `-0.1496` n `8`; equity avg `-0.0098` n `128`; fx avg `0.0` n `6`; index avg `-0.0041` n `26`; metal avg `0.0007` n `20`; unknown avg `0.0115` n `793`
- 1h: commodity avg `0.0074` n `12`; crypto_alt avg `-0.128` n `231`; crypto_major avg `-0.0955` n `8`; equity avg `-0.0115` n `128`; fx avg `-0.0006` n `6`; index avg `0.0093` n `26`; metal avg `-0.0078` n `20`; unknown avg `3.9974` n `793`
- 4h: commodity avg `-0.0069` n `12`; crypto_alt avg `-0.0363` n `231`; crypto_major avg `-0.0064` n `8`; equity avg `0.014` n `128`; fx avg `0.018` n `6`; index avg `0.0153` n `26`; metal avg `-0.006` n `20`; unknown avg `4.2423` n `774`
- 24h: commodity avg `-0.0387` n `12`; crypto_alt avg `0.308` n `231`; crypto_major avg `0.9453` n `8`; equity avg `0.3661` n `128`; fx avg `-0.001` n `6`; index avg `0.1005` n `26`; metal avg `0.1148` n `20`; unknown avg `0.1108` n `728`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.2275`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1561`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1233`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1024`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0894`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0797`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0631`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.057`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0569`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0568`, n `668`, weak_sample_signal
