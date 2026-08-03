# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-03T07:07:32.629313+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0974` n `12`; crypto_alt avg `-0.1202` n `230`; crypto_major avg `-0.1186` n `8`; equity avg `-0.0063` n `102`; fx avg `-0.0161` n `6`; index avg `0.0118` n `25`; metal avg `-0.0836` n `20`; unknown avg `-0.0216` n `784`
- 1h: commodity avg `-0.0661` n `12`; crypto_alt avg `-0.4045` n `230`; crypto_major avg `-0.422` n `8`; equity avg `-0.1748` n `102`; fx avg `0.0663` n `6`; index avg `0.0066` n `25`; metal avg `-0.1059` n `20`; unknown avg `-0.0072` n `784`
- 4h: commodity avg `-0.0984` n `12`; crypto_alt avg `-0.3542` n `230`; crypto_major avg `-0.4894` n `8`; equity avg `-0.2963` n `102`; fx avg `0.0189` n `6`; index avg `-0.0214` n `25`; metal avg `-0.0633` n `20`; unknown avg `0.003` n `768`
- 24h: commodity avg `-0.258` n `12`; crypto_alt avg `-1.1032` n `230`; crypto_major avg `-0.8443` n `8`; equity avg `0.6287` n `102`; fx avg `-0.1838` n `6`; index avg `-0.0131` n `25`; metal avg `-0.1267` n `20`; unknown avg `0.9447` n `766`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1194`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1042`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0818`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0783`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0741`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0726`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0693`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0678`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0606`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0593`, n `668`, weak_sample_signal
