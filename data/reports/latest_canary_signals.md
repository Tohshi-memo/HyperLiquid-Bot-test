# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-15T17:52:23.743921+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0011` n `12`; crypto_alt avg `-0.0055` n `230`; crypto_major avg `0.0122` n `8`; equity avg `0.0057` n `114`; fx avg `0.0065` n `6`; index avg `0.0033` n `25`; metal avg `0.0021` n `20`; unknown avg `0.0363` n `791`
- 1h: commodity avg `0.028` n `12`; crypto_alt avg `0.0351` n `230`; crypto_major avg `-0.043` n `8`; equity avg `0.0385` n `114`; fx avg `0.0001` n `6`; index avg `0.0097` n `25`; metal avg `0.0044` n `20`; unknown avg `0.0583` n `791`
- 4h: commodity avg `0.0234` n `12`; crypto_alt avg `0.365` n `230`; crypto_major avg `0.1748` n `8`; equity avg `0.0457` n `114`; fx avg `-0.0057` n `6`; index avg `0.0082` n `25`; metal avg `-0.0034` n `20`; unknown avg `-0.0023` n `791`
- 24h: commodity avg `-0.1227` n `12`; crypto_alt avg `0.8626` n `230`; crypto_major avg `0.4669` n `8`; equity avg `0.2949` n `114`; fx avg `0.0414` n `6`; index avg `0.0535` n `25`; metal avg `0.0433` n `20`; unknown avg `0.02` n `759`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2182`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.2125`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1835`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1781`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1582`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1562`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1474`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1468`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1461`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1437`, n `668`, weak_sample_signal
