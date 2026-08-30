# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-30T17:52:25.891121+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.012` n `12`; crypto_alt avg `-0.0328` n `231`; crypto_major avg `-0.0198` n `8`; equity avg `-0.0019` n `128`; fx avg `-0.0013` n `6`; index avg `0.0105` n `26`; metal avg `-0.0083` n `20`; unknown avg `-0.0579` n `793`
- 1h: commodity avg `0.0324` n `12`; crypto_alt avg `-0.1314` n `231`; crypto_major avg `-0.3839` n `8`; equity avg `-0.0225` n `128`; fx avg `0.0035` n `6`; index avg `0.0101` n `26`; metal avg `-0.0155` n `20`; unknown avg `-0.0163` n `793`
- 4h: commodity avg `0.0491` n `12`; crypto_alt avg `0.1539` n `231`; crypto_major avg `0.0775` n `8`; equity avg `0.1072` n `128`; fx avg `0.0095` n `6`; index avg `0.0172` n `26`; metal avg `0.0825` n `20`; unknown avg `0.4189` n `793`
- 24h: commodity avg `0.0413` n `12`; crypto_alt avg `1.7565` n `231`; crypto_major avg `1.1108` n `8`; equity avg `0.3846` n `128`; fx avg `0.0147` n `6`; index avg `0.1066` n `26`; metal avg `0.1268` n `20`; unknown avg `0.1098` n `740`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.1237`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1175`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1164`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.112`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1011`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0932`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0831`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0819`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0814`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0608`, n `668`, weak_sample_signal
