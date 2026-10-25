# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-25T15:22:31.966626+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0114` n `13`; crypto_alt avg `-0.1048` n `237`; crypto_major avg `-0.1849` n `8`; equity avg `-0.0043` n `152`; fx avg `-0.0103` n `6`; index avg `-0.0027` n `26`; metal avg `-0.0064` n `20`; unknown avg `-0.0358` n `1240`
- 1h: commodity avg `-0.0148` n `13`; crypto_alt avg `0.6109` n `237`; crypto_major avg `0.3771` n `8`; equity avg `0.1597` n `152`; fx avg `-0.0174` n `6`; index avg `0.0152` n `26`; metal avg `-0.0011` n `20`; unknown avg `0.0888` n `1231`
- 4h: commodity avg `-0.1144` n `13`; crypto_alt avg `0.5645` n `237`; crypto_major avg `0.261` n `8`; equity avg `0.304` n `152`; fx avg `-0.0089` n `6`; index avg `0.0619` n `26`; metal avg `0.0583` n `20`; unknown avg `0.2057` n `1225`
- 24h: commodity avg `-0.1582` n `13`; crypto_alt avg `1.0959` n `237`; crypto_major avg `1.949` n `8`; equity avg `0.7507` n `152`; fx avg `0.0067` n `6`; index avg `0.1375` n `26`; metal avg `0.1339` n `20`; unknown avg `10.0926` n `1080`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.2232`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1785`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.17`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.169`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1572`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1435`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1413`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1377`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1148`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1136`, n `668`, weak_sample_signal
