# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-02T01:11:48.825404+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1388` n `12`; crypto_alt avg `0.299` n `230`; crypto_major avg `0.328` n `8`; equity avg `0.0082` n `102`; fx avg `0.0072` n `6`; index avg `0.0021` n `25`; metal avg `0.0417` n `20`; unknown avg `12.3508` n `782`
- 1h: commodity avg `-0.1429` n `12`; crypto_alt avg `0.3271` n `230`; crypto_major avg `0.2391` n `8`; equity avg `0.1737` n `102`; fx avg `0.0176` n `6`; index avg `0.0129` n `25`; metal avg `0.0467` n `20`; unknown avg `12.378` n `782`
- 4h: commodity avg `-0.297` n `12`; crypto_alt avg `0.6184` n `230`; crypto_major avg `0.539` n `8`; equity avg `0.5394` n `102`; fx avg `0.0051` n `6`; index avg `0.0853` n `25`; metal avg `0.0649` n `20`; unknown avg `0.9907` n `782`
- 24h: commodity avg `-0.3029` n `12`; crypto_alt avg `-0.5281` n `230`; crypto_major avg `-0.5875` n `8`; equity avg `0.1058` n `102`; fx avg `-0.0343` n `6`; index avg `0.0597` n `25`; metal avg `0.1093` n `20`; unknown avg `-0.0323` n `765`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1221`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0979`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0921`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.092`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0799`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0784`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0776`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0714`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0687`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0673`, n `668`, weak_sample_signal
