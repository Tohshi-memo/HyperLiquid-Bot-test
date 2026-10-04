# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-04T08:52:28.187239+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0152` n `13`; crypto_alt avg `-0.1728` n `235`; crypto_major avg `-0.0388` n `8`; equity avg `0.0131` n `143`; fx avg `-0.0012` n `6`; index avg `0.0027` n `26`; metal avg `0.0023` n `20`; unknown avg `0.1073` n `1079`
- 1h: commodity avg `0.0061` n `13`; crypto_alt avg `-0.1131` n `235`; crypto_major avg `0.1016` n `8`; equity avg `0.0169` n `143`; fx avg `0.0` n `6`; index avg `0.0044` n `26`; metal avg `0.0048` n `20`; unknown avg `0.0448` n `1061`
- 4h: commodity avg `0.008` n `13`; crypto_alt avg `0.1947` n `235`; crypto_major avg `0.349` n `8`; equity avg `-0.011` n `143`; fx avg `-0.0182` n `6`; index avg `-0.0013` n `26`; metal avg `0.003` n `20`; unknown avg `0.3843` n `1033`
- 24h: commodity avg `0.1436` n `13`; crypto_alt avg `2.5413` n `235`; crypto_major avg `1.2821` n `8`; equity avg `0.2408` n `143`; fx avg `-0.0436` n `6`; index avg `0.0179` n `26`; metal avg `0.0051` n `20`; unknown avg `-0.0146` n `898`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1946`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1711`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1483`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1413`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1262`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.112`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1074`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1029`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1015`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0961`, n `668`, weak_sample_signal
