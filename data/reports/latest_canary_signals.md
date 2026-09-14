# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-14T08:07:51.985204+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0763` n `12`; crypto_alt avg `0.0001` n `233`; crypto_major avg `0.024` n `8`; equity avg `-0.172` n `136`; fx avg `0.0021` n `6`; index avg `0.0193` n `27`; metal avg `-0.0102` n `20`; unknown avg `0.977` n `892`
- 1h: commodity avg `-0.0004` n `12`; crypto_alt avg `-0.161` n `233`; crypto_major avg `0.0458` n `8`; equity avg `-0.38` n `136`; fx avg `-0.0088` n `6`; index avg `-0.0118` n `27`; metal avg `-0.0967` n `20`; unknown avg `1.11` n `892`
- 4h: commodity avg `0.0238` n `12`; crypto_alt avg `-0.0393` n `233`; crypto_major avg `0.3372` n `8`; equity avg `-0.6991` n `136`; fx avg `0.0057` n `6`; index avg `-0.0864` n `27`; metal avg `-0.1639` n `20`; unknown avg `0.9421` n `832`
- 24h: commodity avg `0.6646` n `12`; crypto_alt avg `-0.2854` n `233`; crypto_major avg `0.8085` n `8`; equity avg `-1.5354` n `136`; fx avg `0.0464` n `6`; index avg `-0.3113` n `27`; metal avg `-0.2958` n `20`; unknown avg `0.8503` n `650`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1239`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1161`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1153`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1142`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0909`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0879`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0855`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0838`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0805`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0739`, n `668`, weak_sample_signal
