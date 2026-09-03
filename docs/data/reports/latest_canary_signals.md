# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-03T01:52:25.063319+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0363` n `12`; crypto_alt avg `-0.0501` n `232`; crypto_major avg `-0.0656` n `8`; equity avg `-0.0306` n `133`; fx avg `0.0204` n `6`; index avg `-0.0159` n `26`; metal avg `0.0112` n `20`; unknown avg `-0.0534` n `792`
- 1h: commodity avg `0.0632` n `12`; crypto_alt avg `0.4582` n `232`; crypto_major avg `0.389` n `8`; equity avg `0.0501` n `133`; fx avg `-0.0222` n `6`; index avg `0.0234` n `26`; metal avg `0.0995` n `20`; unknown avg `15.2651` n `790`
- 4h: commodity avg `0.1505` n `12`; crypto_alt avg `0.6026` n `232`; crypto_major avg `0.2811` n `8`; equity avg `0.0269` n `133`; fx avg `-0.0126` n `6`; index avg `-0.0289` n `26`; metal avg `0.1264` n `20`; unknown avg `14.6516` n `790`
- 24h: commodity avg `0.0619` n `12`; crypto_alt avg `1.4394` n `232`; crypto_major avg `0.91` n `8`; equity avg `1.4087` n `133`; fx avg `-0.3673` n `6`; index avg `0.1538` n `26`; metal avg `0.8711` n `20`; unknown avg `-0.2111` n `751`

## Correlations

- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0805`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0792`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.068`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0613`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0587`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.0583`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.058`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0557`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0543`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0478`, n `668`, weak_sample_signal
