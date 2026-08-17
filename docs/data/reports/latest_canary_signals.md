# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-17T02:52:26.923579+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0523` n `12`; crypto_alt avg `0.1367` n `230`; crypto_major avg `0.2594` n `8`; equity avg `0.2293` n `114`; fx avg `0.0282` n `6`; index avg `0.0119` n `25`; metal avg `-0.0123` n `20`; unknown avg `0.044` n `792`
- 1h: commodity avg `-0.0046` n `12`; crypto_alt avg `0.3763` n `230`; crypto_major avg `0.4204` n `8`; equity avg `0.4211` n `114`; fx avg `0.037` n `6`; index avg `0.0252` n `25`; metal avg `-0.0105` n `20`; unknown avg `0.1412` n `792`
- 4h: commodity avg `-0.0045` n `12`; crypto_alt avg `0.8849` n `230`; crypto_major avg `1.204` n `8`; equity avg `0.5336` n `114`; fx avg `-0.0125` n `6`; index avg `0.0158` n `25`; metal avg `0.1134` n `20`; unknown avg `1.0734` n `791`
- 24h: commodity avg `-0.0776` n `12`; crypto_alt avg `0.4485` n `230`; crypto_major avg `0.6777` n `8`; equity avg `0.7384` n `114`; fx avg `-0.0222` n `6`; index avg `0.0592` n `25`; metal avg `0.206` n `20`; unknown avg `0.1093` n `759`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.1875`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1717`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1476`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1451`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.14`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1295`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1279`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.12`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1054`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0932`, n `668`, weak_sample_signal
