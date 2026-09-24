# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-24T22:07:32.513940+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0951` n `12`; crypto_alt avg `-0.3825` n `234`; crypto_major avg `-0.3601` n `8`; equity avg `-0.0222` n `141`; fx avg `0.0049` n `6`; index avg `-0.0034` n `26`; metal avg `0.021` n `20`; unknown avg `0.1292` n `904`
- 1h: commodity avg `-0.1501` n `12`; crypto_alt avg `0.1152` n `234`; crypto_major avg `-0.0849` n `8`; equity avg `0.0468` n `141`; fx avg `-0.0091` n `6`; index avg `0.0044` n `26`; metal avg `0.0077` n `20`; unknown avg `3.7408` n `904`
- 4h: commodity avg `-0.2155` n `12`; crypto_alt avg `0.6164` n `234`; crypto_major avg `0.1773` n `8`; equity avg `0.2904` n `141`; fx avg `-0.0266` n `6`; index avg `0.0195` n `26`; metal avg `0.0481` n `20`; unknown avg `7.5141` n `829`
- 24h: commodity avg `0.6485` n `12`; crypto_alt avg `3.2938` n `234`; crypto_major avg `0.529` n `8`; equity avg `-0.3559` n `141`; fx avg `0.0258` n `6`; index avg `-0.15` n `26`; metal avg `-0.1376` n `20`; unknown avg `20.3553` n `815`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1579`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1578`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1405`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1388`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1258`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1243`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1204`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1114`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1068`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1006`, n `668`, weak_sample_signal
