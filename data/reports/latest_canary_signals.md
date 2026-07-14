# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-14T04:37:24.331775+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0406` n `12`; crypto_alt avg `0.1043` n `230`; crypto_major avg `0.1536` n `8`; equity avg `0.2454` n `92`; fx avg `0.0021` n `6`; index avg `0.0865` n `25`; metal avg `0.0605` n `20`; unknown avg `0.1612` n `766`
- 1h: commodity avg `-0.0329` n `12`; crypto_alt avg `0.3853` n `230`; crypto_major avg `0.3411` n `8`; equity avg `0.5374` n `92`; fx avg `0.0028` n `6`; index avg `0.1541` n `25`; metal avg `0.0929` n `20`; unknown avg `-0.0906` n `766`
- 4h: commodity avg `-0.0997` n `12`; crypto_alt avg `0.0826` n `230`; crypto_major avg `0.2172` n `8`; equity avg `-0.2879` n `92`; fx avg `-0.0861` n `6`; index avg `-0.0057` n `25`; metal avg `0.2065` n `20`; unknown avg `-0.4823` n `766`
- 24h: commodity avg `1.0177` n `12`; crypto_alt avg `-0.1707` n `230`; crypto_major avg `-0.4776` n `8`; equity avg `-1.0273` n `92`; fx avg `-0.2247` n `6`; index avg `-0.1533` n `25`; metal avg `0.1003` n `20`; unknown avg `-0.2765` n `750`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1932`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1844`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.119`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.118`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1176`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1108`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1073`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1044`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0825`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0731`, n `668`, weak_sample_signal
