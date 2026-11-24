# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-24T19:07:29.317716+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0851` n `13`; crypto_alt avg `-0.1147` n `239`; crypto_major avg `-0.0696` n `8`; equity avg `-0.0742` n `168`; fx avg `0.0064` n `6`; index avg `-0.0028` n `27`; metal avg `0.0305` n `20`; unknown avg `161.5804` n `1255`
- 1h: commodity avg `0.0841` n `13`; crypto_alt avg `-0.3599` n `239`; crypto_major avg `-0.3293` n `8`; equity avg `-0.032` n `168`; fx avg `-0.0082` n `6`; index avg `-0.01` n `27`; metal avg `-0.0431` n `20`; unknown avg `343.8766` n `1243`
- 4h: commodity avg `0.1113` n `13`; crypto_alt avg `-0.0539` n `239`; crypto_major avg `0.0643` n `8`; equity avg `-0.5093` n `168`; fx avg `0.0141` n `6`; index avg `-0.0064` n `27`; metal avg `-0.47` n `20`; unknown avg `346.3872` n `1227`
- 24h: commodity avg `0.6169` n `13`; crypto_alt avg `-3.8163` n `239`; crypto_major avg `-3.5889` n `8`; equity avg `-4.0851` n `167`; fx avg `0.2553` n `6`; index avg `-0.2686` n `27`; metal avg `-1.1854` n `20`; unknown avg `381.4309` n `1115`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1307`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1296`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1274`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1173`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1048`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1043`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0946`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0935`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0877`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.079`, n `668`, weak_sample_signal
