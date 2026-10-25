# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-25T08:22:27.946925+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0016` n `13`; crypto_alt avg `-0.2126` n `237`; crypto_major avg `-0.047` n `8`; equity avg `-0.0406` n `152`; fx avg `-0.0007` n `6`; index avg `0.0067` n `26`; metal avg `-0.0079` n `20`; unknown avg `0.1847` n `1231`
- 1h: commodity avg `-0.0637` n `13`; crypto_alt avg `-0.1872` n `237`; crypto_major avg `-0.0905` n `8`; equity avg `-0.0611` n `152`; fx avg `-0.0047` n `6`; index avg `-0.003` n `26`; metal avg `-0.0107` n `20`; unknown avg `0.144` n `1211`
- 4h: commodity avg `0.0136` n `13`; crypto_alt avg `-1.054` n `237`; crypto_major avg `-0.7372` n `8`; equity avg `-0.2736` n `152`; fx avg `0.0077` n `6`; index avg `-0.0144` n `26`; metal avg `-0.006` n `20`; unknown avg `0.6578` n `1189`
- 24h: commodity avg `0.0428` n `13`; crypto_alt avg `-1.4627` n `237`; crypto_major avg `-0.0831` n `8`; equity avg `0.0049` n `152`; fx avg `-0.0216` n `6`; index avg `0.0121` n `26`; metal avg `-0.0704` n `20`; unknown avg `18.2686` n `1056`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.2003`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1647`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1645`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1633`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1626`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1552`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1435`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1392`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.12`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1181`, n `668`, weak_sample_signal
