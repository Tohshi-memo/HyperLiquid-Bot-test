# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-12T17:22:31.074836+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0026` n `12`; crypto_alt avg `-0.0271` n `230`; crypto_major avg `-0.0518` n `8`; equity avg `0.0097` n `92`; fx avg `-0.0007` n `6`; index avg `-0.0033` n `25`; metal avg `-0.0055` n `20`; unknown avg `-0.0561` n `765`
- 1h: commodity avg `0.0823` n `12`; crypto_alt avg `-0.1253` n `230`; crypto_major avg `-0.0802` n `8`; equity avg `0.0496` n `92`; fx avg `0.0056` n `6`; index avg `-0.0054` n `25`; metal avg `-0.0049` n `20`; unknown avg `-0.1181` n `759`
- 4h: commodity avg `0.1052` n `12`; crypto_alt avg `0.0035` n `230`; crypto_major avg `0.2982` n `8`; equity avg `-0.0274` n `92`; fx avg `0.002` n `6`; index avg `0.053` n `25`; metal avg `-0.0332` n `20`; unknown avg `-0.0659` n `759`
- 24h: commodity avg `0.5708` n `12`; crypto_alt avg `-1.1282` n `230`; crypto_major avg `-0.3951` n `8`; equity avg `-0.1201` n `92`; fx avg `0.0165` n `6`; index avg `-0.085` n `25`; metal avg `-0.1079` n `20`; unknown avg `0.1728` n `741`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1791`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1626`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1322`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1305`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1219`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1068`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1035`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1035`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.101`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0965`, n `668`, weak_sample_signal
