# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-25T00:07:25.014786+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0207` n `13`; crypto_alt avg `-0.0702` n `237`; crypto_major avg `-0.0333` n `8`; equity avg `-0.0037` n `152`; fx avg `-0.0061` n `6`; index avg `-0.0022` n `26`; metal avg `-0.0025` n `20`; unknown avg `0.4884` n `1223`
- 1h: commodity avg `-0.0185` n `13`; crypto_alt avg `0.5012` n `237`; crypto_major avg `0.4353` n `8`; equity avg `0.0856` n `152`; fx avg `0.0019` n `6`; index avg `-0.0026` n `26`; metal avg `0.0115` n `20`; unknown avg `0.2573` n `1225`
- 4h: commodity avg `-0.0427` n `13`; crypto_alt avg `0.6277` n `237`; crypto_major avg `0.5399` n `8`; equity avg `0.0894` n `152`; fx avg `-0.0079` n `6`; index avg `0.0077` n `26`; metal avg `0.0097` n `20`; unknown avg `0.144` n `1151`
- 24h: commodity avg `-0.0941` n `13`; crypto_alt avg `-0.6709` n `237`; crypto_major avg `-0.4139` n `8`; equity avg `-0.0754` n `152`; fx avg `-0.0416` n `6`; index avg `-0.0206` n `26`; metal avg `-0.0893` n `20`; unknown avg `0.4778` n `1064`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1924`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1791`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1757`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1592`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1502`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1417`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1355`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1246`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1187`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1093`, n `668`, weak_sample_signal
