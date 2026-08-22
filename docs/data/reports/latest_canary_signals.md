# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-22T21:37:23.451840+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 1h_index_leads_crypto: score `1.1969` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.006` n `12`; crypto_alt avg `-0.7688` n `230`; crypto_major avg `-0.5641` n `8`; equity avg `-0.0194` n `121`; fx avg `-0.0127` n `6`; index avg `-0.0024` n `25`; metal avg `0.0166` n `20`; unknown avg `-0.1805` n `794`
- 1h: commodity avg `0.0298` n `12`; crypto_alt avg `-1.4841` n `230`; crypto_major avg `-1.2028` n `8`; equity avg `-0.0494` n `121`; fx avg `0.0046` n `6`; index avg `-0.0059` n `25`; metal avg `0.0227` n `20`; unknown avg `-0.1218` n `794`
- 4h: commodity avg `0.0917` n `12`; crypto_alt avg `-1.5259` n `230`; crypto_major avg `-0.2904` n `8`; equity avg `0.0886` n `121`; fx avg `0.038` n `6`; index avg `-0.0066` n `25`; metal avg `0.0196` n `20`; unknown avg `1.1304` n `794`
- 24h: commodity avg `0.0682` n `12`; crypto_alt avg `-1.8691` n `230`; crypto_major avg `0.868` n `8`; equity avg `-0.4187` n `121`; fx avg `0.0684` n `6`; index avg `-0.0501` n `25`; metal avg `-0.0682` n `20`; unknown avg `3.0137` n `777`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1461`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.135`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1289`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1244`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1241`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.121`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1157`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1133`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.107`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1016`, n `668`, weak_sample_signal
