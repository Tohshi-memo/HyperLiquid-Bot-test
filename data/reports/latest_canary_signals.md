# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-20T12:37:27.153500+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0571` n `13`; crypto_alt avg `0.151` n `237`; crypto_major avg `0.1519` n `8`; equity avg `0.1221` n `151`; fx avg `0.0003` n `6`; index avg `0.023` n `26`; metal avg `-0.0145` n `20`; unknown avg `1.2106` n `1198`
- 1h: commodity avg `-0.2316` n `13`; crypto_alt avg `0.3413` n `237`; crypto_major avg `0.2587` n `8`; equity avg `0.0396` n `151`; fx avg `0.0135` n `6`; index avg `-0.0038` n `26`; metal avg `-0.0965` n `20`; unknown avg `0.4247` n `1188`
- 4h: commodity avg `-0.0362` n `13`; crypto_alt avg `0.1595` n `237`; crypto_major avg `0.1253` n `8`; equity avg `-0.8074` n `151`; fx avg `-0.0014` n `6`; index avg `-0.1453` n `26`; metal avg `-0.21` n `20`; unknown avg `0.9311` n `1188`
- 24h: commodity avg `0.1755` n `13`; crypto_alt avg `0.0433` n `237`; crypto_major avg `-0.789` n `8`; equity avg `-2.6018` n `151`; fx avg `0.0043` n `6`; index avg `-0.3452` n `26`; metal avg `-0.3489` n `20`; unknown avg `0.655` n `1055`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1901`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1492`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1145`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1041`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1015`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0926`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0918`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0813`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.073`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0707`, n `668`, weak_sample_signal
