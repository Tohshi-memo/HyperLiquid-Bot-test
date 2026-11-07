# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-07T04:37:26.468429+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.022` n `13`; crypto_alt avg `0.1384` n `239`; crypto_major avg `0.039` n `8`; equity avg `0.0784` n `158`; fx avg `-0.0076` n `6`; index avg `0.0092` n `27`; metal avg `0.0062` n `20`; unknown avg `0.0396` n `1257`
- 1h: commodity avg `-0.0264` n `13`; crypto_alt avg `0.2993` n `239`; crypto_major avg `0.0795` n `8`; equity avg `0.0711` n `158`; fx avg `0.008` n `6`; index avg `0.0117` n `27`; metal avg `0.0072` n `20`; unknown avg `-0.1036` n `1243`
- 4h: commodity avg `-0.136` n `13`; crypto_alt avg `-0.2659` n `239`; crypto_major avg `-0.2349` n `8`; equity avg `0.1419` n `158`; fx avg `0.0063` n `6`; index avg `0.0209` n `27`; metal avg `0.017` n `20`; unknown avg `1.2362` n `1237`
- 24h: commodity avg `-0.294` n `13`; crypto_alt avg `0.2599` n `239`; crypto_major avg `-0.0619` n `8`; equity avg `1.1346` n `158`; fx avg `-0.0439` n `6`; index avg `0.1474` n `27`; metal avg `0.2424` n `20`; unknown avg `8.387` n `1010`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2127`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.165`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1583`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1373`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.115`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1144`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.11`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1089`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1016`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0994`, n `668`, weak_sample_signal
