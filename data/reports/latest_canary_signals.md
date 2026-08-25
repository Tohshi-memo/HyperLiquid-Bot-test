# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-25T20:08:18.807676+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.171` n `12`; crypto_alt avg `-0.2463` n `231`; crypto_major avg `-0.2032` n `8`; equity avg `0.0615` n `122`; fx avg `0.0106` n `6`; index avg `0.0283` n `25`; metal avg `-0.0155` n `20`; unknown avg `-0.0318` n `795`
- 1h: commodity avg `-0.291` n `12`; crypto_alt avg `-0.7299` n `231`; crypto_major avg `-0.5732` n `8`; equity avg `0.0706` n `122`; fx avg `-0.0043` n `6`; index avg `0.0379` n `25`; metal avg `0.0422` n `20`; unknown avg `-0.1126` n `795`
- 4h: commodity avg `-0.1743` n `12`; crypto_alt avg `-0.9595` n `231`; crypto_major avg `-0.6416` n `8`; equity avg `0.0151` n `122`; fx avg `-0.0007` n `6`; index avg `0.0298` n `25`; metal avg `0.0936` n `20`; unknown avg `-0.3551` n `795`
- 24h: commodity avg `-0.7563` n `12`; crypto_alt avg `-1.0392` n `231`; crypto_major avg `0.3251` n `8`; equity avg `2.1099` n `122`; fx avg `0.05` n `6`; index avg `0.2599` n `25`; metal avg `0.0201` n `20`; unknown avg `-0.5259` n `778`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1448`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1193`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1134`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.106`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1016`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0951`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0856`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0836`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0801`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0797`, n `668`, weak_sample_signal
