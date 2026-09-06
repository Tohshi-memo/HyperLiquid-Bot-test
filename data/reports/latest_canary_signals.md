# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-06T01:07:24.445327+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0111` n `12`; crypto_alt avg `0.173` n `232`; crypto_major avg `0.1222` n `8`; equity avg `0.0475` n `134`; fx avg `-0.022` n `6`; index avg `0.005` n `26`; metal avg `-0.0048` n `20`; unknown avg `-0.2587` n `792`
- 1h: commodity avg `0.0837` n `12`; crypto_alt avg `0.7506` n `232`; crypto_major avg `0.3433` n `8`; equity avg `0.0427` n `134`; fx avg `-0.0207` n `6`; index avg `0.0013` n `26`; metal avg `-0.0016` n `20`; unknown avg `6.1155` n `786`
- 4h: commodity avg `0.0465` n `12`; crypto_alt avg `1.0882` n `232`; crypto_major avg `0.1634` n `8`; equity avg `0.1429` n `134`; fx avg `-0.028` n `6`; index avg `0.0157` n `26`; metal avg `-0.0091` n `20`; unknown avg `0.273` n `786`
- 24h: commodity avg `0.1622` n `12`; crypto_alt avg `3.4576` n `232`; crypto_major avg `2.5534` n `8`; equity avg `0.4185` n `134`; fx avg `-0.0975` n `6`; index avg `0.0695` n `26`; metal avg `0.042` n `20`; unknown avg `0.3102` n `694`

## Correlations

- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1636`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1542`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1342`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1209`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1079`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0967`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0957`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.095`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0891`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.087`, n `668`, weak_sample_signal
