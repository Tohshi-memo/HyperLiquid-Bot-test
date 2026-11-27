# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-27T02:58:55.782987+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0264` n `13`; crypto_alt avg `-0.2969` n `239`; crypto_major avg `-0.3384` n `8`; equity avg `-0.0269` n `168`; fx avg `0.0377` n `6`; index avg `0.003` n `27`; metal avg `-0.0501` n `20`; unknown avg `1.8927` n `1253`
- 1h: commodity avg `0.0744` n `13`; crypto_alt avg `1.0474` n `239`; crypto_major avg `1.369` n `8`; equity avg `1.2912` n `168`; fx avg `0.0355` n `6`; index avg `0.1112` n `27`; metal avg `0.5393` n `20`; unknown avg `-0.0121` n `1245`
- 4h: commodity avg `0.1697` n `13`; crypto_alt avg `1.0949` n `239`; crypto_major avg `1.5078` n `8`; equity avg `2.0639` n `168`; fx avg `0.0178` n `6`; index avg `0.2203` n `27`; metal avg `0.85` n `20`; unknown avg `0.0361` n `1211`
- 24h: commodity avg `0.324` n `13`; crypto_alt avg `1.3708` n `239`; crypto_major avg `1.4156` n `8`; equity avg `1.9146` n `168`; fx avg `0.0644` n `6`; index avg `0.1969` n `27`; metal avg `0.5958` n `20`; unknown avg `181.7106` n `993`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1114`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1108`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1055`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1038`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0951`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0933`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0896`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0841`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0797`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0788`, n `668`, weak_sample_signal
