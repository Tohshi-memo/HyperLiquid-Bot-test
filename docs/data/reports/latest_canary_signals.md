# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-04T12:22:31.603536+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0077` n `12`; crypto_alt avg `-0.0532` n `230`; crypto_major avg `-0.0082` n `8`; equity avg `0.0357` n `107`; fx avg `0.0252` n `6`; index avg `0.0228` n `25`; metal avg `0.0542` n `20`; unknown avg `-0.0097` n `781`
- 1h: commodity avg `-0.538` n `12`; crypto_alt avg `-0.0459` n `230`; crypto_major avg `0.1092` n `8`; equity avg `0.1718` n `107`; fx avg `-0.0493` n `6`; index avg `0.0552` n `25`; metal avg `0.2568` n `20`; unknown avg `0.0206` n `781`
- 4h: commodity avg `-0.8008` n `12`; crypto_alt avg `-0.1156` n `230`; crypto_major avg `0.5229` n `8`; equity avg `0.5465` n `107`; fx avg `-0.0776` n `6`; index avg `0.1123` n `25`; metal avg `0.3236` n `20`; unknown avg `0.1714` n `781`
- 24h: commodity avg `-0.4814` n `12`; crypto_alt avg `0.8931` n `230`; crypto_major avg `1.7105` n `8`; equity avg `5.3217` n `107`; fx avg `0.0452` n `6`; index avg `0.6552` n `25`; metal avg `0.7812` n `20`; unknown avg `0.8935` n `764`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1401`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1185`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1157`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1047`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1034`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.093`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.092`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0896`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0894`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0885`, n `668`, weak_sample_signal
