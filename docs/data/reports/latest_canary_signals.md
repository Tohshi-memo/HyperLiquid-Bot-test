# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-26T17:37:31.304267+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0153` n `12`; crypto_alt avg `0.0162` n `234`; crypto_major avg `-0.0494` n `8`; equity avg `0.0057` n `141`; fx avg `0.0063` n `6`; index avg `0.0` n `26`; metal avg `-0.001` n `20`; unknown avg `3.5948` n `961`
- 1h: commodity avg `0.0122` n `12`; crypto_alt avg `-0.543` n `234`; crypto_major avg `-0.3161` n `8`; equity avg `-0.0327` n `141`; fx avg `-0.0011` n `6`; index avg `0.0012` n `26`; metal avg `0.0014` n `20`; unknown avg `15.3572` n `959`
- 4h: commodity avg `0.0055` n `12`; crypto_alt avg `0.9277` n `234`; crypto_major avg `0.2154` n `8`; equity avg `0.0939` n `141`; fx avg `-0.0057` n `6`; index avg `0.0225` n `26`; metal avg `-0.0013` n `20`; unknown avg `22.385` n `945`
- 24h: commodity avg `0.3389` n `12`; crypto_alt avg `2.9921` n `234`; crypto_major avg `0.198` n `8`; equity avg `-0.0195` n `141`; fx avg `0.011` n `6`; index avg `0.0083` n `26`; metal avg `0.0197` n `20`; unknown avg `5.0811` n `814`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1762`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1573`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1513`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1504`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1289`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1287`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1199`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0998`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0899`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0849`, n `668`, weak_sample_signal
