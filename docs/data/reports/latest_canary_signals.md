# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-21T03:22:28.874074+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0206` n `12`; crypto_alt avg `0.1031` n `230`; crypto_major avg `0.1813` n `8`; equity avg `-0.0071` n `121`; fx avg `0.0133` n `6`; index avg `-0.0012` n `25`; metal avg `-0.0021` n `20`; unknown avg `0.2469` n `793`
- 1h: commodity avg `-0.0527` n `12`; crypto_alt avg `-0.0866` n `230`; crypto_major avg `-0.4412` n `8`; equity avg `-0.1012` n `121`; fx avg `0.0162` n `6`; index avg `-0.0047` n `25`; metal avg `0.0589` n `20`; unknown avg `0.8976` n `793`
- 4h: commodity avg `0.0409` n `12`; crypto_alt avg `0.7759` n `230`; crypto_major avg `0.8423` n `8`; equity avg `0.7278` n `121`; fx avg `-0.117` n `6`; index avg `0.1277` n `25`; metal avg `0.1929` n `20`; unknown avg `0.042` n `793`
- 24h: commodity avg `0.3541` n `12`; crypto_alt avg `5.7008` n `230`; crypto_major avg `6.9115` n `8`; equity avg `-0.3777` n `121`; fx avg `-0.0203` n `6`; index avg `-0.0893` n `25`; metal avg `0.5115` n `20`; unknown avg `2.5951` n `776`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.213`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1855`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1841`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1813`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1219`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1158`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1025`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0983`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.094`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0907`, n `668`, weak_sample_signal
