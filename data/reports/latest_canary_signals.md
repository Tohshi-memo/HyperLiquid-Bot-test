# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-04T00:07:27.117716+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0032` n `13`; crypto_alt avg `-0.0685` n `235`; crypto_major avg `0.0436` n `8`; equity avg `-0.0114` n `143`; fx avg `-0.0001` n `6`; index avg `-0.0015` n `26`; metal avg `-0.0015` n `20`; unknown avg `0.0383` n `1071`
- 1h: commodity avg `-0.0294` n `13`; crypto_alt avg `0.2108` n `235`; crypto_major avg `0.0286` n `8`; equity avg `-0.0371` n `143`; fx avg `-0.0098` n `6`; index avg `-0.0028` n `26`; metal avg `-0.0008` n `20`; unknown avg `0.1059` n `1071`
- 4h: commodity avg `0.0499` n `13`; crypto_alt avg `0.3032` n `235`; crypto_major avg `-0.1493` n `8`; equity avg `0.0462` n `143`; fx avg `0.0104` n `6`; index avg `0.0011` n `26`; metal avg `-0.0029` n `20`; unknown avg `-0.1317` n `1055`
- 24h: commodity avg `-0.0889` n `13`; crypto_alt avg `1.6949` n `235`; crypto_major avg `0.6237` n `8`; equity avg `0.1401` n `143`; fx avg `-0.0062` n `6`; index avg `0.0418` n `26`; metal avg `-0.019` n `20`; unknown avg `0.0511` n `898`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1987`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1858`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1563`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1543`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1357`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1322`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1175`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1127`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.106`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0885`, n `668`, weak_sample_signal
