# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-25T18:22:25.845554+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0623` n `13`; crypto_alt avg `-0.0455` n `237`; crypto_major avg `-0.0195` n `8`; equity avg `0.0159` n `152`; fx avg `0.0137` n `6`; index avg `0.0036` n `26`; metal avg `-0.015` n `20`; unknown avg `-0.0021` n `1240`
- 1h: commodity avg `-0.057` n `13`; crypto_alt avg `-0.2801` n `237`; crypto_major avg `-0.2381` n `8`; equity avg `0.0444` n `152`; fx avg `0.009` n `6`; index avg `0.0062` n `26`; metal avg `-0.0047` n `20`; unknown avg `1.1641` n `1240`
- 4h: commodity avg `-0.0769` n `13`; crypto_alt avg `1.2806` n `237`; crypto_major avg `0.754` n `8`; equity avg `0.4667` n `152`; fx avg `-0.0093` n `6`; index avg `0.053` n `26`; metal avg `0.0458` n `20`; unknown avg `0.4084` n `1185`
- 24h: commodity avg `-0.3238` n `13`; crypto_alt avg `0.822` n `237`; crypto_major avg `1.2278` n `8`; equity avg `0.9249` n `152`; fx avg `0.0284` n `6`; index avg `0.1661` n `26`; metal avg `0.1626` n `20`; unknown avg `10.7686` n `1043`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.225`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1798`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1686`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1674`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1515`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1433`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1368`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1364`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1199`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1069`, n `668`, weak_sample_signal
