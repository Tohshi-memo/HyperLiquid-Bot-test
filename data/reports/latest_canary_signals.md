# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-09T03:07:26.522874+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0158` n `12`; crypto_alt avg `-0.3191` n `233`; crypto_major avg `-0.2752` n `8`; equity avg `-0.1976` n `134`; fx avg `-0.025` n `6`; index avg `-0.0269` n `26`; metal avg `-0.0374` n `20`; unknown avg `1.8864` n `795`
- 1h: commodity avg `0.0193` n `12`; crypto_alt avg `-0.409` n `233`; crypto_major avg `-0.2755` n `8`; equity avg `-0.0175` n `134`; fx avg `-0.0142` n `6`; index avg `-0.0128` n `26`; metal avg `0.051` n `20`; unknown avg `1.928` n `791`
- 4h: commodity avg `0.0139` n `12`; crypto_alt avg `-0.4933` n `233`; crypto_major avg `0.0137` n `8`; equity avg `0.3491` n `134`; fx avg `-0.0265` n `6`; index avg `0.0795` n `26`; metal avg `0.167` n `20`; unknown avg `1.2154` n `785`
- 24h: commodity avg `0.139` n `12`; crypto_alt avg `-0.6849` n `232`; crypto_major avg `0.6087` n `8`; equity avg `0.4396` n `134`; fx avg `0.0324` n `6`; index avg `-0.1572` n `26`; metal avg `-0.2758` n `20`; unknown avg `2.4895` n `681`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `0.1512`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.112`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1084`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1032`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.101`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.088`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0859`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0824`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0782`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0715`, n `668`, weak_sample_signal
