# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-28T15:37:33.540452+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0228` n `12`; crypto_alt avg `-0.1352` n `228`; crypto_major avg `-0.0756` n `8`; equity avg `-0.0174` n `88`; fx avg `0.0` n `6`; index avg `0.0017` n `23`; metal avg `-0.0076` n `20`; unknown avg `-0.1347` n `764`
- 1h: commodity avg `0.0054` n `12`; crypto_alt avg `-0.2582` n `228`; crypto_major avg `-0.1894` n `8`; equity avg `-0.0371` n `88`; fx avg `0.0119` n `6`; index avg `0.0004` n `23`; metal avg `-0.0324` n `20`; unknown avg `-0.1205` n `764`
- 4h: commodity avg `0.053` n `12`; crypto_alt avg `0.3359` n `228`; crypto_major avg `-0.1098` n `8`; equity avg `0.0023` n `88`; fx avg `0.0018` n `6`; index avg `0.02` n `23`; metal avg `-0.0551` n `20`; unknown avg `2.5069` n `764`
- 24h: commodity avg `0.207` n `12`; crypto_alt avg `-0.7381` n `228`; crypto_major avg `-1.808` n `8`; equity avg `-0.039` n `88`; fx avg `-0.0097` n `6`; index avg `-0.0509` n `23`; metal avg `-0.0884` n `20`; unknown avg `15.6161` n `690`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1933`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1851`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1361`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1269`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.095`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.095`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0925`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0888`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.087`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.085`, n `668`, weak_sample_signal
