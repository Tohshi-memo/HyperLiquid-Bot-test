# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-08T17:52:29.034919+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0636` n `12`; crypto_alt avg `-0.2797` n `229`; crypto_major avg `-0.3` n `8`; equity avg `-0.1559` n `91`; fx avg `0.0041` n `6`; index avg `-0.0571` n `25`; metal avg `-0.0213` n `20`; unknown avg `-0.0293` n `764`
- 1h: commodity avg `-0.2342` n `12`; crypto_alt avg `0.1994` n `229`; crypto_major avg `0.2247` n `8`; equity avg `0.1559` n `91`; fx avg `0.0184` n `6`; index avg `0.0422` n `25`; metal avg `0.0872` n `20`; unknown avg `0.0578` n `764`
- 4h: commodity avg `-0.1081` n `12`; crypto_alt avg `0.3775` n `229`; crypto_major avg `0.3842` n `8`; equity avg `0.0946` n `91`; fx avg `0.0425` n `6`; index avg `0.1129` n `25`; metal avg `-0.0846` n `20`; unknown avg `0.0242` n `764`
- 24h: commodity avg `0.6338` n `12`; crypto_alt avg `-3.253` n `229`; crypto_major avg `-3.7494` n `8`; equity avg `-0.2881` n `91`; fx avg `0.0213` n `6`; index avg `-0.2164` n `25`; metal avg `-1.2428` n `20`; unknown avg `-0.536` n `737`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1434`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1052`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0903`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0736`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0692`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0685`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0649`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0577`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0508`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0475`, n `668`, weak_sample_signal
