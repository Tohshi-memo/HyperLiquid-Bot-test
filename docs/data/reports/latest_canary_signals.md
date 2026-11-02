# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-02T17:22:30.798403+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0177` n `13`; crypto_alt avg `-0.4867` n `239`; crypto_major avg `-0.4723` n `8`; equity avg `-0.2055` n `156`; fx avg `0.0017` n `6`; index avg `-0.0191` n `27`; metal avg `-0.029` n `20`; unknown avg `-0.1333` n `1261`
- 1h: commodity avg `-0.0629` n `13`; crypto_alt avg `-0.4486` n `239`; crypto_major avg `-0.4048` n `8`; equity avg `-0.3272` n `156`; fx avg `0.0257` n `6`; index avg `-0.023` n `27`; metal avg `-0.0258` n `20`; unknown avg `-0.4888` n `1257`
- 4h: commodity avg `-0.7412` n `13`; crypto_alt avg `-0.6264` n `239`; crypto_major avg `-0.5782` n `8`; equity avg `-1.11` n `156`; fx avg `0.0094` n `6`; index avg `0.0106` n `27`; metal avg `0.4382` n `20`; unknown avg `14.9795` n `1251`
- 24h: commodity avg `-1.1805` n `13`; crypto_alt avg `-2.6099` n `238`; crypto_major avg `-1.4052` n `8`; equity avg `-1.0509` n `156`; fx avg `0.2885` n `6`; index avg `0.1956` n `27`; metal avg `0.3823` n `20`; unknown avg `7.6434` n `1077`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1703`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.164`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1573`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1547`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1241`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.124`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1186`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1171`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1112`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1097`, n `668`, weak_sample_signal
