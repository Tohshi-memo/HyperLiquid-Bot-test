# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-09T23:12:18.995622+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0122` n `13`; crypto_alt avg `0.1227` n `235`; crypto_major avg `-0.0667` n `8`; equity avg `0.0071` n `150`; fx avg `0.0023` n `6`; index avg `0.0019` n `26`; metal avg `0.0031` n `20`; unknown avg `0.0024` n `1114`
- 1h: commodity avg `0.003` n `13`; crypto_alt avg `0.533` n `235`; crypto_major avg `0.1591` n `8`; equity avg `0.0269` n `150`; fx avg `-0.0014` n `6`; index avg `-0.0049` n `26`; metal avg `0.0007` n `20`; unknown avg `0.1705` n `1114`
- 4h: commodity avg `-0.0421` n `13`; crypto_alt avg `0.8518` n `235`; crypto_major avg `0.1537` n `8`; equity avg `0.0501` n `150`; fx avg `-0.0105` n `6`; index avg `-0.0107` n `26`; metal avg `-0.063` n `20`; unknown avg `0.2389` n `1026`
- 24h: commodity avg `-0.1285` n `13`; crypto_alt avg `2.1062` n `235`; crypto_major avg `0.3446` n `8`; equity avg `0.7779` n `150`; fx avg `0.0064` n `6`; index avg `0.1267` n `26`; metal avg `0.5403` n `20`; unknown avg `12.8265` n `901`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1527`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1413`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1377`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1275`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1253`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1222`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1209`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.111`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1065`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1061`, n `668`, weak_sample_signal
