# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-12T14:07:29.031012+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0473` n `12`; crypto_alt avg `-0.0787` n `230`; crypto_major avg `-0.0376` n `8`; equity avg `-0.0054` n `92`; fx avg `0.0065` n `6`; index avg `-0.008` n `25`; metal avg `-0.0119` n `20`; unknown avg `0.0073` n `765`
- 1h: commodity avg `-0.0221` n `12`; crypto_alt avg `-0.1801` n `230`; crypto_major avg `-0.1293` n `8`; equity avg `0.0006` n `92`; fx avg `0.0077` n `6`; index avg `0.0204` n `25`; metal avg `-0.021` n `20`; unknown avg `0.0094` n `765`
- 4h: commodity avg `-0.0647` n `12`; crypto_alt avg `-0.0234` n `230`; crypto_major avg `0.4507` n `8`; equity avg `0.0709` n `92`; fx avg `0.0092` n `6`; index avg `0.0269` n `25`; metal avg `-0.018` n `20`; unknown avg `-0.0589` n `763`
- 24h: commodity avg `0.4436` n `12`; crypto_alt avg `-1.2331` n `230`; crypto_major avg `-0.6333` n `8`; equity avg `0.0159` n `92`; fx avg `0.0079` n `6`; index avg `-0.0993` n `25`; metal avg `-0.107` n `20`; unknown avg `0.0955` n `745`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1819`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1649`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.137`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1313`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1223`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1177`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.109`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1061`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1028`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1014`, n `668`, weak_sample_signal
