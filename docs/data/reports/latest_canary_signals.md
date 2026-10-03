# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-03T23:52:26.126602+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0068` n `13`; crypto_alt avg `0.045` n `235`; crypto_major avg `0.0178` n `8`; equity avg `-0.0006` n `143`; fx avg `0.0006` n `6`; index avg `0.0018` n `26`; metal avg `0.0013` n `20`; unknown avg `0.1315` n `1079`
- 1h: commodity avg `-0.0102` n `13`; crypto_alt avg `0.2771` n `235`; crypto_major avg `-0.0996` n `8`; equity avg `-0.0137` n `143`; fx avg `-0.0116` n `6`; index avg `-0.0025` n `26`; metal avg `0.0024` n `20`; unknown avg `0.2673` n `1077`
- 4h: commodity avg `0.0699` n `13`; crypto_alt avg `0.5798` n `235`; crypto_major avg `0.0004` n `8`; equity avg `0.0812` n `143`; fx avg `0.012` n `6`; index avg `0.0` n `26`; metal avg `-0.0012` n `20`; unknown avg `0.2878` n `1055`
- 24h: commodity avg `-0.0186` n `13`; crypto_alt avg `1.808` n `235`; crypto_major avg `0.558` n `8`; equity avg `0.1742` n `143`; fx avg `-0.0109` n `6`; index avg `0.0483` n `26`; metal avg `-0.0156` n `20`; unknown avg `0.0339` n `898`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.199`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1854`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1557`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1544`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1355`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1322`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1174`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1127`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1059`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0888`, n `668`, weak_sample_signal
