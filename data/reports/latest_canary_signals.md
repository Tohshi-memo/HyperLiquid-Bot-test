# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-12T16:07:27.398018+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0052` n `12`; crypto_alt avg `-0.0066` n `230`; crypto_major avg `-0.0071` n `8`; equity avg `-0.0512` n `92`; fx avg `-0.0206` n `6`; index avg `-0.0047` n `25`; metal avg `-0.0016` n `20`; unknown avg `0.0141` n `765`
- 1h: commodity avg `0.0514` n `12`; crypto_alt avg `-0.0661` n `230`; crypto_major avg `-0.0056` n `8`; equity avg `-0.0566` n `92`; fx avg `-0.0212` n `6`; index avg `0.0141` n `25`; metal avg `-0.0018` n `20`; unknown avg `0.0182` n `765`
- 4h: commodity avg `-0.0128` n `12`; crypto_alt avg `0.1992` n `230`; crypto_major avg `0.6383` n `8`; equity avg `-0.0228` n `92`; fx avg `-0.0192` n `6`; index avg `0.0384` n `25`; metal avg `-0.0142` n `20`; unknown avg `-0.0021` n `765`
- 24h: commodity avg `0.483` n `12`; crypto_alt avg `-0.8255` n `230`; crypto_major avg `-0.2313` n `8`; equity avg `-0.0235` n `92`; fx avg `0.0231` n `6`; index avg `-0.0863` n `25`; metal avg `-0.0954` n `20`; unknown avg `0.1661` n `745`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1803`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1642`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1362`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1335`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1221`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1077`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1071`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1033`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0991`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0981`, n `668`, weak_sample_signal
