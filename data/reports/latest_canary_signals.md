# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-09T22:22:31.237239+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0946` n `13`; crypto_alt avg `0.0683` n `235`; crypto_major avg `0.0878` n `8`; equity avg `0.0088` n `150`; fx avg `-0.0037` n `6`; index avg `-0.0176` n `26`; metal avg `-0.0057` n `20`; unknown avg `0.0363` n `1116`
- 1h: commodity avg `-0.1042` n `13`; crypto_alt avg `-0.0149` n `235`; crypto_major avg `-0.0097` n `8`; equity avg `-0.008` n `150`; fx avg `-0.0052` n `6`; index avg `-0.0194` n `26`; metal avg `-0.0198` n `20`; unknown avg `-0.1674` n `1106`
- 4h: commodity avg `-0.3362` n `13`; crypto_alt avg `0.15` n `235`; crypto_major avg `-0.0188` n `8`; equity avg `-0.0146` n `150`; fx avg `-0.0063` n `6`; index avg `-0.011` n `26`; metal avg `-0.038` n `20`; unknown avg `0.1361` n `1026`
- 24h: commodity avg `-0.3034` n `13`; crypto_alt avg `1.6737` n `235`; crypto_major avg `0.2906` n `8`; equity avg `0.7141` n `150`; fx avg `0.0082` n `6`; index avg `0.1042` n `26`; metal avg `0.5529` n `20`; unknown avg `12.7059` n `901`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.153`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1435`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1359`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1292`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1285`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1223`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.122`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1103`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1061`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.106`, n `668`, weak_sample_signal
