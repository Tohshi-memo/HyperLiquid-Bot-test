# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-22T23:37:34.316025+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0478` n `13`; crypto_alt avg `0.0759` n `239`; crypto_major avg `0.1976` n `8`; equity avg `0.1546` n `166`; fx avg `0.0029` n `6`; index avg `0.0057` n `27`; metal avg `-0.054` n `20`; unknown avg `316.3404` n `1264`
- 1h: commodity avg `-0.3176` n `13`; crypto_alt avg `0.3599` n `239`; crypto_major avg `0.694` n `8`; equity avg `0.5662` n `166`; fx avg `0.045` n `6`; index avg `0.0322` n `27`; metal avg `0.3651` n `20`; unknown avg `44.8673` n `1244`
- 4h: commodity avg `-0.361` n `13`; crypto_alt avg `0.0688` n `239`; crypto_major avg `0.5252` n `8`; equity avg `0.4048` n `166`; fx avg `0.1342` n `6`; index avg `-0.0108` n `27`; metal avg `0.3145` n `20`; unknown avg `0.1522` n `1200`
- 24h: commodity avg `-0.4678` n `13`; crypto_alt avg `0.5655` n `239`; crypto_major avg `1.0985` n `8`; equity avg `1.1894` n `166`; fx avg `0.104` n `6`; index avg `0.0512` n `27`; metal avg `0.347` n `20`; unknown avg `435.801` n `1032`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `-0.17`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1665`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1651`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.158`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1528`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1417`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1326`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.128`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1269`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1235`, n `668`, weak_sample_signal
