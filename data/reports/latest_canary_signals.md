# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-14T08:52:29.211265+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0025` n `12`; crypto_alt avg `-0.0731` n `233`; crypto_major avg `-0.0901` n `8`; equity avg `-0.0572` n `136`; fx avg `0.0031` n `6`; index avg `-0.0129` n `27`; metal avg `-0.0521` n `20`; unknown avg `0.081` n `894`
- 1h: commodity avg `0.001` n `12`; crypto_alt avg `-0.1347` n `233`; crypto_major avg `-0.144` n `8`; equity avg `-0.2139` n `136`; fx avg `-0.0038` n `6`; index avg `-0.0149` n `27`; metal avg `-0.0898` n `20`; unknown avg `6.427` n `886`
- 4h: commodity avg `0.1471` n `12`; crypto_alt avg `-0.2288` n `233`; crypto_major avg `0.0478` n `8`; equity avg `-0.6943` n `136`; fx avg `0.0147` n `6`; index avg `-0.0976` n `27`; metal avg `-0.2282` n `20`; unknown avg `0.1718` n `832`
- 24h: commodity avg `0.7374` n `12`; crypto_alt avg `-0.1759` n `233`; crypto_major avg `0.8036` n `8`; equity avg `-1.443` n `136`; fx avg `0.0375` n `6`; index avg `-0.3249` n `27`; metal avg `-0.3749` n `20`; unknown avg `0.8341` n `650`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1156`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1156`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1123`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1121`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0956`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0878`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0845`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0773`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0733`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0725`, n `668`, weak_sample_signal
