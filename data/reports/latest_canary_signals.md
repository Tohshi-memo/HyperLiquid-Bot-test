# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-21T21:07:30.860133+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0116` n `12`; crypto_alt avg `0.143` n `230`; crypto_major avg `0.1645` n `8`; equity avg `-0.0085` n `121`; fx avg `0.004` n `6`; index avg `0.0` n `25`; metal avg `0.0244` n `20`; unknown avg `0.0376` n `793`
- 1h: commodity avg `0.0285` n `12`; crypto_alt avg `0.8202` n `230`; crypto_major avg `0.831` n `8`; equity avg `0.0328` n `121`; fx avg `-0.0049` n `6`; index avg `-0.0066` n `25`; metal avg `-0.0486` n `20`; unknown avg `-0.1067` n `793`
- 4h: commodity avg `-0.0739` n `12`; crypto_alt avg `-0.1228` n `230`; crypto_major avg `-0.086` n `8`; equity avg `-0.0606` n `121`; fx avg `0.0029` n `6`; index avg `-0.0535` n `25`; metal avg `-0.119` n `20`; unknown avg `-0.3909` n `793`
- 24h: commodity avg `0.1261` n `12`; crypto_alt avg `7.4641` n `230`; crypto_major avg `5.1556` n `8`; equity avg `0.9518` n `121`; fx avg `-0.1003` n `6`; index avg `0.093` n `25`; metal avg `0.53` n `20`; unknown avg `1.135` n `777`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.215`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1878`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1872`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1784`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1085`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1082`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1075`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0957`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.09`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0863`, n `668`, weak_sample_signal
