# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-31T19:07:35.731554+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0172` n `12`; crypto_alt avg `-0.0833` n `230`; crypto_major avg `-0.19` n `8`; equity avg `-0.1775` n `102`; fx avg `0.011` n `6`; index avg `-0.0385` n `25`; metal avg `-0.0067` n `20`; unknown avg `0.1887` n `780`
- 1h: commodity avg `-0.0093` n `12`; crypto_alt avg `-0.3249` n `230`; crypto_major avg `-0.3235` n `8`; equity avg `-0.1978` n `102`; fx avg `0.0415` n `6`; index avg `-0.0238` n `25`; metal avg `0.0236` n `20`; unknown avg `7.605` n `780`
- 4h: commodity avg `-0.115` n `12`; crypto_alt avg `0.2707` n `230`; crypto_major avg `-0.0357` n `8`; equity avg `0.0923` n `102`; fx avg `0.1165` n `6`; index avg `0.0653` n `25`; metal avg `0.1394` n `20`; unknown avg `14.6861` n `780`
- 24h: commodity avg `0.2163` n `12`; crypto_alt avg `-0.3421` n `230`; crypto_major avg `-1.9769` n `8`; equity avg `0.3381` n `102`; fx avg `0.2603` n `6`; index avg `0.2457` n `25`; metal avg `-0.3066` n `20`; unknown avg `0.3254` n `747`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1358`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.131`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0957`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.079`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0737`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0705`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0698`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0683`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0669`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0667`, n `668`, weak_sample_signal
