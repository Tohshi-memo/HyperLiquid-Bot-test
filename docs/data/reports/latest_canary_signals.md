# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-20T00:08:02.100042+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0656` n `12`; crypto_alt avg `-0.0788` n `234`; crypto_major avg `-0.1635` n `8`; equity avg `0.0012` n `140`; fx avg `0.0025` n `6`; index avg `-0.0015` n `26`; metal avg `-0.0017` n `20`; unknown avg `0.337` n `935`
- 1h: commodity avg `0.101` n `12`; crypto_alt avg `0.0271` n `234`; crypto_major avg `-0.0665` n `8`; equity avg `-0.0026` n `140`; fx avg `-0.0178` n `6`; index avg `-0.0048` n `26`; metal avg `-0.0018` n `20`; unknown avg `0.1547` n `919`
- 4h: commodity avg `0.1569` n `12`; crypto_alt avg `-0.2226` n `234`; crypto_major avg `-0.5596` n `8`; equity avg `0.0056` n `140`; fx avg `-0.0443` n `6`; index avg `0.0023` n `26`; metal avg `-0.0024` n `20`; unknown avg `0.3822` n `911`
- 24h: commodity avg `0.0266` n `12`; crypto_alt avg `0.9973` n `234`; crypto_major avg `-0.0097` n `8`; equity avg `-0.0233` n `140`; fx avg `-0.092` n `6`; index avg `0.0137` n `26`; metal avg `-0.0002` n `20`; unknown avg `0.796` n `822`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1737`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1677`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1594`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1562`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1526`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1352`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1339`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1219`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1173`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1167`, n `668`, weak_sample_signal
