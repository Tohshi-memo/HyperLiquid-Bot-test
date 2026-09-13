# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-13T20:07:26.269636+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.012` n `12`; crypto_alt avg `0.1554` n `233`; crypto_major avg `0.1562` n `8`; equity avg `0.0057` n `136`; fx avg `0.007` n `6`; index avg `0.0142` n `27`; metal avg `0.0049` n `20`; unknown avg `4.6498` n `838`
- 1h: commodity avg `0.0496` n `12`; crypto_alt avg `-0.4111` n `233`; crypto_major avg `-0.2504` n `8`; equity avg `-0.1378` n `136`; fx avg `-0.0007` n `6`; index avg `-0.0134` n `27`; metal avg `-0.0218` n `20`; unknown avg `9.4638` n `838`
- 4h: commodity avg `0.081` n `12`; crypto_alt avg `0.2404` n `233`; crypto_major avg `0.3176` n `8`; equity avg `0.1561` n `136`; fx avg `-0.0002` n `6`; index avg `-0.0264` n `27`; metal avg `0.0035` n `20`; unknown avg `2.9866` n `766`
- 24h: commodity avg `0.2992` n `12`; crypto_alt avg `0.0364` n `233`; crypto_major avg `-0.6316` n `8`; equity avg `-1.2482` n `136`; fx avg `0.013` n `6`; index avg `-0.2566` n `26`; metal avg `-0.0803` n `20`; unknown avg `3.6489` n `720`

## Correlations

- market_context_score -> index_forward_1h_return_pct: corr `-0.098`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0952`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0864`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0847`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0781`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0746`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0662`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0659`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0647`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0609`, n `668`, weak_sample_signal
