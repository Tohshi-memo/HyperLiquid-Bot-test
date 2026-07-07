# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-07T04:13:46.004957+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0101` n `12`; crypto_alt avg `0.0692` n `229`; crypto_major avg `-0.0646` n `8`; equity avg `-0.0087` n `91`; fx avg `-0.0101` n `6`; index avg `0.0265` n `25`; metal avg `0.1131` n `20`; unknown avg `-0.0305` n `763`
- 1h: commodity avg `-0.0442` n `12`; crypto_alt avg `-0.3789` n `229`; crypto_major avg `-0.4995` n `8`; equity avg `-0.5748` n `91`; fx avg `-0.0293` n `6`; index avg `-0.1233` n `25`; metal avg `-0.0667` n `20`; unknown avg `-0.1552` n `763`
- 4h: commodity avg `-0.0523` n `12`; crypto_alt avg `-1.2254` n `229`; crypto_major avg `-1.2742` n `8`; equity avg `-1.3682` n `91`; fx avg `-0.1159` n `6`; index avg `-0.3439` n `25`; metal avg `-0.2379` n `20`; unknown avg `0.8964` n `761`
- 24h: commodity avg `0.2622` n `12`; crypto_alt avg `-0.3232` n `229`; crypto_major avg `-0.9897` n `8`; equity avg `-1.4252` n `90`; fx avg `-0.0411` n `6`; index avg `-0.2302` n `25`; metal avg `-0.2108` n `20`; unknown avg `-0.4647` n `727`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1196`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1114`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0889`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0834`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.081`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0686`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0572`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.053`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0523`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0521`, n `668`, weak_sample_signal
