# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-01T20:37:55.379258+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0179` n `13`; crypto_alt avg `-0.0574` n `234`; crypto_major avg `-0.1362` n `8`; equity avg `-0.0211` n `142`; fx avg `0.0001` n `6`; index avg `-0.0065` n `26`; metal avg `-0.026` n `20`; unknown avg `2.5456` n `985`
- 1h: commodity avg `-0.086` n `13`; crypto_alt avg `0.6742` n `234`; crypto_major avg `0.2804` n `8`; equity avg `0.065` n `142`; fx avg `-0.0052` n `6`; index avg `0.0117` n `26`; metal avg `-0.0213` n `20`; unknown avg `3.7954` n `933`
- 4h: commodity avg `0.2428` n `13`; crypto_alt avg `0.7391` n `234`; crypto_major avg `0.4889` n `8`; equity avg `0.7686` n `142`; fx avg `-0.0049` n `6`; index avg `0.157` n `26`; metal avg `0.1021` n `20`; unknown avg `0.3435` n `933`
- 24h: commodity avg `0.0409` n `13`; crypto_alt avg `0.0097` n `234`; crypto_major avg `-0.0307` n `8`; equity avg `0.9048` n `142`; fx avg `-0.111` n `6`; index avg `0.1809` n `26`; metal avg `-0.0413` n `20`; unknown avg `0.1894` n `856`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1711`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1526`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1224`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1168`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1151`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1146`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0941`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0937`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0888`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0831`, n `668`, weak_sample_signal
