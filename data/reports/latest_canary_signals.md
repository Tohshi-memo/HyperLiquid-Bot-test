# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-03T18:39:23.338002+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0425` n `13`; crypto_alt avg `0.0544` n `239`; crypto_major avg `-0.0059` n `8`; equity avg `0.0721` n `158`; fx avg `0.0058` n `6`; index avg `0.0169` n `27`; metal avg `-0.0195` n `20`; unknown avg `-0.2452` n `1263`
- 1h: commodity avg `0.017` n `13`; crypto_alt avg `0.0767` n `239`; crypto_major avg `0.102` n `8`; equity avg `0.0829` n `158`; fx avg `0.0121` n `6`; index avg `0.0382` n `27`; metal avg `0.0218` n `20`; unknown avg `-0.2593` n `1219`
- 4h: commodity avg `0.1184` n `13`; crypto_alt avg `0.0072` n `239`; crypto_major avg `0.098` n `8`; equity avg `0.1936` n `158`; fx avg `0.0578` n `6`; index avg `0.0052` n `27`; metal avg `-0.1903` n `20`; unknown avg `0.0143` n `1215`
- 24h: commodity avg `0.208` n `13`; crypto_alt avg `0.9435` n `239`; crypto_major avg `1.5578` n `8`; equity avg `0.3688` n `158`; fx avg `0.0903` n `6`; index avg `0.0119` n `27`; metal avg `-0.5721` n `20`; unknown avg `374.6304` n `1049`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1436`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1409`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1406`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1386`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1385`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1377`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1307`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1151`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1146`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1144`, n `668`, weak_sample_signal
