# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-01T04:22:25.291382+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0282` n `12`; crypto_alt avg `0.0052` n `230`; crypto_major avg `0.0642` n `8`; equity avg `0.034` n `102`; fx avg `-0.0332` n `6`; index avg `0.0364` n `25`; metal avg `0.0029` n `20`; unknown avg `-0.0455` n `781`
- 1h: commodity avg `-0.0728` n `12`; crypto_alt avg `0.134` n `230`; crypto_major avg `0.0964` n `8`; equity avg `-0.0053` n `102`; fx avg `-0.032` n `6`; index avg `0.0201` n `25`; metal avg `-0.0076` n `20`; unknown avg `0.6655` n `781`
- 4h: commodity avg `-0.1746` n `12`; crypto_alt avg `0.3953` n `230`; crypto_major avg `0.2392` n `8`; equity avg `0.003` n `102`; fx avg `-0.005` n `6`; index avg `0.0348` n `25`; metal avg `0.0012` n `20`; unknown avg `0.2341` n `781`
- 24h: commodity avg `0.9024` n `12`; crypto_alt avg `0.5185` n `230`; crypto_major avg `-1.234` n `8`; equity avg `-2.3143` n `102`; fx avg `-0.1741` n `6`; index avg `-0.1945` n `25`; metal avg `-0.2083` n `20`; unknown avg `4.8425` n `747`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1028`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1016`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0994`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0858`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0746`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0732`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0701`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0685`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0668`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0648`, n `668`, weak_sample_signal
