# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-23T10:52:27.990425+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0297` n `13`; crypto_alt avg `-0.0073` n `237`; crypto_major avg `-0.0685` n `8`; equity avg `-0.2235` n `152`; fx avg `0.0055` n `6`; index avg `-0.0394` n `26`; metal avg `0.0105` n `20`; unknown avg `0.3713` n `1233`
- 1h: commodity avg `-0.01` n `13`; crypto_alt avg `0.0959` n `237`; crypto_major avg `0.0035` n `8`; equity avg `-0.3016` n `152`; fx avg `0.0141` n `6`; index avg `-0.0335` n `26`; metal avg `0.0167` n `20`; unknown avg `-0.0844` n `1231`
- 4h: commodity avg `0.1451` n `13`; crypto_alt avg `-0.254` n `237`; crypto_major avg `-0.2712` n `8`; equity avg `-0.6321` n `152`; fx avg `-0.0738` n `6`; index avg `-0.1312` n `26`; metal avg `-0.0506` n `20`; unknown avg `0.2395` n `1151`
- 24h: commodity avg `0.3376` n `13`; crypto_alt avg `-0.0356` n `237`; crypto_major avg `0.0339` n `8`; equity avg `-1.6176` n `152`; fx avg `-0.0372` n `6`; index avg `-0.218` n `26`; metal avg `-0.4493` n `20`; unknown avg `49.6282` n `950`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.2081`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1861`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1738`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1646`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.156`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1372`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.135`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1336`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1184`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1159`, n `668`, weak_sample_signal
