# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-19T00:52:30.963527+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0086` n `12`; crypto_alt avg `-0.1694` n `234`; crypto_major avg `-0.0243` n `8`; equity avg `0.0149` n `140`; fx avg `-0.0008` n `6`; index avg `-0.0217` n `26`; metal avg `-0.0083` n `20`; unknown avg `0.0349` n `942`
- 1h: commodity avg `-0.0068` n `12`; crypto_alt avg `0.2967` n `234`; crypto_major avg `0.5481` n `8`; equity avg `0.0432` n `140`; fx avg `-0.0148` n `6`; index avg `-0.0051` n `26`; metal avg `-0.0071` n `20`; unknown avg `0.1066` n `934`
- 4h: commodity avg `0.1701` n `12`; crypto_alt avg `0.354` n `234`; crypto_major avg `0.1629` n `8`; equity avg `0.0239` n `140`; fx avg `0.0127` n `6`; index avg `-0.0233` n `26`; metal avg `-0.0142` n `20`; unknown avg `9.0294` n `908`
- 24h: commodity avg `0.155` n `12`; crypto_alt avg `6.4827` n `234`; crypto_major avg `6.8062` n `8`; equity avg `1.5579` n `140`; fx avg `0.179` n `6`; index avg `0.1286` n `26`; metal avg `0.2143` n `20`; unknown avg `4.0754` n `777`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1643`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1601`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1506`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1477`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1424`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1353`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1325`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1294`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.128`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1226`, n `668`, weak_sample_signal
