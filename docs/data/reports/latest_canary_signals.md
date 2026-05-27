# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-27T02:07:17.615149+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1652` n `12`; crypto_alt avg `-0.4952` n `228`; crypto_major avg `-0.2578` n `8`; equity avg `0.0018` n `67`; fx avg `0.0012` n `6`; index avg `-0.0148` n `23`; metal avg `-0.0603` n `18`; unknown avg `-0.2265` n `418`
- 1h: commodity avg `-0.1694` n `12`; crypto_alt avg `-0.7669` n `228`; crypto_major avg `-0.4119` n `8`; equity avg `0.0435` n `67`; fx avg `-0.0049` n `6`; index avg `-0.0011` n `23`; metal avg `-0.3155` n `18`; unknown avg `0.1247` n `418`
- 4h: commodity avg `-0.3095` n `12`; crypto_alt avg `-0.0655` n `228`; crypto_major avg `0.2499` n `8`; equity avg `0.1933` n `67`; fx avg `-0.0265` n `6`; index avg `0.1818` n `23`; metal avg `-0.234` n `18`; unknown avg `-0.3134` n `418`
- 24h: commodity avg `-0.0881` n `12`; crypto_alt avg `-0.2745` n `228`; crypto_major avg `-0.2811` n `8`; equity avg `0.8575` n `67`; fx avg `-0.0347` n `6`; index avg `0.9693` n `23`; metal avg `-0.1146` n `18`; unknown avg `0.5681` n `397`

## Correlations

- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1829`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1809`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1707`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.168`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1625`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1606`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.153`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1423`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.135`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1343`, n `668`, weak_sample_signal
