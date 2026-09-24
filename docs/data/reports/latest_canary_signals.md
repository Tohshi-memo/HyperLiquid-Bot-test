# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-24T05:37:27.432957+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0712` n `12`; crypto_alt avg `-0.103` n `234`; crypto_major avg `-0.11` n `8`; equity avg `0.0434` n `141`; fx avg `0.0123` n `6`; index avg `0.0035` n `26`; metal avg `0.0065` n `20`; unknown avg `-0.1522` n `945`
- 1h: commodity avg `0.1079` n `12`; crypto_alt avg `0.7752` n `234`; crypto_major avg `0.5891` n `8`; equity avg `0.1482` n `141`; fx avg `-0.0109` n `6`; index avg `0.002` n `26`; metal avg `0.0127` n `20`; unknown avg `6.2954` n `943`
- 4h: commodity avg `0.1093` n `12`; crypto_alt avg `1.4311` n `234`; crypto_major avg `0.1632` n `8`; equity avg `-0.2211` n `141`; fx avg `0.011` n `6`; index avg `-0.0507` n `26`; metal avg `0.0327` n `20`; unknown avg `1.9507` n `937`
- 24h: commodity avg `0.5782` n `12`; crypto_alt avg `-3.9618` n `234`; crypto_major avg `-3.9473` n `8`; equity avg `-1.7124` n `140`; fx avg `0.0688` n `6`; index avg `-0.3551` n `26`; metal avg `-0.5567` n `20`; unknown avg `585.0013` n `821`

## Correlations

- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1711`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.15`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1463`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1445`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1367`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1367`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1275`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1204`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1162`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1081`, n `668`, weak_sample_signal
