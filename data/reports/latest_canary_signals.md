# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-15T06:07:28.479429+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0728` n `12`; crypto_alt avg `0.0425` n `233`; crypto_major avg `0.1649` n `8`; equity avg `-0.0992` n `136`; fx avg `0.0206` n `6`; index avg `-0.0247` n `27`; metal avg `-0.0846` n `20`; unknown avg `0.8646` n `886`
- 1h: commodity avg `-0.0106` n `12`; crypto_alt avg `0.0032` n `233`; crypto_major avg `0.2331` n `8`; equity avg `0.0702` n `136`; fx avg `0.0472` n `6`; index avg `0.0201` n `27`; metal avg `-0.0553` n `20`; unknown avg `6.4939` n `886`
- 4h: commodity avg `0.0578` n `12`; crypto_alt avg `-0.4204` n `233`; crypto_major avg `-0.381` n `8`; equity avg `-0.5693` n `136`; fx avg `0.0636` n `6`; index avg `-0.1062` n `27`; metal avg `-0.0574` n `20`; unknown avg `5.8336` n `870`
- 24h: commodity avg `0.1051` n `12`; crypto_alt avg `-1.2579` n `233`; crypto_major avg `-0.286` n `8`; equity avg `-0.451` n `136`; fx avg `0.1813` n `6`; index avg `-0.0984` n `27`; metal avg `-0.3574` n `20`; unknown avg `5.0236` n `794`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.1041`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1013`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0992`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0986`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0835`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0816`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0777`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0732`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0671`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0525`, n `668`, weak_sample_signal
