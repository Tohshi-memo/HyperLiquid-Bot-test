# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-27T20:07:20.162122+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0711` n `12`; crypto_alt avg `0.0035` n `228`; crypto_major avg `0.1746` n `8`; equity avg `-0.0015` n `67`; fx avg `0.0021` n `6`; index avg `-0.0071` n `23`; metal avg `-0.0047` n `18`; unknown avg `-0.0827` n `419`
- 1h: commodity avg `0.0761` n `12`; crypto_alt avg `-0.0165` n `228`; crypto_major avg `0.2746` n `8`; equity avg `0.1085` n `67`; fx avg `0.0056` n `6`; index avg `-0.016` n `23`; metal avg `-0.0298` n `18`; unknown avg `0.0237` n `419`
- 4h: commodity avg `-0.5915` n `12`; crypto_alt avg `-0.7895` n `228`; crypto_major avg `-0.3084` n `8`; equity avg `0.4017` n `67`; fx avg `0.0337` n `6`; index avg `0.2914` n `23`; metal avg `0.1618` n `18`; unknown avg `-0.4927` n `418`
- 24h: commodity avg `-1.2308` n `12`; crypto_alt avg `-0.4629` n `228`; crypto_major avg `-0.1729` n `8`; equity avg `-0.027` n `67`; fx avg `-0.0697` n `6`; index avg `-0.4629` n `23`; metal avg `-1.2781` n `18`; unknown avg `-0.2615` n `400`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1691`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1675`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1573`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1565`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1541`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1439`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1433`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1422`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1298`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.129`, n `668`, weak_sample_signal
