# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-24T02:37:30.728955+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.021` n `12`; crypto_alt avg `0.1007` n `234`; crypto_major avg `0.1146` n `8`; equity avg `0.0434` n `141`; fx avg `-0.0008` n `6`; index avg `0.0162` n `26`; metal avg `0.0593` n `20`; unknown avg `0.0052` n `945`
- 1h: commodity avg `-0.0252` n `12`; crypto_alt avg `0.3957` n `234`; crypto_major avg `-0.2174` n `8`; equity avg `-0.0891` n `141`; fx avg `0.0099` n `6`; index avg `-0.0152` n `26`; metal avg `0.024` n `20`; unknown avg `0.1699` n `943`
- 4h: commodity avg `-0.1128` n `12`; crypto_alt avg `0.8569` n `234`; crypto_major avg `-0.0377` n `8`; equity avg `-0.2235` n `141`; fx avg `0.0259` n `6`; index avg `-0.0402` n `26`; metal avg `-0.0368` n `20`; unknown avg `0.3149` n `937`
- 24h: commodity avg `0.4103` n `12`; crypto_alt avg `-3.9611` n `234`; crypto_major avg `-3.7983` n `8`; equity avg `-1.4444` n `140`; fx avg `0.0792` n `6`; index avg `-0.2903` n `26`; metal avg `-0.5793` n `20`; unknown avg `583.64` n `821`

## Correlations

- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.164`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1606`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1555`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1513`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.144`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1315`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1309`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1257`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1165`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1092`, n `668`, weak_sample_signal
