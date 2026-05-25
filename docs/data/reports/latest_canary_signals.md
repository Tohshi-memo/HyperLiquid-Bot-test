# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-25T00:22:18.994244+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.003` n `12`; crypto_alt avg `0.0622` n `228`; crypto_major avg `0.0177` n `8`; equity avg `0.0563` n `67`; fx avg `-0.02` n `6`; index avg `0.0661` n `23`; metal avg `-0.0371` n `18`; unknown avg `-0.1302` n `396`
- 1h: commodity avg `0.1114` n `12`; crypto_alt avg `0.5265` n `228`; crypto_major avg `0.2007` n `8`; equity avg `0.1456` n `67`; fx avg `-0.1039` n `6`; index avg `0.0691` n `23`; metal avg `-0.1478` n `18`; unknown avg `0.1581` n `396`
- 4h: commodity avg `-0.6493` n `12`; crypto_alt avg `0.2314` n `228`; crypto_major avg `0.2873` n `8`; equity avg `0.0052` n `67`; fx avg `-0.0675` n `6`; index avg `-0.0132` n `23`; metal avg `1.2773` n `18`; unknown avg `0.0337` n `396`
- 24h: commodity avg `0.5335` n `12`; crypto_alt avg `-1.1615` n `228`; crypto_major avg `0.725` n `8`; equity avg `0.4015` n `67`; fx avg `-0.0049` n `6`; index avg `-0.1461` n `23`; metal avg `0.9666` n `18`; unknown avg `-0.0813` n `386`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1359`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.128`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1259`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1179`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1173`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1173`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1171`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1081`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1056`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1054`, n `668`, weak_sample_signal
