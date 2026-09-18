# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-18T20:22:28.256840+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0298` n `12`; crypto_alt avg `0.1487` n `234`; crypto_major avg `0.0386` n `8`; equity avg `0.0045` n `140`; fx avg `0.0086` n `6`; index avg `0.0091` n `26`; metal avg `0.0247` n `20`; unknown avg `15.8654` n `922`
- 1h: commodity avg `0.0054` n `12`; crypto_alt avg `0.1525` n `234`; crypto_major avg `0.1375` n `8`; equity avg `0.3179` n `140`; fx avg `0.0161` n `6`; index avg `0.0806` n `26`; metal avg `0.009` n `20`; unknown avg `57.9984` n `898`
- 4h: commodity avg `-0.222` n `12`; crypto_alt avg `0.9049` n `234`; crypto_major avg `0.8655` n `8`; equity avg `0.9016` n `140`; fx avg `0.0151` n `6`; index avg `0.1923` n `26`; metal avg `0.0473` n `20`; unknown avg `8.5189` n `880`
- 24h: commodity avg `-0.0883` n `12`; crypto_alt avg `6.6279` n `234`; crypto_major avg `6.9768` n `8`; equity avg `1.331` n `140`; fx avg `0.2153` n `6`; index avg `0.0624` n `26`; metal avg `0.4173` n `20`; unknown avg `1944.0353` n `731`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1543`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1491`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1464`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1439`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1404`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1402`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1368`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1242`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1224`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1197`, n `668`, weak_sample_signal
