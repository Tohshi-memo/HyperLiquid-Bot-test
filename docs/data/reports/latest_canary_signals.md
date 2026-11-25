# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-25T12:52:33.649470+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1007` n `13`; crypto_alt avg `-0.1702` n `239`; crypto_major avg `-0.1242` n `8`; equity avg `-0.1976` n `168`; fx avg `-0.0078` n `6`; index avg `-0.0211` n `27`; metal avg `-0.1026` n `20`; unknown avg `158.1146` n `1265`
- 1h: commodity avg `0.1193` n `13`; crypto_alt avg `-0.2021` n `239`; crypto_major avg `-0.0316` n `8`; equity avg `-0.3159` n `168`; fx avg `0.0262` n `6`; index avg `-0.0177` n `27`; metal avg `0.0954` n `20`; unknown avg `221.1651` n `1255`
- 4h: commodity avg `0.1966` n `13`; crypto_alt avg `-1.3665` n `239`; crypto_major avg `-0.8247` n `8`; equity avg `-1.4498` n `168`; fx avg `-0.0068` n `6`; index avg `-0.2229` n `27`; metal avg `-0.1307` n `20`; unknown avg `263.0036` n `1189`
- 24h: commodity avg `0.3847` n `13`; crypto_alt avg `-2.3261` n `239`; crypto_major avg `-3.1926` n `8`; equity avg `-5.2184` n `168`; fx avg `-0.0205` n `6`; index avg `-0.4582` n `27`; metal avg `-1.1903` n `20`; unknown avg `685.9793` n `1067`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1381`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1301`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1249`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1092`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1066`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0906`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0887`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0878`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0752`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0709`, n `668`, weak_sample_signal
