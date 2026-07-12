# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-12T12:07:30.017632+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0149` n `12`; crypto_alt avg `-0.0087` n `230`; crypto_major avg `-0.1021` n `8`; equity avg `0.0066` n `92`; fx avg `-0.0007` n `6`; index avg `0.0018` n `25`; metal avg `-0.0073` n `20`; unknown avg `-0.0193` n `765`
- 1h: commodity avg `-0.0411` n `12`; crypto_alt avg `0.1978` n `230`; crypto_major avg `0.2311` n `8`; equity avg `0.0737` n `92`; fx avg `-0.0009` n `6`; index avg `0.0133` n `25`; metal avg `0.0066` n `20`; unknown avg `-0.0003` n `765`
- 4h: commodity avg `-0.0384` n `12`; crypto_alt avg `0.0224` n `230`; crypto_major avg `0.1889` n `8`; equity avg `0.0854` n `92`; fx avg `0.0028` n `6`; index avg `0.0069` n `25`; metal avg `-0.0033` n `20`; unknown avg `-0.1478` n `763`
- 24h: commodity avg `0.447` n `12`; crypto_alt avg `-0.878` n `230`; crypto_major avg `-0.6067` n `8`; equity avg `-0.1193` n `92`; fx avg `0.0087` n `6`; index avg `-0.1132` n `25`; metal avg `-0.0981` n `20`; unknown avg `0.0827` n `745`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.179`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1635`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1339`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1276`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1214`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1186`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1105`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1052`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1044`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1012`, n `668`, weak_sample_signal
