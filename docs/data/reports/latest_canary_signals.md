# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-11T08:52:27.979697+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0124` n `12`; crypto_alt avg `0.0161` n `230`; crypto_major avg `0.0969` n `8`; equity avg `0.0909` n `113`; fx avg `-0.0014` n `6`; index avg `0.0199` n `25`; metal avg `0.0353` n `20`; unknown avg `0.0413` n `785`
- 1h: commodity avg `0.0263` n `12`; crypto_alt avg `0.1724` n `230`; crypto_major avg `0.1539` n `8`; equity avg `-0.2106` n `113`; fx avg `0.0083` n `6`; index avg `-0.0091` n `25`; metal avg `0.1988` n `20`; unknown avg `0.0145` n `785`
- 4h: commodity avg `0.3986` n `12`; crypto_alt avg `-0.344` n `230`; crypto_major avg `-0.0525` n `8`; equity avg `-0.5683` n `113`; fx avg `0.023` n `6`; index avg `-0.0868` n `25`; metal avg `-0.094` n `20`; unknown avg `0.037` n `753`
- 24h: commodity avg `1.0525` n `12`; crypto_alt avg `-1.2739` n `230`; crypto_major avg `-0.9326` n `8`; equity avg `-1.5924` n `113`; fx avg `0.019` n `6`; index avg `-0.0611` n `25`; metal avg `0.3057` n `20`; unknown avg `0.1037` n `752`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1756`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1728`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.17`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1669`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.142`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1408`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1193`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1187`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1092`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1086`, n `668`, weak_sample_signal
