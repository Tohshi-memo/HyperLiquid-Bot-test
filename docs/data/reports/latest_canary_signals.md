# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-22T12:22:34.200629+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0912` n `12`; crypto_alt avg `0.1841` n `234`; crypto_major avg `0.0931` n `8`; equity avg `0.0468` n `140`; fx avg `0.0289` n `6`; index avg `-0.007` n `26`; metal avg `0.099` n `20`; unknown avg `0.1701` n `944`
- 1h: commodity avg `0.053` n `12`; crypto_alt avg `0.119` n `234`; crypto_major avg `0.0911` n `8`; equity avg `-0.0716` n `140`; fx avg `0.0366` n `6`; index avg `-0.0063` n `26`; metal avg `0.1802` n `20`; unknown avg `2.9921` n `936`
- 4h: commodity avg `-0.4033` n `12`; crypto_alt avg `-0.1888` n `234`; crypto_major avg `0.4631` n `8`; equity avg `0.6533` n `140`; fx avg `-0.0649` n `6`; index avg `0.1048` n `26`; metal avg `0.3491` n `20`; unknown avg `2.2421` n `934`
- 24h: commodity avg `-0.4246` n `12`; crypto_alt avg `0.1319` n `234`; crypto_major avg `1.2877` n `8`; equity avg `0.813` n `140`; fx avg `-0.2579` n `6`; index avg `0.2218` n `26`; metal avg `-0.1222` n `20`; unknown avg `1108.3936` n `802`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.1467`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1398`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1264`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1189`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1113`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.105`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0996`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.095`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0928`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0923`, n `668`, weak_sample_signal
