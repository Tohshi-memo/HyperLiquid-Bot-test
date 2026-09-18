# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-18T18:52:29.975719+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0759` n `12`; crypto_alt avg `-0.034` n `234`; crypto_major avg `-0.239` n `8`; equity avg `0.1204` n `140`; fx avg `0.0083` n `6`; index avg `0.0265` n `26`; metal avg `-0.044` n `20`; unknown avg `43.2462` n `940`
- 1h: commodity avg `-0.0918` n `12`; crypto_alt avg `0.1899` n `234`; crypto_major avg `0.1253` n `8`; equity avg `0.0935` n `140`; fx avg `0.01` n `6`; index avg `0.0514` n `26`; metal avg `-0.063` n `20`; unknown avg `24.0858` n `938`
- 4h: commodity avg `-0.2155` n `12`; crypto_alt avg `0.4697` n `234`; crypto_major avg `0.0445` n `8`; equity avg `0.28` n `140`; fx avg `0.0083` n `6`; index avg `0.0511` n `26`; metal avg `0.0969` n `20`; unknown avg `17.8618` n `908`
- 24h: commodity avg `-0.2096` n `12`; crypto_alt avg `6.1481` n `234`; crypto_major avg `6.7243` n `8`; equity avg `0.8716` n `140`; fx avg `0.2015` n `6`; index avg `-0.0461` n `26`; metal avg `0.35` n `20`; unknown avg `12.3078` n `717`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1452`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1439`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1356`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1351`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.131`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1287`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1264`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1213`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1188`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.114`, n `668`, weak_sample_signal
