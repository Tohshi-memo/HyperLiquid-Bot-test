# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-03T10:07:29.647738+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0713` n `13`; crypto_alt avg `0.0633` n `239`; crypto_major avg `0.045` n `8`; equity avg `0.1948` n `157`; fx avg `-0.0164` n `6`; index avg `0.0167` n `27`; metal avg `0.0161` n `20`; unknown avg `-0.0732` n `1258`
- 1h: commodity avg `-0.2022` n `13`; crypto_alt avg `0.2444` n `239`; crypto_major avg `0.1892` n `8`; equity avg `0.4395` n `157`; fx avg `-0.0053` n `6`; index avg `0.0438` n `27`; metal avg `0.1046` n `20`; unknown avg `0.1937` n `1258`
- 4h: commodity avg `0.1486` n `13`; crypto_alt avg `0.4797` n `239`; crypto_major avg `0.7117` n `8`; equity avg `1.2622` n `157`; fx avg `0.0652` n `6`; index avg `0.1191` n `27`; metal avg `-0.1505` n `20`; unknown avg `20.048` n `1224`
- 24h: commodity avg `-0.4569` n `13`; crypto_alt avg `-1.5828` n `238`; crypto_major avg `-0.8976` n `8`; equity avg `-3.4162` n `157`; fx avg `-0.0086` n `6`; index avg `-0.2154` n `27`; metal avg `-0.4287` n `20`; unknown avg `3.9603` n `1023`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `0.1682`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1624`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1604`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1517`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1283`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1196`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1157`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1089`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.108`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1047`, n `668`, weak_sample_signal
