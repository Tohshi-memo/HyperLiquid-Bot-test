# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-13T11:37:25.769936+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.003` n `12`; crypto_alt avg `0.0601` n `233`; crypto_major avg `0.0816` n `8`; equity avg `-0.0149` n `136`; fx avg `-0.0054` n `6`; index avg `0.0069` n `27`; metal avg `-0.0021` n `20`; unknown avg `0.1404` n `838`
- 1h: commodity avg `0.1536` n `12`; crypto_alt avg `-0.1024` n `233`; crypto_major avg `-0.0489` n `8`; equity avg `-0.0575` n `136`; fx avg `0.0009` n `6`; index avg `0.0017` n `27`; metal avg `-0.0122` n `20`; unknown avg `0.0316` n `836`
- 4h: commodity avg `0.1445` n `12`; crypto_alt avg `-0.7499` n `233`; crypto_major avg `-0.9169` n `8`; equity avg `-0.8539` n `136`; fx avg `0.0125` n `6`; index avg `-0.1288` n `27`; metal avg `-0.0629` n `20`; unknown avg `0.4653` n `830`
- 24h: commodity avg `0.2837` n `12`; crypto_alt avg `-0.572` n `233`; crypto_major avg `-1.9174` n `8`; equity avg `-1.7829` n `136`; fx avg `0.0076` n `6`; index avg `-0.2709` n `26`; metal avg `-0.0484` n `20`; unknown avg `-0.3332` n `708`

## Correlations

- market_context_score -> index_forward_1h_return_pct: corr `-0.0916`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0872`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0773`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0755`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.071`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0657`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.065`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0611`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.059`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.058`, n `668`, weak_sample_signal
