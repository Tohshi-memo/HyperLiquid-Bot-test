# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-04T02:52:26.977967+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0061` n `13`; crypto_alt avg `-0.0451` n `235`; crypto_major avg `-0.0178` n `8`; equity avg `0.0085` n `143`; fx avg `-0.0044` n `6`; index avg `0.0001` n `26`; metal avg `-0.0033` n `20`; unknown avg `-0.0134` n `1079`
- 1h: commodity avg `-0.0078` n `13`; crypto_alt avg `0.0525` n `235`; crypto_major avg `-0.0257` n `8`; equity avg `0.0144` n `143`; fx avg `-0.0002` n `6`; index avg `0.0006` n `26`; metal avg `0.0042` n `20`; unknown avg `-0.0594` n `1077`
- 4h: commodity avg `-0.0036` n `13`; crypto_alt avg `0.0414` n `235`; crypto_major avg `-0.0418` n `8`; equity avg `-0.0282` n `143`; fx avg `-0.0138` n `6`; index avg `-0.012` n `26`; metal avg `0.0065` n `20`; unknown avg `-0.0703` n `1071`
- 24h: commodity avg `0.1696` n `13`; crypto_alt avg `1.3953` n `235`; crypto_major avg `0.5611` n `8`; equity avg `0.1434` n `143`; fx avg `-0.0407` n `6`; index avg `0.0049` n `26`; metal avg `-0.0006` n `20`; unknown avg `0.0075` n `898`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.2016`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.186`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1561`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1552`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1269`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1248`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1236`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1099`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1041`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0853`, n `668`, weak_sample_signal
