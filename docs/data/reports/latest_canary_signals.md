# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-07T05:22:31.027958+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `-1.5358` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `1.4359` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0362` n `12`; crypto_alt avg `-0.2148` n `229`; crypto_major avg `-0.2001` n `8`; equity avg `0.1218` n `91`; fx avg `0.0013` n `6`; index avg `0.0085` n `25`; metal avg `-0.0616` n `20`; unknown avg `0.4123` n `763`
- 1h: commodity avg `0.0191` n `12`; crypto_alt avg `-0.4409` n `229`; crypto_major avg `-0.3397` n `8`; equity avg `-0.1167` n `91`; fx avg `0.0241` n `6`; index avg `-0.0461` n `25`; metal avg `-0.1398` n `20`; unknown avg `23.5571` n `763`
- 4h: commodity avg `0.0403` n `12`; crypto_alt avg `-1.3677` n `229`; crypto_major avg `-1.6867` n `8`; equity avg `-0.958` n `91`; fx avg `-0.0744` n `6`; index avg `-0.2508` n `25`; metal avg `-0.1509` n `20`; unknown avg `16.1159` n `761`
- 24h: commodity avg `0.234` n `12`; crypto_alt avg `-0.2985` n `229`; crypto_major avg `-1.2016` n `8`; equity avg `-1.8873` n `90`; fx avg `0.0023` n `6`; index avg `-0.3996` n `25`; metal avg `-0.3799` n `20`; unknown avg `-0.5787` n `727`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1115`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1066`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0881`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0773`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.077`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0749`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0613`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0486`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0469`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0457`, n `668`, weak_sample_signal
