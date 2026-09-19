# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-19T01:52:28.393747+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.001` n `12`; crypto_alt avg `0.5309` n `234`; crypto_major avg `0.4559` n `8`; equity avg `0.0207` n `140`; fx avg `-0.0091` n `6`; index avg `-0.002` n `26`; metal avg `0.016` n `20`; unknown avg `-0.1339` n `942`
- 1h: commodity avg `-0.0067` n `12`; crypto_alt avg `-0.1106` n `234`; crypto_major avg `0.0371` n `8`; equity avg `-0.1235` n `140`; fx avg `-0.0108` n `6`; index avg `0.0041` n `26`; metal avg `-0.0063` n `20`; unknown avg `0.059` n `940`
- 4h: commodity avg `0.168` n `12`; crypto_alt avg `0.1838` n `234`; crypto_major avg `0.3103` n `8`; equity avg `-0.1224` n `140`; fx avg `-0.0186` n `6`; index avg `-0.0157` n `26`; metal avg `-0.0249` n `20`; unknown avg `16.9256` n `924`
- 24h: commodity avg `0.1508` n `12`; crypto_alt avg `5.5449` n `234`; crypto_major avg `6.0898` n `8`; equity avg `1.4263` n `140`; fx avg `0.1259` n `6`; index avg `0.1496` n `26`; metal avg `0.2184` n `20`; unknown avg `3.9501` n `777`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1595`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1519`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1493`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1367`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1328`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1305`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1299`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1286`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1265`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1194`, n `668`, weak_sample_signal
