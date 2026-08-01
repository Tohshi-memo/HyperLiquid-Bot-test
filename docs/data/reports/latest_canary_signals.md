# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-01T04:52:33.376540+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0053` n `12`; crypto_alt avg `0.0255` n `230`; crypto_major avg `0.0812` n `8`; equity avg `0.0222` n `102`; fx avg `0.0035` n `6`; index avg `0.007` n `25`; metal avg `-0.0098` n `20`; unknown avg `0.038` n `781`
- 1h: commodity avg `-0.0492` n `12`; crypto_alt avg `0.1539` n `230`; crypto_major avg `0.1692` n `8`; equity avg `0.05` n `102`; fx avg `-0.0023` n `6`; index avg `0.0423` n `25`; metal avg `-0.0238` n `20`; unknown avg `0.4163` n `781`
- 4h: commodity avg `-0.0816` n `12`; crypto_alt avg `0.1801` n `230`; crypto_major avg `0.1557` n `8`; equity avg `0.0302` n `102`; fx avg `0.0178` n `6`; index avg `0.0603` n `25`; metal avg `-0.0234` n `20`; unknown avg `0.2439` n `781`
- 24h: commodity avg `0.9853` n `12`; crypto_alt avg `0.5973` n `230`; crypto_major avg `-1.2801` n `8`; equity avg `-2.5772` n `102`; fx avg `-0.1455` n `6`; index avg `-0.2648` n `25`; metal avg `-0.2704` n `20`; unknown avg `4.822` n `747`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1042`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1031`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1009`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.086`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0746`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0743`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.07`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0692`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0678`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0648`, n `668`, weak_sample_signal
