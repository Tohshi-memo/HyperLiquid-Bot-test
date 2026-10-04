# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-04T11:37:29.165259+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0242` n `13`; crypto_alt avg `-0.1468` n `235`; crypto_major avg `-0.0226` n `8`; equity avg `-0.0093` n `143`; fx avg `-0.0017` n `6`; index avg `-0.0058` n `26`; metal avg `0.0004` n `20`; unknown avg `-0.1368` n `1079`
- 1h: commodity avg `0.0325` n `13`; crypto_alt avg `-0.0141` n `235`; crypto_major avg `-0.0045` n `8`; equity avg `0.0158` n `143`; fx avg `0.0026` n `6`; index avg `0.0017` n `26`; metal avg `0.0004` n `20`; unknown avg `-0.0066` n `1077`
- 4h: commodity avg `0.0353` n `13`; crypto_alt avg `-0.3296` n `235`; crypto_major avg `0.3441` n `8`; equity avg `0.0422` n `143`; fx avg `0.0231` n `6`; index avg `0.0101` n `26`; metal avg `-0.0071` n `20`; unknown avg `-0.0511` n `1061`
- 24h: commodity avg `0.1831` n `13`; crypto_alt avg `1.3868` n `235`; crypto_major avg `1.2793` n `8`; equity avg `0.2575` n `143`; fx avg `-0.0029` n `6`; index avg `0.0388` n `26`; metal avg `-0.0041` n `20`; unknown avg `0.0417` n `898`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.2075`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1798`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1501`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1492`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1359`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1095`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.102`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.095`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0934`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0929`, n `668`, weak_sample_signal
