# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-10T05:37:28.228547+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1233` n `13`; crypto_alt avg `0.1364` n `239`; crypto_major avg `0.1402` n `8`; equity avg `0.2094` n `160`; fx avg `-0.0394` n `6`; index avg `0.0385` n `27`; metal avg `-0.0054` n `20`; unknown avg `1.7435` n `1259`
- 1h: commodity avg `0.1653` n `13`; crypto_alt avg `0.2706` n `239`; crypto_major avg `0.5019` n `8`; equity avg `0.4668` n `160`; fx avg `-0.0653` n `6`; index avg `0.1028` n `27`; metal avg `0.0176` n `20`; unknown avg `1.1569` n `1247`
- 4h: commodity avg `0.0812` n `13`; crypto_alt avg `0.4146` n `239`; crypto_major avg `0.126` n `8`; equity avg `0.3662` n `160`; fx avg `-0.0888` n `6`; index avg `0.0705` n `27`; metal avg `-0.0051` n `20`; unknown avg `20.4157` n `1233`
- 24h: commodity avg `-0.4662` n `13`; crypto_alt avg `1.5615` n `239`; crypto_major avg `0.438` n `8`; equity avg `4.3031` n `160`; fx avg `-0.0298` n `6`; index avg `0.4771` n `27`; metal avg `0.1399` n `20`; unknown avg `190.6449` n `1065`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1983`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1472`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1385`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1378`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1337`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1318`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1283`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1057`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1033`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.101`, n `668`, weak_sample_signal
