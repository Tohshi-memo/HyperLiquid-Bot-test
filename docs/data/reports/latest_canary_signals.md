# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-10T21:07:35.445187+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.1` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0087` n `12`; crypto_alt avg `0.1683` n `229`; crypto_major avg `0.0907` n `8`; equity avg `-0.0019` n `92`; fx avg `0.0086` n `6`; index avg `-0.0021` n `25`; metal avg `0.022` n `20`; unknown avg `-0.2061` n `765`
- 1h: commodity avg `0.0332` n `12`; crypto_alt avg `0.0507` n `229`; crypto_major avg `0.0457` n `8`; equity avg `0.047` n `92`; fx avg `0.0009` n `6`; index avg `0.015` n `25`; metal avg `0.0595` n `20`; unknown avg `-0.2422` n `765`
- 4h: commodity avg `0.1577` n `12`; crypto_alt avg `-0.1491` n `229`; crypto_major avg `-0.2344` n `8`; equity avg `-0.1304` n `92`; fx avg `-0.041` n `6`; index avg `0.0473` n `25`; metal avg `0.1275` n `20`; unknown avg `-0.3814` n `765`
- 24h: commodity avg `-0.2604` n `12`; crypto_alt avg `0.5453` n `229`; crypto_major avg `0.614` n `8`; equity avg `-0.6842` n `92`; fx avg `-0.1741` n `6`; index avg `0.0415` n `25`; metal avg `0.1881` n `20`; unknown avg `-0.263` n `732`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.1252`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1115`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1042`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1006`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0994`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0956`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.093`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0878`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0789`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0776`, n `668`, weak_sample_signal
