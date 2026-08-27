# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-27T19:52:26.116931+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0645` n `12`; crypto_alt avg `0.0364` n `231`; crypto_major avg `-0.1315` n `8`; equity avg `0.1925` n `127`; fx avg `-0.0049` n `6`; index avg `0.0259` n `26`; metal avg `0.0079` n `20`; unknown avg `0.0778` n `792`
- 1h: commodity avg `-0.0627` n `12`; crypto_alt avg `0.1197` n `231`; crypto_major avg `0.2144` n `8`; equity avg `0.2946` n `127`; fx avg `-0.0006` n `6`; index avg `0.0738` n `26`; metal avg `0.0371` n `20`; unknown avg `-0.0647` n `792`
- 4h: commodity avg `0.1767` n `12`; crypto_alt avg `-0.2628` n `231`; crypto_major avg `-0.0269` n `8`; equity avg `0.3977` n `127`; fx avg `0.0148` n `6`; index avg `0.0119` n `26`; metal avg `0.128` n `20`; unknown avg `0.2792` n `792`
- 24h: commodity avg `0.3748` n `12`; crypto_alt avg `2.9307` n `231`; crypto_major avg `3.9838` n `8`; equity avg `1.7249` n `127`; fx avg `-0.0439` n `6`; index avg `0.1665` n `26`; metal avg `0.2557` n `20`; unknown avg `1.1035` n `775`

## Correlations

- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1294`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1246`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0913`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0832`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0772`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0743`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0698`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0666`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0622`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0546`, n `668`, weak_sample_signal
