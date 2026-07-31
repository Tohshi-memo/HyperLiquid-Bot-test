# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-31T23:22:27.698277+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0161` n `12`; crypto_alt avg `0.0356` n `230`; crypto_major avg `0.0128` n `8`; equity avg `-0.0346` n `102`; fx avg `-0.0027` n `6`; index avg `-0.0003` n `25`; metal avg `0.004` n `20`; unknown avg `-0.0121` n `781`
- 1h: commodity avg `0.0771` n `12`; crypto_alt avg `-0.0099` n `230`; crypto_major avg `-0.0298` n `8`; equity avg `0.0492` n `102`; fx avg `-0.0335` n `6`; index avg `-0.0016` n `25`; metal avg `0.0091` n `20`; unknown avg `0.1903` n `781`
- 4h: commodity avg `0.6285` n `12`; crypto_alt avg `-0.1521` n `230`; crypto_major avg `-0.1897` n `8`; equity avg `-1.0108` n `102`; fx avg `-0.114` n `6`; index avg `-0.1672` n `25`; metal avg `-0.0778` n `20`; unknown avg `2.0526` n `780`
- 24h: commodity avg `0.8214` n `12`; crypto_alt avg `-0.6995` n `230`; crypto_major avg `-2.3946` n `8`; equity avg `-1.6169` n `102`; fx avg `0.0797` n `6`; index avg `0.0349` n `25`; metal avg `-0.4035` n `20`; unknown avg `2.5436` n `747`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1059`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1032`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0911`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0838`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0765`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.072`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0715`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0663`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0662`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0651`, n `668`, weak_sample_signal
