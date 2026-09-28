# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-28T14:07:33.466726+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.013` n `12`; crypto_alt avg `-0.2642` n `234`; crypto_major avg `-0.219` n `8`; equity avg `0.0564` n `141`; fx avg `-0.0147` n `6`; index avg `-0.0035` n `26`; metal avg `-0.0499` n `20`; unknown avg `108.7554` n `934`
- 1h: commodity avg `-0.0498` n `12`; crypto_alt avg `-0.5414` n `234`; crypto_major avg `-0.2745` n `8`; equity avg `-0.3813` n `141`; fx avg `0.0027` n `6`; index avg `-0.0714` n `26`; metal avg `0.0098` n `20`; unknown avg `530.999` n `934`
- 4h: commodity avg `-0.3495` n `12`; crypto_alt avg `0.9336` n `234`; crypto_major avg `0.8115` n `8`; equity avg `-0.0067` n `141`; fx avg `-0.0052` n `6`; index avg `0.0114` n `26`; metal avg `-0.0637` n `20`; unknown avg `382.0096` n `928`
- 24h: commodity avg `-0.3166` n `12`; crypto_alt avg `-2.8598` n `234`; crypto_major avg `-2.1014` n `8`; equity avg `-2.8514` n `141`; fx avg `0.0153` n `6`; index avg `-0.2446` n `26`; metal avg `-0.9473` n `20`; unknown avg `6.248` n `810`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.2483`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1802`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1584`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1366`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1336`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1169`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1137`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.1074`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1016`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0973`, n `668`, weak_sample_signal
