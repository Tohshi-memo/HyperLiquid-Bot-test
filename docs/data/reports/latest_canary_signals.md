# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-13T08:07:28.577789+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.095` n `12`; crypto_alt avg `0.1523` n `230`; crypto_major avg `0.1065` n `8`; equity avg `0.1121` n `92`; fx avg `-0.0163` n `6`; index avg `0.0309` n `25`; metal avg `0.1309` n `20`; unknown avg `0.0079` n `766`
- 1h: commodity avg `-0.1441` n `12`; crypto_alt avg `0.2927` n `230`; crypto_major avg `0.2852` n `8`; equity avg `0.1674` n `92`; fx avg `-0.0398` n `6`; index avg `0.0536` n `25`; metal avg `0.1985` n `20`; unknown avg `0.0453` n `766`
- 4h: commodity avg `-0.1943` n `12`; crypto_alt avg `1.0164` n `230`; crypto_major avg `0.3353` n `8`; equity avg `0.0773` n `92`; fx avg `-0.0623` n `6`; index avg `0.0359` n `25`; metal avg `0.2967` n `20`; unknown avg `0.0181` n `750`
- 24h: commodity avg `-0.2138` n `12`; crypto_alt avg `-1.0583` n `230`; crypto_major avg `-0.9512` n `8`; equity avg `-2.2299` n `92`; fx avg `-0.0187` n `6`; index avg `-0.4599` n `25`; metal avg `-0.1936` n `20`; unknown avg `-0.0383` n `743`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1888`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1731`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1307`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1161`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1051`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0999`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0991`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0991`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0893`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0884`, n `668`, weak_sample_signal
