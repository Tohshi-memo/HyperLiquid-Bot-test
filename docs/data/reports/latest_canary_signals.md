# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-27T22:52:27.335146+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0152` n `12`; crypto_alt avg `0.1801` n `234`; crypto_major avg `0.146` n `8`; equity avg `-0.0245` n `141`; fx avg `0.0018` n `6`; index avg `-0.0041` n `26`; metal avg `-0.0191` n `20`; unknown avg `3.2771` n `958`
- 1h: commodity avg `-0.3509` n `12`; crypto_alt avg `-0.6188` n `234`; crypto_major avg `-0.6249` n `8`; equity avg `-0.3715` n `141`; fx avg `0.0225` n `6`; index avg `-0.1131` n `26`; metal avg `-0.1849` n `20`; unknown avg `1.2951` n `926`
- 4h: commodity avg `-0.3051` n `12`; crypto_alt avg `-0.8169` n `234`; crypto_major avg `-0.9291` n `8`; equity avg `-0.3947` n `141`; fx avg `-0.0092` n `6`; index avg `-0.1046` n `26`; metal avg `-0.1936` n `20`; unknown avg `2.3726` n `860`
- 24h: commodity avg `-0.4578` n `12`; crypto_alt avg `0.3817` n `234`; crypto_major avg `-0.2837` n `8`; equity avg `-0.0569` n `141`; fx avg `-0.0161` n `6`; index avg `-0.0612` n `26`; metal avg `-0.2052` n `20`; unknown avg `5.4398` n `827`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1637`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1544`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1401`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1353`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1321`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.128`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1251`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1047`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1019`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0972`, n `668`, weak_sample_signal
