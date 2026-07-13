# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-13T19:52:42.893040+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0293` n `12`; crypto_alt avg `0.0989` n `230`; crypto_major avg `0.1188` n `8`; equity avg `0.3147` n `92`; fx avg `0.0059` n `6`; index avg `0.0567` n `25`; metal avg `0.0439` n `20`; unknown avg `-0.028` n `766`
- 1h: commodity avg `0.0327` n `12`; crypto_alt avg `0.0851` n `230`; crypto_major avg `0.223` n `8`; equity avg `0.0594` n `92`; fx avg `0.0015` n `6`; index avg `-0.0182` n `25`; metal avg `-0.021` n `20`; unknown avg `-0.0718` n `766`
- 4h: commodity avg `0.5944` n `12`; crypto_alt avg `-0.7685` n `230`; crypto_major avg `-0.4534` n `8`; equity avg `-0.7236` n `92`; fx avg `-0.0053` n `6`; index avg `-0.1261` n `25`; metal avg `-0.1532` n `20`; unknown avg `-0.2053` n `766`
- 24h: commodity avg `0.5811` n `12`; crypto_alt avg `-2.3481` n `230`; crypto_major avg `-2.9707` n `8`; equity avg `-3.1952` n `92`; fx avg `-0.0784` n `6`; index avg `-0.6309` n `25`; metal avg `-0.5463` n `20`; unknown avg `-0.283` n `749`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1889`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.176`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1134`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1117`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1098`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1059`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1054`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0983`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0803`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0677`, n `668`, weak_sample_signal
