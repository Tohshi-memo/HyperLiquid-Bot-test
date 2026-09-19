# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-19T00:07:30.553782+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0252` n `12`; crypto_alt avg `0.1427` n `234`; crypto_major avg `0.0257` n `8`; equity avg `0.0098` n `140`; fx avg `0.0001` n `6`; index avg `0.002` n `26`; metal avg `-0.0044` n `20`; unknown avg `3.9508` n `934`
- 1h: commodity avg `0.135` n `12`; crypto_alt avg `0.1877` n `234`; crypto_major avg `-0.2538` n `8`; equity avg `0.0127` n `140`; fx avg `0.0142` n `6`; index avg `0.0044` n `26`; metal avg `-0.0255` n `20`; unknown avg `3.8789` n `934`
- 4h: commodity avg `0.134` n `12`; crypto_alt avg `0.5501` n `234`; crypto_major avg `-0.4372` n `8`; equity avg `-0.0222` n `140`; fx avg `0.0506` n `6`; index avg `-0.0106` n `26`; metal avg `-0.0325` n `20`; unknown avg `3.7643` n `884`
- 24h: commodity avg `0.1315` n `12`; crypto_alt avg `6.5288` n `234`; crypto_major avg `6.2661` n `8`; equity avg `1.42` n `140`; fx avg `0.2153` n `6`; index avg `0.1291` n `26`; metal avg `0.3184` n `20`; unknown avg `5.2107` n `777`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1656`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1522`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1485`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1432`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1401`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1363`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1276`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1272`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1259`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1231`, n `668`, weak_sample_signal
