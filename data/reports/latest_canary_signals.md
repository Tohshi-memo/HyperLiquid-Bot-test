# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-22T07:37:27.096444+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.3594` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0013` n `12`; crypto_alt avg `0.3146` n `230`; crypto_major avg `0.4978` n `8`; equity avg `0.0066` n `121`; fx avg `-0.0012` n `6`; index avg `-0.0005` n `25`; metal avg `0.0207` n `20`; unknown avg `0.0465` n `794`
- 1h: commodity avg `-0.004` n `12`; crypto_alt avg `0.9219` n `230`; crypto_major avg `0.7493` n `8`; equity avg `0.0761` n `121`; fx avg `-0.0086` n `6`; index avg `0.0039` n `25`; metal avg `0.0417` n `20`; unknown avg `0.75` n `794`
- 4h: commodity avg `0.0759` n `12`; crypto_alt avg `-3.0042` n `230`; crypto_major avg `-1.4081` n `8`; equity avg `-0.3845` n `121`; fx avg `0.0023` n `6`; index avg `-0.0487` n `25`; metal avg `-0.096` n `20`; unknown avg `0.5148` n `778`
- 24h: commodity avg `0.0844` n `12`; crypto_alt avg `6.2133` n `230`; crypto_major avg `7.2964` n `8`; equity avg `-0.6014` n `121`; fx avg `0.0365` n `6`; index avg `-0.1106` n `25`; metal avg `0.0046` n `20`; unknown avg `1.8473` n `777`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `0.1549`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.151`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1464`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1405`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1402`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1376`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1357`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1259`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1221`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0969`, n `668`, weak_sample_signal
