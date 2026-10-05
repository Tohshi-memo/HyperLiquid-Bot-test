# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-05T16:52:38.669577+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0076` n `13`; crypto_alt avg `0.0732` n `235`; crypto_major avg `0.146` n `8`; equity avg `0.0515` n `144`; fx avg `0.0018` n `6`; index avg `0.0208` n `26`; metal avg `0.0269` n `20`; unknown avg `0.1446` n `1079`
- 1h: commodity avg `-0.0632` n `13`; crypto_alt avg `-0.0304` n `235`; crypto_major avg `0.1009` n `8`; equity avg `-0.0359` n `144`; fx avg `-0.0099` n `6`; index avg `0.0278` n `26`; metal avg `-0.0504` n `20`; unknown avg `1.3844` n `1071`
- 4h: commodity avg `-0.1139` n `13`; crypto_alt avg `-0.8518` n `235`; crypto_major avg `-0.427` n `8`; equity avg `0.3052` n `144`; fx avg `-0.0508` n `6`; index avg `0.1724` n `26`; metal avg `-0.1091` n `20`; unknown avg `0.706` n `989`
- 24h: commodity avg `-0.2086` n `13`; crypto_alt avg `-0.1249` n `235`; crypto_major avg `0.0722` n `8`; equity avg `0.2632` n `144`; fx avg `-0.0993` n `6`; index avg `0.1154` n `26`; metal avg `0.1361` n `20`; unknown avg `-0.1921` n `826`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.2011`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1784`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1683`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1257`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1075`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1064`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1009`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0987`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0919`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0911`, n `668`, weak_sample_signal
