# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-17T13:22:28.295324+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.073` n `12`; crypto_alt avg `-0.0983` n `230`; crypto_major avg `-0.1303` n `8`; equity avg `-0.0776` n `114`; fx avg `0.0041` n `6`; index avg `-0.0033` n `25`; metal avg `-0.0694` n `20`; unknown avg `0.0002` n `792`
- 1h: commodity avg `0.1258` n `12`; crypto_alt avg `-0.1486` n `230`; crypto_major avg `-0.2741` n `8`; equity avg `-0.2095` n `114`; fx avg `0.0224` n `6`; index avg `-0.0243` n `25`; metal avg `-0.0703` n `20`; unknown avg `0.0195` n `792`
- 4h: commodity avg `0.1215` n `12`; crypto_alt avg `0.0509` n `230`; crypto_major avg `-0.049` n `8`; equity avg `-0.3429` n `114`; fx avg `0.0454` n `6`; index avg `-0.0248` n `25`; metal avg `-0.1092` n `20`; unknown avg `1.3196` n `792`
- 24h: commodity avg `-0.0005` n `12`; crypto_alt avg `-0.2464` n `230`; crypto_major avg `0.4437` n `8`; equity avg `0.9234` n `114`; fx avg `0.0185` n `6`; index avg `0.1079` n `25`; metal avg `0.0491` n `20`; unknown avg `-0.0234` n `775`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1666`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1628`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.143`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1399`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1151`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1106`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0923`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0758`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0749`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0742`, n `668`, weak_sample_signal
