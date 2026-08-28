# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-28T01:37:24.750694+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.07` n `12`; crypto_alt avg `-0.0896` n `231`; crypto_major avg `-0.2593` n `8`; equity avg `0.0145` n `127`; fx avg `-0.0212` n `6`; index avg `-0.0048` n `26`; metal avg `-0.1199` n `20`; unknown avg `0.1701` n `792`
- 1h: commodity avg `-0.0765` n `12`; crypto_alt avg `0.39` n `231`; crypto_major avg `0.154` n `8`; equity avg `0.1346` n `127`; fx avg `-0.0188` n `6`; index avg `-0.0012` n `26`; metal avg `-0.0191` n `20`; unknown avg `-0.2302` n `792`
- 4h: commodity avg `-0.0828` n `12`; crypto_alt avg `1.0596` n `231`; crypto_major avg `0.5689` n `8`; equity avg `0.1643` n `127`; fx avg `-0.0497` n `6`; index avg `0.0336` n `26`; metal avg `-0.087` n `20`; unknown avg `-0.2171` n `792`
- 24h: commodity avg `0.2342` n `12`; crypto_alt avg `2.0887` n `231`; crypto_major avg `2.5978` n `8`; equity avg `0.2341` n `127`; fx avg `-0.0083` n `6`; index avg `0.0468` n `26`; metal avg `-0.1239` n `20`; unknown avg `0.8225` n `775`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1324`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1238`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.095`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0871`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0819`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0759`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0651`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0589`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0563`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.056`, n `668`, weak_sample_signal
