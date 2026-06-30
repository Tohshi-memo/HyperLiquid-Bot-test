# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-30T11:37:28.885852+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0581` n `12`; crypto_alt avg `-0.2084` n `228`; crypto_major avg `-0.1064` n `8`; equity avg `-0.0767` n `88`; fx avg `-0.0073` n `6`; index avg `-0.0043` n `23`; metal avg `-0.0269` n `20`; unknown avg `0.1155` n `765`
- 1h: commodity avg `0.0276` n `12`; crypto_alt avg `-0.508` n `228`; crypto_major avg `-0.0553` n `8`; equity avg `0.1242` n `88`; fx avg `-0.0291` n `6`; index avg `0.0483` n `23`; metal avg `0.0411` n `20`; unknown avg `0.0742` n `765`
- 4h: commodity avg `0.2301` n `12`; crypto_alt avg `-0.8746` n `228`; crypto_major avg `-0.4568` n `8`; equity avg `-0.1247` n `88`; fx avg `-0.02` n `6`; index avg `-0.0167` n `23`; metal avg `0.0659` n `20`; unknown avg `-0.0812` n `765`
- 24h: commodity avg `0.1393` n `12`; crypto_alt avg `-1.2732` n `228`; crypto_major avg `0.1835` n `8`; equity avg `1.356` n `88`; fx avg `0.1181` n `6`; index avg `0.148` n `23`; metal avg `0.3533` n `20`; unknown avg `9.203` n `734`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1211`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0907`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0893`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0856`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0833`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0638`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0595`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.058`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.056`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0512`, n `668`, weak_sample_signal
