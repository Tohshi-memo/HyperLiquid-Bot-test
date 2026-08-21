# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-21T12:00:57.497807+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 1h_index_leads_crypto: score `1.4138` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0261` n `12`; crypto_alt avg `-0.0534` n `230`; crypto_major avg `-0.2365` n `8`; equity avg `-0.0513` n `121`; fx avg `0.0108` n `6`; index avg `-0.0129` n `23`; metal avg `0.0154` n `18`; unknown avg `-0.0273` n `774`
- 1h: commodity avg `-0.0944` n `12`; crypto_alt avg `-0.176` n `230`; crypto_major avg `-1.3908` n `8`; equity avg `0.0367` n `121`; fx avg `-0.0122` n `6`; index avg `0.023` n `25`; metal avg `0.0563` n `20`; unknown avg `0.1905` n `793`
- 4h: commodity avg `-0.0001` n `12`; crypto_alt avg `1.3262` n `230`; crypto_major avg `-0.0122` n `8`; equity avg `0.1873` n `121`; fx avg `0.0204` n `6`; index avg `0.0038` n `25`; metal avg `0.1619` n `20`; unknown avg `0.5656` n `793`
- 24h: commodity avg `0.0379` n `12`; crypto_alt avg `7.2831` n `230`; crypto_major avg `5.7721` n `8`; equity avg `1.5677` n `121`; fx avg `-0.0985` n `6`; index avg `0.2313` n `25`; metal avg `1.2042` n `20`; unknown avg `2.4095` n `776`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.2263`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1997`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1917`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1904`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1191`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1123`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.109`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0978`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.09`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0866`, n `668`, weak_sample_signal
