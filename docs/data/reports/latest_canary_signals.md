# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-01T19:37:23.219026+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.1304` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.086` n `12`; crypto_alt avg `0.0732` n `230`; crypto_major avg `-0.0221` n `8`; equity avg `-0.0595` n `102`; fx avg `0.0034` n `6`; index avg `-0.0092` n `25`; metal avg `-0.0049` n `20`; unknown avg `0.1125` n `782`
- 1h: commodity avg `0.1328` n `12`; crypto_alt avg `-0.0365` n `230`; crypto_major avg `-0.1749` n `8`; equity avg `-0.0699` n `102`; fx avg `0.0071` n `6`; index avg `0.0046` n `25`; metal avg `0.0395` n `20`; unknown avg `0.2873` n `782`
- 4h: commodity avg `0.2016` n `12`; crypto_alt avg `-1.0281` n `230`; crypto_major avg `-1.1803` n `8`; equity avg `-0.3316` n `102`; fx avg `-0.007` n `6`; index avg `-0.0499` n `25`; metal avg `0.0063` n `20`; unknown avg `2.1848` n `782`
- 24h: commodity avg `0.6595` n `12`; crypto_alt avg `-0.7691` n `230`; crypto_major avg `-1.4107` n `8`; equity avg `-1.1646` n `102`; fx avg `-0.1648` n `6`; index avg `-0.1301` n `25`; metal avg `-0.0545` n `20`; unknown avg `4.2798` n `764`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.112`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1015`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0824`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0802`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0791`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0712`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0689`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0669`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0668`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0664`, n `668`, weak_sample_signal
