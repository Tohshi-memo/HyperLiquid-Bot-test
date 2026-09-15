# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-15T13:52:33.415536+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0313` n `12`; crypto_alt avg `-0.3007` n `233`; crypto_major avg `-0.3364` n `8`; equity avg `-0.065` n `136`; fx avg `-0.0122` n `6`; index avg `0.0005` n `27`; metal avg `0.0176` n `20`; unknown avg `0.1333` n `890`
- 1h: commodity avg `0.2501` n `12`; crypto_alt avg `-0.8065` n `233`; crypto_major avg `-0.887` n `8`; equity avg `-0.2048` n `136`; fx avg `0.0198` n `6`; index avg `-0.0626` n `27`; metal avg `0.0424` n `20`; unknown avg `3.6456` n `888`
- 4h: commodity avg `-0.0032` n `12`; crypto_alt avg `-0.685` n `233`; crypto_major avg `-0.6007` n `8`; equity avg `0.1883` n `136`; fx avg `-0.0086` n `6`; index avg `0.0503` n `27`; metal avg `0.2951` n `20`; unknown avg `6.2337` n `882`
- 24h: commodity avg `-0.0439` n `12`; crypto_alt avg `-1.5398` n `233`; crypto_major avg `-1.3804` n `8`; equity avg `0.2621` n `136`; fx avg `0.1656` n `6`; index avg `0.0335` n `27`; metal avg `0.2467` n `20`; unknown avg `0.7253` n `814`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.1209`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1015`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1001`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0974`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0921`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0896`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0883`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0853`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.077`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.069`, n `668`, weak_sample_signal
