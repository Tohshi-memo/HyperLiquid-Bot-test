# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-31T02:52:24.901014+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.1072` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0064` n `12`; crypto_alt avg `0.0234` n `230`; crypto_major avg `0.0302` n `8`; equity avg `0.2288` n `102`; fx avg `0.0241` n `6`; index avg `0.0509` n `25`; metal avg `-0.0462` n `20`; unknown avg `-0.1475` n `779`
- 1h: commodity avg `-0.0359` n `12`; crypto_alt avg `-0.4375` n `230`; crypto_major avg `-0.4974` n `8`; equity avg `-0.3749` n `102`; fx avg `-0.0119` n `6`; index avg `-0.0411` n `25`; metal avg `-0.0682` n `20`; unknown avg `-0.0272` n `779`
- 4h: commodity avg `-0.2399` n `12`; crypto_alt avg `-0.4344` n `230`; crypto_major avg `-0.9041` n `8`; equity avg `0.3986` n `102`; fx avg `0.1907` n `6`; index avg `0.2031` n `25`; metal avg `-0.3084` n `20`; unknown avg `0.3065` n `779`
- 24h: commodity avg `-0.1402` n `12`; crypto_alt avg `-0.3` n `230`; crypto_major avg `0.3976` n `8`; equity avg `7.3354` n `102`; fx avg `-0.1763` n `6`; index avg `0.9832` n `25`; metal avg `0.3281` n `20`; unknown avg `0.041` n `739`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1363`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1266`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0954`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0932`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.09`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0815`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0813`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0802`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0772`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0664`, n `668`, weak_sample_signal
