# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-06T07:37:26.443480+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0562` n `13`; crypto_alt avg `0.106` n `235`; crypto_major avg `0.0495` n `8`; equity avg `0.0242` n `149`; fx avg `0.0111` n `6`; index avg `0.006` n `26`; metal avg `-0.0154` n `20`; unknown avg `0.1108` n `1074`
- 1h: commodity avg `0.0232` n `13`; crypto_alt avg `0.1665` n `235`; crypto_major avg `0.0482` n `8`; equity avg `-0.01` n `149`; fx avg `0.028` n `6`; index avg `-0.0002` n `26`; metal avg `0.0097` n `20`; unknown avg `0.1772` n `1008`
- 4h: commodity avg `-0.2224` n `13`; crypto_alt avg `0.5257` n `235`; crypto_major avg `-0.0327` n `8`; equity avg `0.1244` n `149`; fx avg `0.0342` n `6`; index avg `0.0393` n `26`; metal avg `-0.0242` n `20`; unknown avg `0.0892` n `986`
- 24h: commodity avg `-0.2854` n `13`; crypto_alt avg `-1.2922` n `235`; crypto_major avg `-0.9632` n `8`; equity avg `0.2621` n `149`; fx avg `0.0663` n `6`; index avg `0.165` n `26`; metal avg `-0.1142` n `20`; unknown avg `-0.2754` n `830`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1869`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1705`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1625`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1468`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1038`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1019`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0979`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0952`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0929`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0908`, n `668`, weak_sample_signal
