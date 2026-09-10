# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-10T14:37:29.452842+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0325` n `12`; crypto_alt avg `0.2988` n `233`; crypto_major avg `0.1917` n `8`; equity avg `0.5126` n `135`; fx avg `0.0077` n `6`; index avg `0.0653` n `26`; metal avg `0.021` n `20`; unknown avg `0.3615` n `770`
- 1h: commodity avg `-0.0932` n `12`; crypto_alt avg `0.3819` n `233`; crypto_major avg `0.3402` n `8`; equity avg `0.7152` n `135`; fx avg `0.0016` n `6`; index avg `0.0864` n `26`; metal avg `0.0499` n `20`; unknown avg `0.1207` n `768`
- 4h: commodity avg `0.3602` n `12`; crypto_alt avg `-0.3745` n `233`; crypto_major avg `-1.0366` n `8`; equity avg `-0.3588` n `135`; fx avg `0.0114` n `6`; index avg `-0.1968` n `26`; metal avg `-0.3924` n `20`; unknown avg `-0.4812` n `762`
- 24h: commodity avg `0.2396` n `12`; crypto_alt avg `-4.7215` n `233`; crypto_major avg `-3.8729` n `8`; equity avg `-1.6575` n `135`; fx avg `0.1042` n `6`; index avg `-0.2737` n `26`; metal avg `-1.0757` n `20`; unknown avg `-0.6868` n `660`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.131`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1299`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1092`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1082`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1062`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0924`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0872`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0845`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0801`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0786`, n `668`, weak_sample_signal
