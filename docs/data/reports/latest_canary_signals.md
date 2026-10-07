# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-07T10:07:30.182654+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0091` n `13`; crypto_alt avg `-0.1024` n `235`; crypto_major avg `-0.2748` n `8`; equity avg `0.0095` n `150`; fx avg `-0.0105` n `6`; index avg `0.0099` n `26`; metal avg `0.016` n `20`; unknown avg `1.4028` n `1074`
- 1h: commodity avg `0.0488` n `13`; crypto_alt avg `-0.6835` n `235`; crypto_major avg `-0.7285` n `8`; equity avg `-0.1492` n `150`; fx avg `-0.0239` n `6`; index avg `-0.0217` n `26`; metal avg `-0.0221` n `20`; unknown avg `1.3561` n `1074`
- 4h: commodity avg `0.0771` n `13`; crypto_alt avg `-1.1096` n `235`; crypto_major avg `-1.0062` n `8`; equity avg `-0.654` n `150`; fx avg `-0.0979` n `6`; index avg `-0.085` n `26`; metal avg `-0.2484` n `20`; unknown avg `1.4063` n `1058`
- 24h: commodity avg `1.1671` n `13`; crypto_alt avg `-4.5823` n `235`; crypto_major avg `-3.163` n `8`; equity avg `-0.9811` n `150`; fx avg `-0.1043` n `6`; index avg `-0.1838` n `26`; metal avg `-0.4229` n `20`; unknown avg `814.9604` n `978`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1668`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1592`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1587`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0848`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0768`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0682`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0671`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0664`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0636`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0629`, n `668`, weak_sample_signal
