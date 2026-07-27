# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-27T04:37:30.725014+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0472` n `12`; crypto_alt avg `-0.1207` n `230`; crypto_major avg `-0.1234` n `8`; equity avg `-0.0587` n `100`; fx avg `-0.0062` n `6`; index avg `-0.0194` n `25`; metal avg `0.0206` n `20`; unknown avg `15.4592` n `775`
- 1h: commodity avg `-0.0915` n `12`; crypto_alt avg `0.0649` n `230`; crypto_major avg `0.2745` n `8`; equity avg `0.0718` n `100`; fx avg `-0.0016` n `6`; index avg `0.0164` n `25`; metal avg `0.0134` n `20`; unknown avg `0.8096` n `775`
- 4h: commodity avg `-0.0433` n `12`; crypto_alt avg `0.1216` n `230`; crypto_major avg `0.308` n `8`; equity avg `0.2021` n `100`; fx avg `0.0442` n `6`; index avg `-0.0333` n `25`; metal avg `-0.0987` n `20`; unknown avg `-0.4595` n `775`
- 24h: commodity avg `-0.5654` n `12`; crypto_alt avg `1.2175` n `230`; crypto_major avg `1.3292` n `8`; equity avg `0.785` n `100`; fx avg `0.0717` n `6`; index avg `0.0664` n `25`; metal avg `0.3248` n `20`; unknown avg `-0.0378` n `759`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1712`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.157`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.148`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.135`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1263`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1182`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1167`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1153`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1074`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0988`, n `668`, weak_sample_signal
