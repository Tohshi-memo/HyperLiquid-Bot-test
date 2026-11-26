# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-26T23:52:24.199772+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0057` n `13`; crypto_alt avg `0.1728` n `239`; crypto_major avg `0.1194` n `8`; equity avg `-0.0276` n `168`; fx avg `-0.0025` n `6`; index avg `-0.0018` n `27`; metal avg `0.0169` n `20`; unknown avg `1.1917` n `1263`
- 1h: commodity avg `0.0146` n `13`; crypto_alt avg `-0.2991` n `239`; crypto_major avg `-0.3156` n `8`; equity avg `-0.2266` n `168`; fx avg `0.0139` n `6`; index avg `-0.002` n `27`; metal avg `-0.0432` n `20`; unknown avg `54.0066` n `1223`
- 4h: commodity avg `0.03` n `13`; crypto_alt avg `-0.3918` n `239`; crypto_major avg `-0.5082` n `8`; equity avg `-0.1999` n `168`; fx avg `0.0199` n `6`; index avg `-0.0032` n `27`; metal avg `-0.0335` n `20`; unknown avg `239.5498` n `1143`
- 24h: commodity avg `0.1335` n `13`; crypto_alt avg `1.0496` n `239`; crypto_major avg `0.38` n `8`; equity avg `0.4419` n `168`; fx avg `0.0037` n `6`; index avg `0.043` n `27`; metal avg `-0.0519` n `20`; unknown avg `210.8831` n `993`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1156`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.11`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1044`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.102`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.099`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0971`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.087`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0848`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0846`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0814`, n `668`, weak_sample_signal
