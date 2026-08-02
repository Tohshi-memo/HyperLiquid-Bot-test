# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-02T15:37:24.762415+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0102` n `12`; crypto_alt avg `0.0338` n `230`; crypto_major avg `0.0285` n `8`; equity avg `-0.0213` n `102`; fx avg `0.0048` n `6`; index avg `-0.0055` n `25`; metal avg `0.0018` n `20`; unknown avg `-0.0587` n `782`
- 1h: commodity avg `0.0036` n `12`; crypto_alt avg `0.0127` n `230`; crypto_major avg `0.0458` n `8`; equity avg `0.0255` n `102`; fx avg `0.007` n `6`; index avg `-0.0088` n `25`; metal avg `0.0258` n `20`; unknown avg `1.0675` n `782`
- 4h: commodity avg `-0.0637` n `12`; crypto_alt avg `0.1092` n `230`; crypto_major avg `0.1244` n `8`; equity avg `0.0796` n `102`; fx avg `-0.0348` n `6`; index avg `0.0289` n `25`; metal avg `0.03` n `20`; unknown avg `1.1061` n `782`
- 24h: commodity avg `-1.0939` n `12`; crypto_alt avg `0.3853` n `230`; crypto_major avg `0.2516` n `8`; equity avg `0.926` n `102`; fx avg `-0.143` n `6`; index avg `0.2009` n `25`; metal avg `0.2501` n `20`; unknown avg `1.4526` n `766`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.124`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1235`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1081`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0917`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0838`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0816`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0812`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0744`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0723`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0719`, n `668`, weak_sample_signal
