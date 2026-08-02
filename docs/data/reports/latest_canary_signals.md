# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-02T20:52:29.699690+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0137` n `12`; crypto_alt avg `0.0675` n `230`; crypto_major avg `0.0814` n `8`; equity avg `-0.025` n `102`; fx avg `0.0157` n `6`; index avg `-0.0121` n `25`; metal avg `0.0098` n `20`; unknown avg `0.0307` n `783`
- 1h: commodity avg `0.0665` n `12`; crypto_alt avg `-0.0432` n `230`; crypto_major avg `-0.0904` n `8`; equity avg `0.0422` n `102`; fx avg `0.0291` n `6`; index avg `-0.0005` n `25`; metal avg `0.0339` n `20`; unknown avg `-0.0705` n `783`
- 4h: commodity avg `0.0341` n `12`; crypto_alt avg `0.1378` n `230`; crypto_major avg `0.4046` n `8`; equity avg `0.3178` n `102`; fx avg `0.1034` n `6`; index avg `0.0223` n `25`; metal avg `0.0899` n `20`; unknown avg `0.1206` n `782`
- 24h: commodity avg `-1.2413` n `12`; crypto_alt avg `1.5574` n `230`; crypto_major avg `1.9832` n `8`; equity avg `1.7743` n `102`; fx avg `-0.0361` n `6`; index avg `0.3389` n `25`; metal avg `0.4058` n `20`; unknown avg `1.6415` n `766`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.135`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1241`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.118`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0873`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0823`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0812`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0789`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0716`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0683`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0671`, n `668`, weak_sample_signal
