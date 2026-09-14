# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-14T22:36:30.265399+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0091` n `12`; crypto_alt avg `-0.0107` n `233`; crypto_major avg `-0.0155` n `8`; equity avg `-0.022` n `136`; fx avg `0.0014` n `6`; index avg `-0.0038` n `27`; metal avg `0.0071` n `20`; unknown avg `0.8799` n `908`
- 1h: commodity avg `0.0046` n `12`; crypto_alt avg `-0.1812` n `233`; crypto_major avg `-0.1792` n `8`; equity avg `-0.0062` n `136`; fx avg `-0.0112` n `6`; index avg `-0.0046` n `27`; metal avg `-0.0054` n `20`; unknown avg `0.4749` n `894`
- 4h: commodity avg `0.1962` n `12`; crypto_alt avg `-0.8015` n `233`; crypto_major avg `-0.7586` n `8`; equity avg `-0.432` n `136`; fx avg `0.001` n `6`; index avg `-0.1038` n `27`; metal avg `-0.1162` n `20`; unknown avg `0.5969` n `866`
- 24h: commodity avg `-0.1094` n `12`; crypto_alt avg `1.5006` n `233`; crypto_major avg `2.7234` n `8`; equity avg `-0.3542` n `136`; fx avg `0.0022` n `6`; index avg `-0.1547` n `27`; metal avg `-0.3172` n `20`; unknown avg `0.6392` n `676`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `0.1013`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.101`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0963`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0958`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0937`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0746`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0743`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0733`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0629`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0622`, n `668`, weak_sample_signal
