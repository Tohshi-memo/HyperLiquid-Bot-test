# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-14T10:37:30.454414+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0248` n `12`; crypto_alt avg `0.0879` n `233`; crypto_major avg `-0.0024` n `8`; equity avg `0.1263` n `136`; fx avg `0.0144` n `6`; index avg `0.0305` n `27`; metal avg `0.032` n `20`; unknown avg `0.2431` n `894`
- 1h: commodity avg `-0.0482` n `12`; crypto_alt avg `0.3502` n `233`; crypto_major avg `0.3122` n `8`; equity avg `0.3355` n `136`; fx avg `0.006` n `6`; index avg `0.0592` n `27`; metal avg `0.0821` n `20`; unknown avg `0.3601` n `892`
- 4h: commodity avg `0.0972` n `12`; crypto_alt avg `-0.1806` n `233`; crypto_major avg `0.4116` n `8`; equity avg `-0.4685` n `136`; fx avg `-0.0189` n `6`; index avg `-0.0722` n `27`; metal avg `-0.3707` n `20`; unknown avg `5.5171` n `862`
- 24h: commodity avg `0.6251` n `12`; crypto_alt avg `0.2546` n `233`; crypto_major avg `1.7809` n `8`; equity avg `-0.7778` n `136`; fx avg `0.0368` n `6`; index avg `-0.2202` n `27`; metal avg `-0.4632` n `20`; unknown avg `0.97` n `650`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `0.1182`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1178`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.114`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.111`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0965`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.088`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0853`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0777`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0752`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0738`, n `668`, weak_sample_signal
