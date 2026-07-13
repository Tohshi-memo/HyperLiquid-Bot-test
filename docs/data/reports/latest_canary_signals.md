# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-13T10:22:30.501529+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0323` n `12`; crypto_alt avg `0.0523` n `230`; crypto_major avg `-0.0353` n `8`; equity avg `-0.0008` n `92`; fx avg `-0.0127` n `6`; index avg `-0.003` n `25`; metal avg `-0.036` n `20`; unknown avg `-0.0111` n `766`
- 1h: commodity avg `0.1644` n `12`; crypto_alt avg `0.0835` n `230`; crypto_major avg `-0.1635` n `8`; equity avg `-0.0175` n `92`; fx avg `-0.052` n `6`; index avg `-0.0166` n `25`; metal avg `-0.0771` n `20`; unknown avg `-0.0417` n `766`
- 4h: commodity avg `-0.2406` n `12`; crypto_alt avg `0.3917` n `230`; crypto_major avg `0.1368` n `8`; equity avg `0.5682` n `92`; fx avg `-0.1157` n `6`; index avg `0.1625` n `25`; metal avg `0.2435` n `20`; unknown avg `0.0456` n `766`
- 24h: commodity avg `-0.2282` n `12`; crypto_alt avg `-1.0199` n `230`; crypto_major avg `-1.1574` n `8`; equity avg `-1.9781` n `92`; fx avg `-0.0832` n `6`; index avg `-0.4184` n `25`; metal avg `-0.2154` n `20`; unknown avg `-0.093` n `743`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1928`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1755`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1372`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1275`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1205`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1125`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.102`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1009`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0927`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0873`, n `668`, weak_sample_signal
