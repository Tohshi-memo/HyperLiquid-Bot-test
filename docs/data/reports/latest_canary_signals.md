# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-04T07:07:28.150531+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0619` n `12`; crypto_alt avg `-0.0545` n `230`; crypto_major avg `0.0523` n `8`; equity avg `0.0853` n `107`; fx avg `-0.0415` n `6`; index avg `0.0141` n `25`; metal avg `0.055` n `20`; unknown avg `0.0005` n `781`
- 1h: commodity avg `-0.1176` n `12`; crypto_alt avg `-0.4048` n `230`; crypto_major avg `-0.2047` n `8`; equity avg `0.1006` n `107`; fx avg `0.0039` n `6`; index avg `0.0124` n `25`; metal avg `0.0124` n `20`; unknown avg `-0.0227` n `781`
- 4h: commodity avg `-0.1355` n `12`; crypto_alt avg `-0.481` n `230`; crypto_major avg `-0.2044` n `8`; equity avg `0.941` n `107`; fx avg `0.0435` n `6`; index avg `0.1537` n `25`; metal avg `0.1148` n `20`; unknown avg `-0.0489` n `765`
- 24h: commodity avg `0.2345` n `12`; crypto_alt avg `1.029` n `230`; crypto_major avg `1.2921` n `8`; equity avg `2.6721` n `107`; fx avg `0.0459` n `6`; index avg `0.2666` n `25`; metal avg `0.1604` n `20`; unknown avg `0.176` n `763`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1434`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.119`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1102`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1024`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0996`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0877`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0855`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0848`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.084`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.084`, n `668`, weak_sample_signal
