# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-23T10:07:32.113149+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0081` n `13`; crypto_alt avg `0.0627` n `237`; crypto_major avg `0.0493` n `8`; equity avg `-0.0697` n `152`; fx avg `0.003` n `6`; index avg `-0.0007` n `26`; metal avg `-0.0012` n `20`; unknown avg `0.1166` n `1231`
- 1h: commodity avg `0.1385` n `13`; crypto_alt avg `-0.2776` n `237`; crypto_major avg `-0.2337` n `8`; equity avg `-0.5151` n `152`; fx avg `-0.008` n `6`; index avg `-0.0719` n `26`; metal avg `-0.0664` n `20`; unknown avg `0.873` n `1219`
- 4h: commodity avg `0.0965` n `13`; crypto_alt avg `-0.1131` n `237`; crypto_major avg `0.0432` n `8`; equity avg `0.0473` n `152`; fx avg `-0.0682` n `6`; index avg `-0.0554` n `26`; metal avg `-0.0943` n `20`; unknown avg `0.6357` n `1151`
- 24h: commodity avg `0.4086` n `13`; crypto_alt avg `-0.2451` n `237`; crypto_major avg `0.0711` n `8`; equity avg `-1.1773` n `152`; fx avg `-0.0358` n `6`; index avg `-0.1574` n `26`; metal avg `-0.4694` n `20`; unknown avg `49.6904` n `950`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.2031`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1841`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1716`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1634`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1514`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1397`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1329`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1293`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1201`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1178`, n `668`, weak_sample_signal
