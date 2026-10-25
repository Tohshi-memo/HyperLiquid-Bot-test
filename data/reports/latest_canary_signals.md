# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-25T00:52:34.431223+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0044` n `13`; crypto_alt avg `-0.0152` n `237`; crypto_major avg `0.0367` n `8`; equity avg `0.0545` n `152`; fx avg `0.0019` n `6`; index avg `0.0122` n `26`; metal avg `0.0043` n `20`; unknown avg `0.2305` n `1231`
- 1h: commodity avg `-0.0121` n `13`; crypto_alt avg `0.0603` n `237`; crypto_major avg `0.1327` n `8`; equity avg `0.0856` n `152`; fx avg `-0.0022` n `6`; index avg `0.0107` n `26`; metal avg `-0.0006` n `20`; unknown avg `1.5319` n `1225`
- 4h: commodity avg `-0.0319` n `13`; crypto_alt avg `0.5486` n `237`; crypto_major avg `0.6257` n `8`; equity avg `0.168` n `152`; fx avg `0.0013` n `6`; index avg `0.0212` n `26`; metal avg `0.0168` n `20`; unknown avg `0.1707` n `1149`
- 24h: commodity avg `-0.1145` n `13`; crypto_alt avg `-0.2576` n `237`; crypto_major avg `0.1667` n `8`; equity avg `0.2156` n `152`; fx avg `-0.0305` n `6`; index avg `0.0304` n `26`; metal avg `-0.0567` n `20`; unknown avg `0.5259` n `1064`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1928`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.179`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1749`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1597`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.15`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1436`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1351`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1258`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1185`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1133`, n `668`, weak_sample_signal
