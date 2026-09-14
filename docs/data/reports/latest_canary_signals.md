# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-14T12:52:29.354724+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1789` n `12`; crypto_alt avg `-0.1647` n `233`; crypto_major avg `-0.1137` n `8`; equity avg `0.0078` n `136`; fx avg `0.0191` n `6`; index avg `0.0096` n `27`; metal avg `0.0059` n `20`; unknown avg `0.0071` n `894`
- 1h: commodity avg `0.0321` n `12`; crypto_alt avg `-0.3251` n `233`; crypto_major avg `-0.1708` n `8`; equity avg `-0.3054` n `136`; fx avg `0.0244` n `6`; index avg `-0.0494` n `27`; metal avg `-0.0051` n `20`; unknown avg `5.889` n `886`
- 4h: commodity avg `0.0341` n `12`; crypto_alt avg `-0.4989` n `233`; crypto_major avg `-0.0338` n `8`; equity avg `-0.4774` n `136`; fx avg `0.0537` n `6`; index avg `-0.0588` n `27`; metal avg `-0.1469` n `20`; unknown avg `5.0569` n `886`
- 24h: commodity avg `0.5811` n `12`; crypto_alt avg `-0.3809` n `233`; crypto_major avg `1.6029` n `8`; equity avg `-1.1402` n `136`; fx avg `0.0809` n `6`; index avg `-0.2427` n `27`; metal avg `-0.471` n `20`; unknown avg `1.3373` n `650`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `0.124`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1185`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1144`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1131`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0936`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0799`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0798`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0787`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.069`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0673`, n `668`, weak_sample_signal
