# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-27T01:18:34.882334+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0381` n `12`; crypto_alt avg `-0.1058` n `230`; crypto_major avg `-0.1552` n `8`; equity avg `-0.2576` n `100`; fx avg `-0.0003` n `6`; index avg `-0.066` n `25`; metal avg `0.015` n `20`; unknown avg `0.0449` n `775`
- 1h: commodity avg `0.1763` n `12`; crypto_alt avg `-0.1422` n `230`; crypto_major avg `-0.1679` n `8`; equity avg `-0.2937` n `100`; fx avg `0.0431` n `6`; index avg `-0.1034` n `25`; metal avg `-0.0229` n `20`; unknown avg `-0.2173` n `775`
- 4h: commodity avg `-0.2501` n `12`; crypto_alt avg `0.6781` n `230`; crypto_major avg `0.5355` n `8`; equity avg `-0.0424` n `100`; fx avg `0.0716` n `6`; index avg `-0.0326` n `25`; metal avg `0.2189` n `20`; unknown avg `-0.2277` n `775`
- 24h: commodity avg `-0.4563` n `12`; crypto_alt avg `1.4626` n `230`; crypto_major avg `1.4191` n `8`; equity avg `0.4764` n `100`; fx avg `0.125` n `6`; index avg `0.0389` n `25`; metal avg `0.4413` n `20`; unknown avg `0.0218` n `758`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1662`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1478`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.146`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1357`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1203`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1058`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1057`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1006`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0997`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0952`, n `668`, weak_sample_signal
