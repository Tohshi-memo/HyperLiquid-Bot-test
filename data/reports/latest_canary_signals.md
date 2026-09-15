# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-15T04:52:30.425639+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0179` n `12`; crypto_alt avg `0.2137` n `233`; crypto_major avg `0.0759` n `8`; equity avg `0.0402` n `136`; fx avg `0.0042` n `6`; index avg `0.0059` n `27`; metal avg `0.0202` n `20`; unknown avg `-0.0417` n `908`
- 1h: commodity avg `0.0633` n `12`; crypto_alt avg `0.0042` n `233`; crypto_major avg `-0.18` n `8`; equity avg `-0.3936` n `136`; fx avg `0.0009` n `6`; index avg `-0.0965` n `27`; metal avg `-0.0172` n `20`; unknown avg `0.3069` n `898`
- 4h: commodity avg `0.092` n `12`; crypto_alt avg `-0.6122` n `233`; crypto_major avg `-0.5661` n `8`; equity avg `-0.5906` n `136`; fx avg `0.0528` n `6`; index avg `-0.1011` n `27`; metal avg `0.1397` n `20`; unknown avg `-0.1984` n `890`
- 24h: commodity avg `0.0641` n `12`; crypto_alt avg `-0.8531` n `233`; crypto_major avg `-0.0782` n `8`; equity avg `-0.49` n `136`; fx avg `0.1277` n `6`; index avg `-0.0915` n `27`; metal avg `-0.236` n `20`; unknown avg `4.9552` n `788`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.1206`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1088`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0994`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0989`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0981`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.087`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0831`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0817`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0713`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0653`, n `668`, weak_sample_signal
