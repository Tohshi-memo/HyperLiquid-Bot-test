# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-18T21:53:05.838018+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0108` n `12`; crypto_alt avg `-0.1076` n `234`; crypto_major avg `-0.0923` n `8`; equity avg `0.0289` n `140`; fx avg `-0.0015` n `6`; index avg `0.0068` n `26`; metal avg `-0.0051` n `20`; unknown avg `-0.1575` n `934`
- 1h: commodity avg `-0.0044` n `12`; crypto_alt avg `0.0625` n `234`; crypto_major avg `-0.109` n `8`; equity avg `0.0229` n `140`; fx avg `0.0205` n `6`; index avg `-0.0035` n `26`; metal avg `0.0045` n `20`; unknown avg `8.964` n `924`
- 4h: commodity avg `-0.0929` n `12`; crypto_alt avg `1.1902` n `234`; crypto_major avg `0.6101` n `8`; equity avg `0.6409` n `140`; fx avg `0.0565` n `6`; index avg `0.1454` n `26`; metal avg `-0.0998` n `20`; unknown avg `2.7299` n `880`
- 24h: commodity avg `-0.0746` n `12`; crypto_alt avg `7.0889` n `234`; crypto_major avg `7.0462` n `8`; equity avg `1.2992` n `140`; fx avg `0.2706` n `6`; index avg `0.041` n `26`; metal avg `0.3682` n `20`; unknown avg `4.6321` n `719`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.158`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1573`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.148`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1442`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1436`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1408`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1366`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1266`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1235`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1227`, n `668`, weak_sample_signal
