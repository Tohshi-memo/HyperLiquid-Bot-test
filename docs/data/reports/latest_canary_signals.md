# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-19T20:37:30.420055+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0091` n `12`; crypto_alt avg `-0.1523` n `234`; crypto_major avg `-0.1088` n `8`; equity avg `-0.0055` n `140`; fx avg `-0.0114` n `6`; index avg `-0.0064` n `26`; metal avg `-0.002` n `20`; unknown avg `0.9165` n `943`
- 1h: commodity avg `0.0118` n `12`; crypto_alt avg `-0.1329` n `234`; crypto_major avg `-0.173` n `8`; equity avg `0.0424` n `140`; fx avg `-0.0479` n `6`; index avg `-0.0066` n `26`; metal avg `0.0045` n `20`; unknown avg `-0.0272` n `919`
- 4h: commodity avg `0.078` n `12`; crypto_alt avg `-0.2328` n `234`; crypto_major avg `-0.5543` n `8`; equity avg `0.1014` n `140`; fx avg `-0.0531` n `6`; index avg `0.0031` n `26`; metal avg `0.0151` n `20`; unknown avg `159.5788` n `879`
- 24h: commodity avg `0.068` n `12`; crypto_alt avg `1.4454` n `234`; crypto_major avg `0.3059` n `8`; equity avg `0.0096` n `140`; fx avg `-0.0598` n `6`; index avg `-0.0128` n `26`; metal avg `-0.0346` n `20`; unknown avg `6.8574` n `820`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1737`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1699`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1688`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1549`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1496`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1417`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1311`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1254`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1175`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1099`, n `668`, weak_sample_signal
