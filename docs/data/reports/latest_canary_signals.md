# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-13T16:07:28.645470+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0111` n `12`; crypto_alt avg `0.078` n `233`; crypto_major avg `0.1783` n `8`; equity avg `0.0937` n `136`; fx avg `0.0006` n `6`; index avg `0.0448` n `27`; metal avg `0.0218` n `20`; unknown avg `0.1218` n `836`
- 1h: commodity avg `0.0036` n `12`; crypto_alt avg `-0.1194` n `233`; crypto_major avg `0.1247` n `8`; equity avg `0.0351` n `136`; fx avg `0.0071` n `6`; index avg `0.0085` n `27`; metal avg `-0.0013` n `20`; unknown avg `73.6026` n `836`
- 4h: commodity avg `-0.0013` n `12`; crypto_alt avg `0.4146` n `233`; crypto_major avg `0.5306` n `8`; equity avg `0.1935` n `136`; fx avg `0.0092` n `6`; index avg `0.0473` n `27`; metal avg `0.0059` n `20`; unknown avg `2.6719` n `830`
- 24h: commodity avg `0.2999` n `12`; crypto_alt avg `-0.6498` n `233`; crypto_major avg `-1.3518` n `8`; equity avg `-1.6384` n `136`; fx avg `0.0132` n `6`; index avg `-0.2584` n `26`; metal avg `-0.089` n `20`; unknown avg `1.9928` n `708`

## Correlations

- market_context_score -> index_forward_1h_return_pct: corr `-0.0862`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.085`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0822`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0726`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0721`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0647`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0647`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0643`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0623`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0588`, n `668`, weak_sample_signal
