# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-15T13:37:32.417382+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1435` n `12`; crypto_alt avg `-0.5238` n `233`; crypto_major avg `-0.5706` n `8`; equity avg `0.0712` n `136`; fx avg `0.0178` n `6`; index avg `-0.0333` n `27`; metal avg `0.0418` n `20`; unknown avg `14.3349` n `906`
- 1h: commodity avg `0.1639` n `12`; crypto_alt avg `-0.3032` n `233`; crypto_major avg `-0.281` n `8`; equity avg `-0.0157` n `136`; fx avg `0.018` n `6`; index avg `-0.0326` n `27`; metal avg `0.1332` n `20`; unknown avg `7.2861` n `904`
- 4h: commodity avg `0.0114` n `12`; crypto_alt avg `-0.3027` n `233`; crypto_major avg `-0.1136` n `8`; equity avg `0.4848` n `136`; fx avg `-0.002` n `6`; index avg `0.0969` n `27`; metal avg `0.3197` n `20`; unknown avg `8.8368` n `898`
- 24h: commodity avg `0.0988` n `12`; crypto_alt avg `-1.0427` n `233`; crypto_major avg `-0.9012` n `8`; equity avg `0.6948` n `136`; fx avg `0.1702` n `6`; index avg `0.0974` n `27`; metal avg `0.2389` n `20`; unknown avg `-0.0466` n `818`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.1252`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1027`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1011`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.101`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0938`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0901`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0855`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0848`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.077`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0707`, n `668`, weak_sample_signal
