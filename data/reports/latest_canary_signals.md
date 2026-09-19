# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-19T14:52:25.819294+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0805` n `12`; crypto_alt avg `-0.1451` n `234`; crypto_major avg `-0.083` n `8`; equity avg `0.0067` n `140`; fx avg `0.0083` n `6`; index avg `0.0002` n `26`; metal avg `0.012` n `20`; unknown avg `0.5903` n `942`
- 1h: commodity avg `-0.0749` n `12`; crypto_alt avg `0.179` n `234`; crypto_major avg `0.2067` n `8`; equity avg `0.01` n `140`; fx avg `0.0067` n `6`; index avg `-0.0002` n `26`; metal avg `0.0206` n `20`; unknown avg `0.6765` n `940`
- 4h: commodity avg `-0.0668` n `12`; crypto_alt avg `0.3439` n `234`; crypto_major avg `0.58` n `8`; equity avg `0.0581` n `140`; fx avg `-0.0256` n `6`; index avg `0.0067` n `26`; metal avg `0.0209` n `20`; unknown avg `1.0462` n `932`
- 24h: commodity avg `-0.1504` n `12`; crypto_alt avg `2.7747` n `234`; crypto_major avg `1.1848` n `8`; equity avg `0.6562` n `140`; fx avg `0.0334` n `6`; index avg `0.1189` n `26`; metal avg `0.0561` n `20`; unknown avg `2.102` n `806`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1749`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1722`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1675`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.155`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1478`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1472`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1383`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1318`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1247`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1179`, n `668`, weak_sample_signal
