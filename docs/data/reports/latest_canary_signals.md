# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-01T00:22:25.960705+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.005` n `12`; crypto_alt avg `0.0977` n `230`; crypto_major avg `-0.0066` n `8`; equity avg `-0.1394` n `102`; fx avg `-0.0061` n `6`; index avg `-0.014` n `25`; metal avg `-0.0054` n `20`; unknown avg `0.0184` n `781`
- 1h: commodity avg `-0.0263` n `12`; crypto_alt avg `0.297` n `230`; crypto_major avg `-0.0304` n `8`; equity avg `0.0799` n `102`; fx avg `-0.0184` n `6`; index avg `0.014` n `25`; metal avg `-0.0365` n `20`; unknown avg `4.9654` n `781`
- 4h: commodity avg `0.621` n `12`; crypto_alt avg `0.0936` n `230`; crypto_major avg `-0.148` n `8`; equity avg `-0.2782` n `102`; fx avg `-0.0612` n `6`; index avg `-0.0539` n `25`; metal avg `-0.0576` n `20`; unknown avg `4.8318` n `780`
- 24h: commodity avg `0.7427` n `12`; crypto_alt avg `-0.2792` n `230`; crypto_major avg `-2.158` n `8`; equity avg `-2.1222` n `102`; fx avg `-0.0454` n `6`; index avg `-0.1745` n `25`; metal avg `-0.4402` n `20`; unknown avg `2.6603` n `747`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1029`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0995`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0934`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0839`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0746`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0708`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.07`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0666`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0662`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0648`, n `668`, weak_sample_signal
