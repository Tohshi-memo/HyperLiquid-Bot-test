# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-29T20:52:37.099514+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.03` n `12`; crypto_alt avg `0.0238` n `234`; crypto_major avg `0.0361` n `8`; equity avg `0.0272` n `142`; fx avg `0.0005` n `6`; index avg `0.0005` n `26`; metal avg `0.0079` n `20`; unknown avg `19.3572` n `960`
- 1h: commodity avg `-0.0356` n `12`; crypto_alt avg `0.4501` n `234`; crypto_major avg `0.2622` n `8`; equity avg `0.0897` n `142`; fx avg `-0.0022` n `6`; index avg `0.0261` n `26`; metal avg `0.0612` n `20`; unknown avg `5.2505` n `900`
- 4h: commodity avg `-0.2926` n `12`; crypto_alt avg `0.683` n `234`; crypto_major avg `0.5853` n `8`; equity avg `0.2096` n `142`; fx avg `0.01` n `6`; index avg `0.1202` n `26`; metal avg `0.2946` n `20`; unknown avg `2.7338` n `900`
- 24h: commodity avg `-1.012` n `12`; crypto_alt avg `1.2311` n `234`; crypto_major avg `-0.0989` n `8`; equity avg `0.7976` n `142`; fx avg `-0.1624` n `6`; index avg `0.1` n `26`; metal avg `0.3011` n `20`; unknown avg `462.7506` n `834`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1984`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1951`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1852`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1531`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1353`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1345`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1339`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1333`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1257`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1231`, n `668`, weak_sample_signal
