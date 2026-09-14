# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-14T01:37:01.432898+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0873` n `12`; crypto_alt avg `-0.0347` n `233`; crypto_major avg `-0.0179` n `8`; equity avg `0.0897` n `136`; fx avg `-0.0079` n `6`; index avg `0.0282` n `27`; metal avg `0.0611` n `20`; unknown avg `1.1146` n `894`
- 1h: commodity avg `-0.0205` n `12`; crypto_alt avg `-0.0525` n `233`; crypto_major avg `-0.1806` n `8`; equity avg `-0.1368` n `136`; fx avg `-0.0073` n `6`; index avg `0.0151` n `27`; metal avg `0.0442` n `20`; unknown avg `-0.3286` n `774`
- 4h: commodity avg `0.3802` n `12`; crypto_alt avg `-1.6247` n `233`; crypto_major avg `-1.1582` n `8`; equity avg `-0.9158` n `136`; fx avg `0.0076` n `6`; index avg `-0.1843` n `27`; metal avg `-0.0567` n `20`; unknown avg `12.7653` n `768`
- 24h: commodity avg `0.7471` n `12`; crypto_alt avg `-1.8044` n `233`; crypto_major avg `-1.612` n `8`; equity avg `-1.9109` n `136`; fx avg `0.0567` n `6`; index avg `-0.3922` n `26`; metal avg `-0.1101` n `20`; unknown avg `1.4175` n `682`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1317`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1283`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1216`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1147`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0991`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0984`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0887`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0853`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0837`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0774`, n `668`, weak_sample_signal
