# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-13T11:52:30.198267+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0174` n `12`; crypto_alt avg `0.0561` n `233`; crypto_major avg `0.0643` n `8`; equity avg `0.0156` n `136`; fx avg `0.0036` n `6`; index avg `-0.0134` n `27`; metal avg `-0.0046` n `20`; unknown avg `0.1666` n `838`
- 1h: commodity avg `0.1219` n `12`; crypto_alt avg `0.2368` n `233`; crypto_major avg `0.2347` n `8`; equity avg `0.0198` n `136`; fx avg `0.002` n `6`; index avg `-0.0003` n `27`; metal avg `-0.0055` n `20`; unknown avg `0.068` n `836`
- 4h: commodity avg `0.1433` n `12`; crypto_alt avg `-0.6744` n `233`; crypto_major avg `-0.8825` n `8`; equity avg `-0.8006` n `136`; fx avg `0.014` n `6`; index avg `-0.1357` n `27`; metal avg `-0.0658` n `20`; unknown avg `0.6177` n `830`
- 24h: commodity avg `0.2364` n `12`; crypto_alt avg `-0.6424` n `233`; crypto_major avg `-1.9134` n `8`; equity avg `-1.7694` n `136`; fx avg `0.0099` n `6`; index avg `-0.283` n `26`; metal avg `-0.084` n `20`; unknown avg `-0.2729` n `708`

## Correlations

- market_context_score -> index_forward_1h_return_pct: corr `-0.0914`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0871`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0772`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0764`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0725`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0656`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0647`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0611`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0591`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0586`, n `668`, weak_sample_signal
