# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-15T01:37:25.450962+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0547` n `12`; crypto_alt avg `0.0467` n `230`; crypto_major avg `0.0069` n `8`; equity avg `-0.0193` n `93`; fx avg `0.0138` n `6`; index avg `0.0049` n `25`; metal avg `-0.074` n `20`; unknown avg `-0.0023` n `767`
- 1h: commodity avg `-0.1498` n `12`; crypto_alt avg `0.097` n `230`; crypto_major avg `-0.1157` n `8`; equity avg `0.0216` n `93`; fx avg `-0.0115` n `6`; index avg `0.0052` n `25`; metal avg `-0.0219` n `20`; unknown avg `0.0828` n `767`
- 4h: commodity avg `0.0668` n `12`; crypto_alt avg `0.289` n `230`; crypto_major avg `-0.0901` n `8`; equity avg `0.4086` n `93`; fx avg `0.0354` n `6`; index avg `0.0779` n `25`; metal avg `-0.0185` n `20`; unknown avg `0.4519` n `765`
- 24h: commodity avg `0.1274` n `12`; crypto_alt avg `1.8367` n `230`; crypto_major avg `2.9758` n `8`; equity avg `1.7804` n `92`; fx avg `0.0837` n `6`; index avg `0.4926` n `25`; metal avg `0.7127` n `20`; unknown avg `0.2082` n `740`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1041`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.101`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0878`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0861`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0834`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0833`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.073`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0654`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0564`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0545`, n `668`, weak_sample_signal
