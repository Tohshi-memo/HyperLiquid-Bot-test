# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-27T15:37:33.531866+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0314` n `13`; crypto_alt avg `-0.0611` n `238`; crypto_major avg `-0.0817` n `8`; equity avg `0.0905` n `154`; fx avg `-0.0012` n `6`; index avg `0.0133` n `27`; metal avg `-0.0128` n `20`; unknown avg `4.0318` n `1238`
- 1h: commodity avg `0.0286` n `13`; crypto_alt avg `0.4182` n `238`; crypto_major avg `0.3189` n `8`; equity avg `0.5092` n `154`; fx avg `-0.0154` n `6`; index avg `0.1168` n `27`; metal avg `0.0736` n `20`; unknown avg `5.8985` n `1202`
- 4h: commodity avg `-0.1831` n `13`; crypto_alt avg `1.1383` n `238`; crypto_major avg `1.1193` n `8`; equity avg `1.3081` n `154`; fx avg `0.0011` n `6`; index avg `0.1875` n `27`; metal avg `0.3745` n `20`; unknown avg `0.05` n `1150`
- 24h: commodity avg `-0.4951` n `13`; crypto_alt avg `-0.5789` n `237`; crypto_major avg `0.0993` n `8`; equity avg `0.8073` n `154`; fx avg `-0.0738` n `6`; index avg `0.3101` n `27`; metal avg `0.0478` n `20`; unknown avg `18.4114` n `1044`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.2265`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.2005`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1986`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1567`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1168`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1139`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1139`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.109`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1084`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0902`, n `668`, weak_sample_signal
