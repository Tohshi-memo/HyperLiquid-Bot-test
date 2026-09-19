# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-19T03:07:26.750133+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0029` n `12`; crypto_alt avg `0.1576` n `234`; crypto_major avg `0.081` n `8`; equity avg `-0.0003` n `140`; fx avg `0.0028` n `6`; index avg `-0.0173` n `26`; metal avg `0.0142` n `20`; unknown avg `5.0022` n `940`
- 1h: commodity avg `-0.0065` n `12`; crypto_alt avg `0.6543` n `234`; crypto_major avg `0.2309` n `8`; equity avg `0.0391` n `140`; fx avg `0.004` n `6`; index avg `-0.018` n `26`; metal avg `0.015` n `20`; unknown avg `5.8553` n `940`
- 4h: commodity avg `0.1437` n `12`; crypto_alt avg `0.9983` n `234`; crypto_major avg `0.588` n `8`; equity avg `-0.0856` n `140`; fx avg `-0.0065` n `6`; index avg `-0.0176` n `26`; metal avg `-0.0274` n `20`; unknown avg `0.3975` n `934`
- 24h: commodity avg `0.0995` n `12`; crypto_alt avg `5.616` n `234`; crypto_major avg `6.0173` n `8`; equity avg `1.0504` n `140`; fx avg `0.0879` n `6`; index avg `0.056` n `26`; metal avg `0.1604` n `20`; unknown avg `4.2194` n `787`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1681`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1677`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1629`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1501`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1429`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1412`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1357`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1339`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1325`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1284`, n `668`, weak_sample_signal
