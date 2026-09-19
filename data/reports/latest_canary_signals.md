# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-19T22:52:29.595119+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0002` n `12`; crypto_alt avg `0.3578` n `234`; crypto_major avg `0.1699` n `8`; equity avg `-0.0144` n `140`; fx avg `0.005` n `6`; index avg `-0.0002` n `26`; metal avg `0.0054` n `20`; unknown avg `4.1586` n `943`
- 1h: commodity avg `0.0238` n `12`; crypto_alt avg `0.4823` n `234`; crypto_major avg `0.1936` n `8`; equity avg `-0.02` n `140`; fx avg `0.0059` n `6`; index avg `-0.0097` n `26`; metal avg `0.0032` n `20`; unknown avg `4.491` n `933`
- 4h: commodity avg `0.0349` n `12`; crypto_alt avg `-0.1522` n `234`; crypto_major avg `-0.6007` n `8`; equity avg `0.0548` n `140`; fx avg `-0.0266` n `6`; index avg `0.0099` n `26`; metal avg `0.003` n `20`; unknown avg `55.4834` n `911`
- 24h: commodity avg `0.0767` n `12`; crypto_alt avg `1.0826` n `234`; crypto_major avg `-0.2153` n `8`; equity avg `0.0105` n `140`; fx avg `-0.0536` n `6`; index avg `0.0322` n `26`; metal avg `-0.0108` n `20`; unknown avg `6.0402` n `838`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1788`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1642`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.158`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1577`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1557`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1368`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1327`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1202`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1193`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1161`, n `668`, weak_sample_signal
