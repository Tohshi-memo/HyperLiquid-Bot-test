# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-04T03:37:24.240442+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.004` n `13`; crypto_alt avg `0.0359` n `235`; crypto_major avg `0.0929` n `8`; equity avg `0.0172` n `143`; fx avg `0.0013` n `6`; index avg `0.0003` n `26`; metal avg `0.0011` n `20`; unknown avg `-0.1462` n `1079`
- 1h: commodity avg `-0.0573` n `13`; crypto_alt avg `0.114` n `235`; crypto_major avg `0.1063` n `8`; equity avg `0.0265` n `143`; fx avg `-0.0039` n `6`; index avg `0.0023` n `26`; metal avg `0.0042` n `20`; unknown avg `-0.2318` n `1077`
- 4h: commodity avg `-0.0515` n `13`; crypto_alt avg `-0.027` n `235`; crypto_major avg `0.2` n `8`; equity avg `0.0028` n `143`; fx avg `-0.0011` n `6`; index avg `-0.0055` n `26`; metal avg `0.0128` n `20`; unknown avg `-0.2406` n `1071`
- 24h: commodity avg `0.1063` n `13`; crypto_alt avg `1.3295` n `235`; crypto_major avg `0.7345` n `8`; equity avg `0.1894` n `143`; fx avg `-0.0277` n `6`; index avg `0.0098` n `26`; metal avg `0.0065` n `20`; unknown avg `0.1066` n `898`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.2012`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1849`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.155`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1539`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1238`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1236`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1219`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1086`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1035`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0859`, n `668`, weak_sample_signal
