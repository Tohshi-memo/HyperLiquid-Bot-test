# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-04T10:37:28.339173+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0269` n `13`; crypto_alt avg `-0.2094` n `235`; crypto_major avg `-0.1476` n `8`; equity avg `-0.0149` n `143`; fx avg `0.0153` n `6`; index avg `-0.0022` n `26`; metal avg `-0.0005` n `20`; unknown avg `0.1254` n `1079`
- 1h: commodity avg `-0.0129` n `13`; crypto_alt avg `-0.2196` n `235`; crypto_major avg `0.0143` n `8`; equity avg `0.0021` n `143`; fx avg `0.0174` n `6`; index avg `0.0037` n `26`; metal avg `-0.0041` n `20`; unknown avg `-0.0727` n `1077`
- 4h: commodity avg `-0.0173` n `13`; crypto_alt avg `-0.2314` n `235`; crypto_major avg `0.3475` n `8`; equity avg `0.0065` n `143`; fx avg `0.0242` n `6`; index avg `0.0032` n `26`; metal avg `-0.006` n `20`; unknown avg `0.0291` n `1061`
- 24h: commodity avg `0.2252` n `13`; crypto_alt avg `1.5083` n `235`; crypto_major avg `1.3006` n `8`; equity avg `0.2307` n `143`; fx avg `-0.0098` n `6`; index avg `0.0242` n `26`; metal avg `-0.002` n `20`; unknown avg `-0.0272` n `898`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.2004`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1737`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1496`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1433`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1322`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1103`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1037`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0964`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0962`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0936`, n `668`, weak_sample_signal
