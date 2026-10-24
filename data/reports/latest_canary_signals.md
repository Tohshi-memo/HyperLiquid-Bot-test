# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-24T23:52:31.709783+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0096` n `13`; crypto_alt avg `-0.0187` n `237`; crypto_major avg `-0.0106` n `8`; equity avg `-0.0024` n `152`; fx avg `0.0007` n `6`; index avg `0.0002` n `26`; metal avg `0.0017` n `20`; unknown avg `0.259` n `1231`
- 1h: commodity avg `-0.0156` n `13`; crypto_alt avg `0.523` n `237`; crypto_major avg `0.4267` n `8`; equity avg `0.0894` n `152`; fx avg `0.0096` n `6`; index avg `0.0069` n `26`; metal avg `0.0207` n `20`; unknown avg `0.0241` n `1231`
- 4h: commodity avg `-0.0041` n `13`; crypto_alt avg `1.0494` n `237`; crypto_major avg `0.8115` n `8`; equity avg `0.1486` n `152`; fx avg `0.0108` n `6`; index avg `0.0164` n `26`; metal avg `0.0203` n `20`; unknown avg `0.241` n `1141`
- 24h: commodity avg `-0.0366` n `13`; crypto_alt avg `-0.5993` n `237`; crypto_major avg `-0.3995` n `8`; equity avg `0.0357` n `152`; fx avg `-0.0328` n `6`; index avg `0.0029` n `26`; metal avg `-0.0928` n `20`; unknown avg `1.2227` n `1064`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1924`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1791`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1761`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.159`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1505`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1412`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1358`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.124`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1189`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.109`, n `668`, weak_sample_signal
