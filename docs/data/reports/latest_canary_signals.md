# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-12T14:22:28.981870+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0241` n `12`; crypto_alt avg `-0.0391` n `230`; crypto_major avg `-0.0367` n `8`; equity avg `-0.016` n `92`; fx avg `-0.0015` n `6`; index avg `-0.0016` n `25`; metal avg `-0.003` n `20`; unknown avg `-0.003` n `765`
- 1h: commodity avg `0.011` n `12`; crypto_alt avg `-0.1992` n `230`; crypto_major avg `-0.1322` n `8`; equity avg `-0.0351` n `92`; fx avg `0.0061` n `6`; index avg `0.0206` n `25`; metal avg `-0.0259` n `20`; unknown avg `0.0013` n `765`
- 4h: commodity avg `-0.0468` n `12`; crypto_alt avg `-0.1052` n `230`; crypto_major avg `0.3034` n `8`; equity avg `0.0319` n `92`; fx avg `0.0068` n `6`; index avg `0.0075` n `25`; metal avg `-0.0221` n `20`; unknown avg `-0.2119` n `763`
- 24h: commodity avg `0.4946` n `12`; crypto_alt avg `-1.3365` n `230`; crypto_major avg `-0.7196` n `8`; equity avg `-0.0024` n `92`; fx avg `0.0165` n `6`; index avg `-0.1017` n `25`; metal avg `-0.1159` n `20`; unknown avg `0.0823` n `745`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1818`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1647`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1361`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1304`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1223`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1176`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1085`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1063`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1032`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.101`, n `668`, weak_sample_signal
