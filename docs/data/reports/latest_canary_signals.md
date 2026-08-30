# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-30T18:07:30.802353+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0025` n `12`; crypto_alt avg `-0.0391` n `231`; crypto_major avg `0.0221` n `8`; equity avg `-0.0062` n `128`; fx avg `-0.0012` n `6`; index avg `-0.0153` n `26`; metal avg `-0.0135` n `20`; unknown avg `0.0244` n `793`
- 1h: commodity avg `0.0118` n `12`; crypto_alt avg `-0.2816` n `231`; crypto_major avg `-0.3546` n `8`; equity avg `-0.0234` n `128`; fx avg `-0.0041` n `6`; index avg `-0.0047` n `26`; metal avg `-0.022` n `20`; unknown avg `-0.0032` n `793`
- 4h: commodity avg `0.0551` n `12`; crypto_alt avg `0.1679` n `231`; crypto_major avg `0.1277` n `8`; equity avg `0.0937` n `128`; fx avg `0.0097` n `6`; index avg `0.0176` n `26`; metal avg `0.045` n `20`; unknown avg `0.3711` n `793`
- 24h: commodity avg `0.0392` n `12`; crypto_alt avg `1.785` n `231`; crypto_major avg `1.1318` n `8`; equity avg `0.3768` n `128`; fx avg `0.0164` n `6`; index avg `0.0965` n `26`; metal avg `0.1142` n `20`; unknown avg `0.1925` n `740`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.1224`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1164`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1146`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1109`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0991`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0923`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0814`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0811`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0797`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0606`, n `668`, weak_sample_signal
