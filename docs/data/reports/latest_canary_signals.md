# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-17T14:27:27.196851+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0422` n `12`; crypto_alt avg `-0.0248` n `230`; crypto_major avg `-0.0058` n `8`; equity avg `0.1106` n `114`; fx avg `-0.002` n `6`; index avg `0.001` n `25`; metal avg `0.076` n `20`; unknown avg `-0.0174` n `792`
- 1h: commodity avg `-0.0068` n `12`; crypto_alt avg `0.0319` n `230`; crypto_major avg `0.1827` n `8`; equity avg `0.2762` n `114`; fx avg `-0.0043` n `6`; index avg `0.034` n `25`; metal avg `0.197` n `20`; unknown avg `0.0398` n `792`
- 4h: commodity avg `0.0249` n `12`; crypto_alt avg `0.215` n `230`; crypto_major avg `0.1654` n `8`; equity avg `-0.0921` n `114`; fx avg `0.0168` n `6`; index avg `0.0045` n `25`; metal avg `0.075` n `20`; unknown avg `1.9702` n `792`
- 24h: commodity avg `0.0001` n `12`; crypto_alt avg `-0.2961` n `230`; crypto_major avg `0.6196` n `8`; equity avg `1.1578` n `114`; fx avg `0.0282` n `6`; index avg `0.1443` n `25`; metal avg `0.2436` n `20`; unknown avg `0.0846` n `775`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1673`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1601`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1422`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.14`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1094`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1064`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0914`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0767`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0747`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0735`, n `668`, weak_sample_signal
