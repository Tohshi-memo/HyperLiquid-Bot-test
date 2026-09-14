# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-14T08:37:30.479090+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0284` n `12`; crypto_alt avg `-0.1036` n `233`; crypto_major avg `-0.131` n `8`; equity avg `0.0694` n `136`; fx avg `0.0076` n `6`; index avg `-0.0015` n `27`; metal avg `0.0092` n `20`; unknown avg `0.5942` n `888`
- 1h: commodity avg `0.0405` n `12`; crypto_alt avg `-0.1688` n `233`; crypto_major avg `-0.0443` n `8`; equity avg `-0.2567` n `136`; fx avg `-0.0196` n `6`; index avg `-0.0343` n `27`; metal avg `-0.0807` n `20`; unknown avg `3.7328` n `886`
- 4h: commodity avg `0.1226` n `12`; crypto_alt avg `-0.1485` n `233`; crypto_major avg `0.1794` n `8`; equity avg `-0.5978` n `136`; fx avg `-0.0039` n `6`; index avg `-0.0819` n `27`; metal avg `-0.1898` n `20`; unknown avg `0.9807` n `832`
- 24h: commodity avg `0.74` n `12`; crypto_alt avg `-0.1058` n `233`; crypto_major avg `0.8946` n `8`; equity avg `-1.3881` n `136`; fx avg `0.0344` n `6`; index avg `-0.3121` n `27`; metal avg `-0.3234` n `20`; unknown avg `0.8868` n `650`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1165`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1155`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1127`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1122`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0954`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0878`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0839`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0797`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0772`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0723`, n `668`, weak_sample_signal
