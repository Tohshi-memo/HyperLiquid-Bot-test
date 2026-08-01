# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-01T10:07:28.400347+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0487` n `12`; crypto_alt avg `-0.1777` n `230`; crypto_major avg `-0.1329` n `8`; equity avg `-0.0016` n `102`; fx avg `0.0051` n `6`; index avg `-0.0241` n `25`; metal avg `-0.0236` n `20`; unknown avg `-0.0008` n `781`
- 1h: commodity avg `0.0036` n `12`; crypto_alt avg `-0.3749` n `230`; crypto_major avg `-0.2866` n `8`; equity avg `-0.0829` n `102`; fx avg `0.0079` n `6`; index avg `0.0086` n `25`; metal avg `-0.028` n `20`; unknown avg `-0.0056` n `781`
- 4h: commodity avg `0.0399` n `12`; crypto_alt avg `-0.3995` n `230`; crypto_major avg `-0.2316` n `8`; equity avg `0.0569` n `102`; fx avg `0.0104` n `6`; index avg `0.0319` n `25`; metal avg `-0.0076` n `20`; unknown avg `-0.0663` n `781`
- 24h: commodity avg `0.5453` n `12`; crypto_alt avg `0.2043` n `230`; crypto_major avg `-1.1418` n `8`; equity avg `-2.5876` n `102`; fx avg `-0.0486` n `6`; index avg `-0.2499` n `25`; metal avg `-0.0534` n `20`; unknown avg `4.7748` n `764`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1076`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1046`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1039`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0877`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0767`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0732`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0682`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0677`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0654`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0647`, n `668`, weak_sample_signal
