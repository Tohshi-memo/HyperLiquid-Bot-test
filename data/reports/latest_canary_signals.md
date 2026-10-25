# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-25T01:52:31.409901+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0091` n `13`; crypto_alt avg `-0.1436` n `237`; crypto_major avg `0.0852` n `8`; equity avg `0.0071` n `152`; fx avg `-0.0056` n `6`; index avg `0.0022` n `26`; metal avg `0.0024` n `20`; unknown avg `0.1986` n `1227`
- 1h: commodity avg `-0.0212` n `13`; crypto_alt avg `-0.4824` n `237`; crypto_major avg `0.0156` n `8`; equity avg `-0.0171` n `152`; fx avg `-0.004` n `6`; index avg `-0.006` n `26`; metal avg `-0.0014` n `20`; unknown avg `0.1121` n `1221`
- 4h: commodity avg `-0.0791` n `13`; crypto_alt avg `0.3064` n `237`; crypto_major avg `0.8811` n `8`; equity avg `0.2081` n `152`; fx avg `-0.0057` n `6`; index avg `0.0145` n `26`; metal avg `0.0319` n `20`; unknown avg `0.2582` n `1189`
- 24h: commodity avg `-0.0272` n `13`; crypto_alt avg `-1.2209` n `237`; crypto_major avg `-0.1865` n `8`; equity avg `0.0397` n `152`; fx avg `-0.0369` n `6`; index avg `0.0052` n `26`; metal avg `-0.0792` n `20`; unknown avg `1.2891` n `1064`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.193`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1787`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1736`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1589`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1497`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1444`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1347`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1246`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1203`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1172`, n `668`, weak_sample_signal
