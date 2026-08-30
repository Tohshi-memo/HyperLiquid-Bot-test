# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-30T15:37:22.990512+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0243` n `12`; crypto_alt avg `0.0669` n `231`; crypto_major avg `0.0589` n `8`; equity avg `0.0028` n `128`; fx avg `0.0028` n `6`; index avg `0.0007` n `26`; metal avg `0.0196` n `20`; unknown avg `0.2988` n `793`
- 1h: commodity avg `0.0375` n `12`; crypto_alt avg `-0.093` n `231`; crypto_major avg `-0.0546` n `8`; equity avg `-0.0116` n `128`; fx avg `0.0015` n `6`; index avg `-0.0014` n `26`; metal avg `-0.0142` n `20`; unknown avg `0.2297` n `793`
- 4h: commodity avg `0.0211` n `12`; crypto_alt avg `0.4965` n `231`; crypto_major avg `0.7201` n `8`; equity avg `-0.0086` n `128`; fx avg `0.0035` n `6`; index avg `0.0012` n `26`; metal avg `0.0556` n `20`; unknown avg `0.3657` n `793`
- 24h: commodity avg `0.0748` n `12`; crypto_alt avg `1.1072` n `231`; crypto_major avg `0.875` n `8`; equity avg `0.3017` n `128`; fx avg `0.019` n `6`; index avg `0.0684` n `26`; metal avg `0.0999` n `20`; unknown avg `0.1163` n `740`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.1135`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1119`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1081`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1019`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0951`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0889`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0813`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0807`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0753`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0595`, n `668`, weak_sample_signal
