# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-25T18:37:28.943425+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0325` n `13`; crypto_alt avg `0.0503` n `237`; crypto_major avg `-0.003` n `8`; equity avg `-0.0121` n `152`; fx avg `-0.0137` n `6`; index avg `0.0002` n `26`; metal avg `0.004` n `20`; unknown avg `0.6507` n `1240`
- 1h: commodity avg `-0.0325` n `13`; crypto_alt avg `-0.044` n `237`; crypto_major avg `-0.0559` n `8`; equity avg `0.0455` n `152`; fx avg `-0.0091` n `6`; index avg `0.0119` n `26`; metal avg `-0.0037` n `20`; unknown avg `0.1007` n `1240`
- 4h: commodity avg `-0.0351` n `13`; crypto_alt avg `1.316` n `237`; crypto_major avg `0.7064` n `8`; equity avg `0.4266` n `152`; fx avg `-0.0191` n `6`; index avg `0.0547` n `26`; metal avg `0.0471` n `20`; unknown avg `0.2116` n `1185`
- 24h: commodity avg `-0.1848` n `13`; crypto_alt avg `0.7212` n `237`; crypto_major avg `1.1116` n `8`; equity avg `0.8657` n `152`; fx avg `0.0078` n `6`; index avg `0.157` n `26`; metal avg `0.1649` n `20`; unknown avg `11.1517` n `1043`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.2249`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1796`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1683`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1669`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.151`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1428`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.136`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1358`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1197`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1068`, n `668`, weak_sample_signal
