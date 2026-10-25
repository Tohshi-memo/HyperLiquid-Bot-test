# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-25T03:37:23.980455+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0118` n `13`; crypto_alt avg `-0.1726` n `237`; crypto_major avg `-0.1217` n `8`; equity avg `0.0104` n `152`; fx avg `0.0106` n `6`; index avg `0.0008` n `26`; metal avg `-0.0005` n `20`; unknown avg `1.6454` n `1229`
- 1h: commodity avg `-0.0079` n `13`; crypto_alt avg `0.0122` n `237`; crypto_major avg `-0.0455` n `8`; equity avg `0.061` n `152`; fx avg `0.0108` n `6`; index avg `0.0109` n `26`; metal avg `-0.002` n `20`; unknown avg `0.7347` n `1225`
- 4h: commodity avg `-0.0174` n `13`; crypto_alt avg `-0.5317` n `237`; crypto_major avg `0.2054` n `8`; equity avg `0.1021` n `152`; fx avg `-0.003` n `6`; index avg `0.0201` n `26`; metal avg `0.0009` n `20`; unknown avg `0.0916` n `1209`
- 24h: commodity avg `0.1656` n `13`; crypto_alt avg `-1.4354` n `237`; crypto_major avg `-0.177` n `8`; equity avg `-0.0281` n `152`; fx avg `-0.0333` n `6`; index avg `-0.0034` n `26`; metal avg `-0.0774` n `20`; unknown avg `6.0309` n `1064`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1967`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1701`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1636`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1603`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1551`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1549`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1375`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1348`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1176`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1172`, n `668`, weak_sample_signal
