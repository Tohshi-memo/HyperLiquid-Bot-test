# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-29T23:52:23.768994+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.006` n `12`; crypto_alt avg `0.0746` n `231`; crypto_major avg `0.0709` n `8`; equity avg `-0.0002` n `128`; fx avg `0.0055` n `6`; index avg `-0.0126` n `26`; metal avg `0.0054` n `20`; unknown avg `0.0121` n `793`
- 1h: commodity avg `-0.0144` n `12`; crypto_alt avg `0.0825` n `231`; crypto_major avg `0.118` n `8`; equity avg `0.0162` n `128`; fx avg `0.0113` n `6`; index avg `-0.0231` n `26`; metal avg `0.0081` n `20`; unknown avg `-0.0209` n `793`
- 4h: commodity avg `-0.0102` n `12`; crypto_alt avg `0.0649` n `231`; crypto_major avg `0.1141` n `8`; equity avg `0.0822` n `128`; fx avg `0.0164` n `6`; index avg `0.0065` n `26`; metal avg `0.0123` n `20`; unknown avg `-0.0922` n `774`
- 24h: commodity avg `-0.0073` n `12`; crypto_alt avg `0.3515` n `231`; crypto_major avg `0.9208` n `8`; equity avg `0.4342` n `128`; fx avg `-0.007` n `6`; index avg `0.0858` n `26`; metal avg `0.1156` n `20`; unknown avg `0.1836` n `728`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.2149`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1324`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1151`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0852`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0835`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0762`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0626`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0577`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0556`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0555`, n `668`, weak_sample_signal
