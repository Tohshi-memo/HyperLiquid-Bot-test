# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-05T13:01:04.693499+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0184` n `12`; crypto_alt avg `0.0678` n `232`; crypto_major avg `0.0316` n `8`; equity avg `0.0026` n `134`; fx avg `-0.0037` n `6`; index avg `0.0059` n `26`; metal avg `-0.0036` n `20`; unknown avg `16.8898` n `790`
- 1h: commodity avg `-0.0025` n `12`; crypto_alt avg `0.408` n `232`; crypto_major avg `0.5804` n `8`; equity avg `0.0179` n `134`; fx avg `0.0003` n `6`; index avg `0.016` n `26`; metal avg `-0.0141` n `20`; unknown avg `-0.1347` n `783`
- 4h: commodity avg `0.0054` n `12`; crypto_alt avg `0.4437` n `232`; crypto_major avg `0.6086` n `8`; equity avg `0.0773` n `134`; fx avg `-0.0076` n `6`; index avg `0.0464` n `26`; metal avg `-0.0051` n `20`; unknown avg `-0.2197` n `780`
- 24h: commodity avg `0.1931` n `12`; crypto_alt avg `3.2364` n `232`; crypto_major avg `1.6507` n `8`; equity avg `1.8099` n `134`; fx avg `0.0081` n `6`; index avg `0.22` n `26`; metal avg `0.2514` n `20`; unknown avg `16.7389` n `664`

## Correlations

- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1666`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1524`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1319`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1238`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1213`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1173`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1115`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1103`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0957`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0943`, n `668`, weak_sample_signal
