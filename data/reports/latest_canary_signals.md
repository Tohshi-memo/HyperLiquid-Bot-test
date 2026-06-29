# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-29T04:52:36.334069+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0134` n `12`; crypto_alt avg `-0.076` n `228`; crypto_major avg `-0.0983` n `8`; equity avg `0.0221` n `88`; fx avg `-0.0047` n `6`; index avg `0.0309` n `23`; metal avg `-0.022` n `20`; unknown avg `0.5703` n `764`
- 1h: commodity avg `-0.033` n `12`; crypto_alt avg `-0.4714` n `228`; crypto_major avg `-0.5357` n `8`; equity avg `-0.177` n `88`; fx avg `-0.0015` n `6`; index avg `-0.0284` n `23`; metal avg `-0.2396` n `20`; unknown avg `6.6887` n `764`
- 4h: commodity avg `0.0073` n `12`; crypto_alt avg `0.8102` n `228`; crypto_major avg `0.5264` n `8`; equity avg `0.2704` n `88`; fx avg `0.0591` n `6`; index avg `0.0517` n `23`; metal avg `-0.068` n `20`; unknown avg `-0.4883` n `764`
- 24h: commodity avg `-0.2738` n `12`; crypto_alt avg `-0.2342` n `228`; crypto_major avg `-0.2772` n `8`; equity avg `-0.0397` n `88`; fx avg `0.0399` n `6`; index avg `-0.0677` n `23`; metal avg `-0.3128` n `20`; unknown avg `-1.0433` n `722`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1902`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1626`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.113`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1101`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1091`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1025`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0951`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0947`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0947`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0871`, n `668`, weak_sample_signal
