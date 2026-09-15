# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-15T06:22:26.835494+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0006` n `12`; crypto_alt avg `-0.2534` n `233`; crypto_major avg `-0.283` n `8`; equity avg `0.0202` n `136`; fx avg `0.0013` n `6`; index avg `0.0038` n `27`; metal avg `0.0253` n `20`; unknown avg `1.5852` n `908`
- 1h: commodity avg `-0.0183` n `12`; crypto_alt avg `0.171` n `233`; crypto_major avg `0.2929` n `8`; equity avg `0.2722` n `136`; fx avg `0.0156` n `6`; index avg `0.0596` n `27`; metal avg `-0.0027` n `20`; unknown avg `1.3486` n `886`
- 4h: commodity avg `0.0802` n `12`; crypto_alt avg `-0.7472` n `233`; crypto_major avg `-0.7137` n `8`; equity avg `-0.5745` n `136`; fx avg `0.0269` n `6`; index avg `-0.1041` n `27`; metal avg `-0.0427` n `20`; unknown avg `2.8506` n `870`
- 24h: commodity avg `0.102` n `12`; crypto_alt avg `-1.3981` n `233`; crypto_major avg `-0.3693` n `8`; equity avg `-0.3823` n `136`; fx avg `0.1679` n `6`; index avg `-0.0913` n `27`; metal avg `-0.3138` n `20`; unknown avg `5.761` n `794`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1027`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1023`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0997`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.098`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0881`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0847`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0754`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0723`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0689`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0605`, n `668`, weak_sample_signal
