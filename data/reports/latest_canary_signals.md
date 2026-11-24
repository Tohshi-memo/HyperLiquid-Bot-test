# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-24T19:22:36.316025+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0209` n `13`; crypto_alt avg `0.103` n `239`; crypto_major avg `-0.0135` n `8`; equity avg `0.174` n `168`; fx avg `-0.0116` n `6`; index avg `0.0221` n `27`; metal avg `-0.0005` n `20`; unknown avg `175.0628` n `1263`
- 1h: commodity avg `0.0316` n `13`; crypto_alt avg `-0.0997` n `239`; crypto_major avg `-0.3071` n `8`; equity avg `0.114` n `168`; fx avg `-0.0118` n `6`; index avg `0.0071` n `27`; metal avg `0.0055` n `20`; unknown avg `383.8854` n `1245`
- 4h: commodity avg `0.2144` n `13`; crypto_alt avg `0.4217` n `239`; crypto_major avg `0.3816` n `8`; equity avg `0.2903` n `168`; fx avg `0.0204` n `6`; index avg `0.0745` n `27`; metal avg `-0.3129` n `20`; unknown avg `367.6721` n `1227`
- 24h: commodity avg `0.7446` n `13`; crypto_alt avg `-3.3962` n `239`; crypto_major avg `-3.3625` n `8`; equity avg `-3.9182` n `167`; fx avg `0.2589` n `6`; index avg `-0.2464` n `27`; metal avg `-1.1654` n `20`; unknown avg `422.1742` n `1115`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1307`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1295`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1274`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1167`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1048`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1037`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0942`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0926`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.086`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0783`, n `668`, weak_sample_signal
