# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-28T13:37:28.877389+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0125` n `12`; crypto_alt avg `-0.0085` n `231`; crypto_major avg `0.0094` n `8`; equity avg `-0.1464` n `127`; fx avg `0.0056` n `6`; index avg `-0.0131` n `26`; metal avg `0.0378` n `20`; unknown avg `-0.0316` n `793`
- 1h: commodity avg `0.1186` n `12`; crypto_alt avg `-0.2402` n `231`; crypto_major avg `0.1736` n `8`; equity avg `-0.1799` n `127`; fx avg `0.0033` n `6`; index avg `0.0084` n `26`; metal avg `0.0747` n `20`; unknown avg `-0.2377` n `792`
- 4h: commodity avg `-0.1517` n `12`; crypto_alt avg `-0.0548` n `231`; crypto_major avg `0.0316` n `8`; equity avg `-0.1538` n `127`; fx avg `0.024` n `6`; index avg `0.0161` n `26`; metal avg `0.1745` n `20`; unknown avg `-0.0499` n `792`
- 24h: commodity avg `-0.1631` n `12`; crypto_alt avg `-0.7782` n `231`; crypto_major avg `0.0769` n `8`; equity avg `-0.7994` n `127`; fx avg `-0.1076` n `6`; index avg `0.0666` n `26`; metal avg `0.956` n `20`; unknown avg `0.4547` n `760`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.1163`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1078`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0994`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0979`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0895`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0828`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0745`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0712`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0669`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0544`, n `668`, weak_sample_signal
