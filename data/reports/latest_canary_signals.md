# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-23T07:07:26.245595+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.0278` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0049` n `12`; crypto_alt avg `0.3347` n `230`; crypto_major avg `0.304` n `8`; equity avg `0.0139` n `121`; fx avg `0.0625` n `6`; index avg `-0.0025` n `25`; metal avg `0.0095` n `20`; unknown avg `0.0477` n `794`
- 1h: commodity avg `0.0145` n `12`; crypto_alt avg `1.0202` n `230`; crypto_major avg `0.6687` n `8`; equity avg `0.0556` n `121`; fx avg `0.0273` n `6`; index avg `-0.011` n `25`; metal avg `0.0129` n `20`; unknown avg `0.2371` n `794`
- 4h: commodity avg `-0.0019` n `12`; crypto_alt avg `-0.6182` n `230`; crypto_major avg `-1.0609` n `8`; equity avg `-0.2157` n `121`; fx avg `0.0079` n `6`; index avg `-0.0331` n `25`; metal avg `-0.0237` n `20`; unknown avg `0.2478` n `778`
- 24h: commodity avg `-0.0218` n `12`; crypto_alt avg `-4.591` n `230`; crypto_major avg `-3.0379` n `8`; equity avg `-0.183` n `121`; fx avg `0.1158` n `6`; index avg `-0.0396` n `25`; metal avg `0.068` n `20`; unknown avg `2.1931` n `778`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1564`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1321`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1312`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1287`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1134`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1018`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0945`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0894`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0886`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.087`, n `668`, weak_sample_signal
