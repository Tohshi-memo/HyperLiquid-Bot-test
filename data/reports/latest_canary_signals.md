# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-22T05:22:26.973845+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0043` n `12`; crypto_alt avg `-0.4958` n `234`; crypto_major avg `-0.316` n `8`; equity avg `-0.2393` n `140`; fx avg `0.0113` n `6`; index avg `-0.0316` n `26`; metal avg `-0.0569` n `20`; unknown avg `0.0052` n `944`
- 1h: commodity avg `0.0287` n `12`; crypto_alt avg `-0.7918` n `234`; crypto_major avg `-1.0161` n `8`; equity avg `-0.4306` n `140`; fx avg `-0.0358` n `6`; index avg `-0.0603` n `26`; metal avg `-0.0148` n `20`; unknown avg `2.1916` n `942`
- 4h: commodity avg `0.1238` n `12`; crypto_alt avg `-0.492` n `234`; crypto_major avg `-0.4009` n `8`; equity avg `-0.7366` n `140`; fx avg `-0.0511` n `6`; index avg `-0.1037` n `26`; metal avg `-0.1115` n `20`; unknown avg `3.0488` n `936`
- 24h: commodity avg `-0.1462` n `12`; crypto_alt avg `2.3056` n `234`; crypto_major avg `3.7339` n `8`; equity avg `1.6629` n `140`; fx avg `-0.275` n `6`; index avg `0.3802` n `26`; metal avg `-0.0747` n `20`; unknown avg `8.3008` n `772`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1512`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1327`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1217`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1111`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1083`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1014`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0993`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0973`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0912`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0853`, n `668`, weak_sample_signal
