# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-15T08:52:30.405683+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0187` n `12`; crypto_alt avg `0.1188` n `233`; crypto_major avg `0.084` n `8`; equity avg `0.0101` n `136`; fx avg `0.0205` n `6`; index avg `-0.0031` n `27`; metal avg `-0.0175` n `20`; unknown avg `-0.003` n `908`
- 1h: commodity avg `-0.0371` n `12`; crypto_alt avg `0.1835` n `233`; crypto_major avg `0.0433` n `8`; equity avg `-0.1597` n `136`; fx avg `0.0556` n `6`; index avg `-0.0202` n `27`; metal avg `-0.0078` n `20`; unknown avg `0.1785` n `900`
- 4h: commodity avg `0.0825` n `12`; crypto_alt avg `-0.7884` n `233`; crypto_major avg `-0.7661` n `8`; equity avg `-0.4047` n `136`; fx avg `0.1388` n `6`; index avg `-0.0889` n `27`; metal avg `-0.2636` n `20`; unknown avg `19.2242` n `876`
- 24h: commodity avg `-0.0003` n `12`; crypto_alt avg `-1.397` n `233`; crypto_major avg `-0.895` n `8`; equity avg `-0.2183` n `136`; fx avg `0.2524` n `6`; index avg `-0.0828` n `27`; metal avg `-0.2713` n `20`; unknown avg `4.6213` n `820`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1078`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1019`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.101`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.099`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0872`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0856`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0813`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0735`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0641`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0633`, n `668`, weak_sample_signal
