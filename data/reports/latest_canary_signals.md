# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-25T10:22:32.940708+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0008` n `13`; crypto_alt avg `-0.0767` n `237`; crypto_major avg `0.0151` n `8`; equity avg `0.0076` n `152`; fx avg `-0.0125` n `6`; index avg `-0.0042` n `26`; metal avg `0.0073` n `20`; unknown avg `-0.0084` n `1231`
- 1h: commodity avg `-0.0166` n `13`; crypto_alt avg `0.3183` n `237`; crypto_major avg `0.2279` n `8`; equity avg `0.1129` n `152`; fx avg `-0.0137` n `6`; index avg `0.0212` n `26`; metal avg `0.0187` n `20`; unknown avg `29.8958` n `1203`
- 4h: commodity avg `-0.0441` n `13`; crypto_alt avg `-0.8647` n `237`; crypto_major avg `-0.6452` n `8`; equity avg `-0.1871` n `152`; fx avg `0.0083` n `6`; index avg `-0.0125` n `26`; metal avg `0.0108` n `20`; unknown avg `30.7847` n `1183`
- 24h: commodity avg `-0.0059` n `13`; crypto_alt avg `-1.6578` n `237`; crypto_major avg `-0.0693` n `8`; equity avg `0.0031` n `152`; fx avg `-0.025` n `6`; index avg `0.0271` n `26`; metal avg `-0.0563` n `20`; unknown avg `33.2647` n `1052`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1966`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1615`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1606`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1562`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1434`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1414`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1323`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1244`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1177`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1169`, n `668`, weak_sample_signal
