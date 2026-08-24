# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-24T08:02:24.282802+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0094` n `12`; crypto_alt avg `-0.2501` n `231`; crypto_major avg `-0.3897` n `8`; equity avg `-0.1181` n `122`; fx avg `0.0044` n `6`; index avg `-0.0298` n `25`; metal avg `0.0213` n `20`; unknown avg `-0.0329` n `793`
- 1h: commodity avg `0.1496` n `12`; crypto_alt avg `-0.2589` n `231`; crypto_major avg `-0.6553` n `8`; equity avg `-0.2172` n `122`; fx avg `-0.0046` n `6`; index avg `-0.0349` n `25`; metal avg `-0.0647` n `20`; unknown avg `-0.0317` n `793`
- 4h: commodity avg `0.0909` n `12`; crypto_alt avg `-0.0221` n `231`; crypto_major avg `-0.1208` n `8`; equity avg `-0.3993` n `122`; fx avg `0.0274` n `6`; index avg `-0.0767` n `25`; metal avg `0.0441` n `20`; unknown avg `-0.0447` n `777`
- 24h: commodity avg `-0.2238` n `12`; crypto_alt avg `2.3972` n `231`; crypto_major avg `0.7051` n `8`; equity avg `-1.486` n `122`; fx avg `-0.1269` n `6`; index avg `-0.1637` n `25`; metal avg `0.146` n `20`; unknown avg `5.1541` n `776`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1186`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1076`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1002`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0907`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0895`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0881`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0831`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0642`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0627`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0548`, n `668`, weak_sample_signal
