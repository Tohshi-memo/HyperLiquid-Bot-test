# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-06T13:22:26.382551+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0228` n `13`; crypto_alt avg `0.0861` n `239`; crypto_major avg `0.1184` n `8`; equity avg `0.1362` n `158`; fx avg `0.0015` n `6`; index avg `0.048` n `27`; metal avg `0.0547` n `20`; unknown avg `1.0` n `1255`
- 1h: commodity avg `0.0033` n `13`; crypto_alt avg `-0.2518` n `239`; crypto_major avg `-0.3435` n `8`; equity avg `-0.2545` n `158`; fx avg `-0.0352` n `6`; index avg `0.0188` n `27`; metal avg `0.0202` n `20`; unknown avg `1.9215` n `1253`
- 4h: commodity avg `0.2432` n `13`; crypto_alt avg `0.3595` n `239`; crypto_major avg `-0.0619` n `8`; equity avg `0.13` n `158`; fx avg `0.0697` n `6`; index avg `0.042` n `27`; metal avg `-0.0483` n `20`; unknown avg `5.4113` n `1176`
- 24h: commodity avg `0.4812` n `13`; crypto_alt avg `-2.3104` n `239`; crypto_major avg `-4.5325` n `8`; equity avg `-3.6507` n `158`; fx avg `0.0016` n `6`; index avg `-0.5372` n `27`; metal avg `-0.2723` n `20`; unknown avg `11.4538` n `1078`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2182`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1608`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.143`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1412`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1402`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1329`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.128`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1097`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1096`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0986`, n `668`, weak_sample_signal
