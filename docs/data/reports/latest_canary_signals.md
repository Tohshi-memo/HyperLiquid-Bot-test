# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-27T16:22:23.598102+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.1362` - Commodity perps and crypto are moving differently; check macro-linked stress.

## Class Returns

- 15m: commodity avg `-0.0838` n `12`; crypto_alt avg `-0.4215` n `228`; crypto_major avg `-0.3258` n `8`; equity avg `0.0977` n `67`; fx avg `0.0115` n `6`; index avg `0.1986` n `23`; metal avg `0.1118` n `18`; unknown avg `-0.2429` n `418`
- 1h: commodity avg `-0.1699` n `12`; crypto_alt avg `-0.271` n `228`; crypto_major avg `-0.2668` n `8`; equity avg `0.2125` n `67`; fx avg `0.0122` n `6`; index avg `0.1981` n `23`; metal avg `0.2006` n `18`; unknown avg `-0.0771` n `418`
- 4h: commodity avg `0.9881` n `12`; crypto_alt avg `-0.2684` n `228`; crypto_major avg `-1.1481` n `8`; equity avg `-1.2308` n `67`; fx avg `-0.0208` n `6`; index avg `-0.9731` n `23`; metal avg `-0.4134` n `18`; unknown avg `-0.301` n `418`
- 24h: commodity avg `-1.203` n `12`; crypto_alt avg `-0.8732` n `228`; crypto_major avg `-1.1356` n `8`; equity avg `-0.2894` n `67`; fx avg `-0.0684` n `6`; index avg `-0.448` n `23`; metal avg `-0.9501` n `18`; unknown avg `0.0605` n `400`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1699`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.168`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1655`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1609`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1527`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.15`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1488`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1335`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1329`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1278`, n `668`, weak_sample_signal
