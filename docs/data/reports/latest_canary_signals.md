# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-30T14:22:23.286533+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0023` n `12`; crypto_alt avg `-0.1169` n `231`; crypto_major avg `-0.0467` n `8`; equity avg `0.0117` n `128`; fx avg `-0.0038` n `6`; index avg `-0.0002` n `26`; metal avg `0.0282` n `20`; unknown avg `0.0881` n `793`
- 1h: commodity avg `-0.0073` n `12`; crypto_alt avg `0.0` n `231`; crypto_major avg `0.2939` n `8`; equity avg `0.0603` n `128`; fx avg `-0.008` n `6`; index avg `0.0008` n `26`; metal avg `0.0697` n `20`; unknown avg `0.0951` n `793`
- 4h: commodity avg `0.0137` n `12`; crypto_alt avg `0.752` n `231`; crypto_major avg `0.9212` n `8`; equity avg `0.0461` n `128`; fx avg `-0.0074` n `6`; index avg `0.0136` n `26`; metal avg `0.0792` n `20`; unknown avg `0.5334` n `789`
- 24h: commodity avg `-0.0229` n `12`; crypto_alt avg `1.4357` n `231`; crypto_major avg `1.3508` n `8`; equity avg `0.3171` n `128`; fx avg `0.0142` n `6`; index avg `0.0843` n `26`; metal avg `0.1517` n `20`; unknown avg `-0.0745` n `730`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.1124`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1064`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1013`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1008`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0952`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0937`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0832`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0819`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0789`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0621`, n `668`, weak_sample_signal
