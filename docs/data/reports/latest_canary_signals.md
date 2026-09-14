# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-14T23:07:36.359255+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0016` n `12`; crypto_alt avg `-0.1418` n `233`; crypto_major avg `-0.162` n `8`; equity avg `0.0519` n `136`; fx avg `-0.007` n `6`; index avg `-0.0028` n `27`; metal avg `-0.0185` n `20`; unknown avg `0.3264` n `908`
- 1h: commodity avg `0.0036` n `12`; crypto_alt avg `-0.3704` n `233`; crypto_major avg `-0.4993` n `8`; equity avg `0.0526` n `136`; fx avg `-0.0219` n `6`; index avg `-0.0012` n `27`; metal avg `-0.0224` n `20`; unknown avg `0.4318` n `898`
- 4h: commodity avg `0.1617` n `12`; crypto_alt avg `-0.8382` n `233`; crypto_major avg `-0.9363` n `8`; equity avg `-0.2237` n `136`; fx avg `-0.0016` n `6`; index avg `-0.0643` n `27`; metal avg `-0.0949` n `20`; unknown avg `0.091` n `866`
- 24h: commodity avg `-0.0824` n `12`; crypto_alt avg `1.4367` n `233`; crypto_major avg `2.5012` n `8`; equity avg `-0.23` n `136`; fx avg `0.0069` n `6`; index avg `-0.1604` n `27`; metal avg `-0.3735` n `20`; unknown avg `1.936` n `676`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `0.1011`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0988`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0964`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0961`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0945`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0742`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0703`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0701`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0617`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0591`, n `668`, weak_sample_signal
