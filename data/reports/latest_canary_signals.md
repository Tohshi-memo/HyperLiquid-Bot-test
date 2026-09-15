# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-15T11:22:33.381858+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0058` n `12`; crypto_alt avg `-0.2174` n `233`; crypto_major avg `-0.1746` n `8`; equity avg `0.031` n `136`; fx avg `0.0133` n `6`; index avg `0.0167` n `27`; metal avg `0.0503` n `20`; unknown avg `0.2644` n `908`
- 1h: commodity avg `-0.1446` n `12`; crypto_alt avg `-0.092` n `233`; crypto_major avg `0.0049` n `8`; equity avg `0.2783` n `136`; fx avg `0.0025` n `6`; index avg `0.0726` n `27`; metal avg `0.1182` n `20`; unknown avg `0.973` n `906`
- 4h: commodity avg `-0.1494` n `12`; crypto_alt avg `-0.5088` n `233`; crypto_major avg `-0.0999` n `8`; equity avg `0.4231` n `136`; fx avg `-0.0001` n `6`; index avg `0.0986` n `27`; metal avg `0.105` n `20`; unknown avg `0.2724` n `898`
- 24h: commodity avg `-0.1733` n `12`; crypto_alt avg `-1.4454` n `233`; crypto_major avg `-0.881` n `8`; equity avg `0.5889` n `136`; fx avg `0.1883` n `6`; index avg `0.0723` n `27`; metal avg `0.0352` n `20`; unknown avg `-0.4602` n `818`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.1097`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1075`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1035`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0988`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0901`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0861`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0845`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0823`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.08`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0679`, n `668`, weak_sample_signal
