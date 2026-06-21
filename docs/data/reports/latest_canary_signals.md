# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-21T01:07:26.302518+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0196` n `12`; crypto_alt avg `0.0232` n `228`; crypto_major avg `-0.018` n `8`; equity avg `0.0186` n `78`; fx avg `0.0007` n `6`; index avg `0.0173` n `23`; metal avg `-0.0086` n `18`; unknown avg `0.2208` n `701`
- 1h: commodity avg `0.0255` n `12`; crypto_alt avg `0.1637` n `228`; crypto_major avg `-0.0531` n `8`; equity avg `0.0213` n `78`; fx avg `0.1224` n `6`; index avg `0.0053` n `23`; metal avg `-0.0217` n `18`; unknown avg `0.0647` n `701`
- 4h: commodity avg `0.0467` n `12`; crypto_alt avg `0.869` n `228`; crypto_major avg `0.5003` n `8`; equity avg `0.1143` n `78`; fx avg `-0.0002` n `6`; index avg `0.0254` n `23`; metal avg `-0.0317` n `18`; unknown avg `0.3325` n `701`
- 24h: commodity avg `0.3667` n `12`; crypto_alt avg `1.2812` n `228`; crypto_major avg `1.587` n `8`; equity avg `0.432` n `78`; fx avg `0.0501` n `6`; index avg `0.0278` n `23`; metal avg `-0.0682` n `18`; unknown avg `-0.0466` n `557`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0852`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0846`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0805`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0768`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0687`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0667`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0623`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.058`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0557`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0552`, n `668`, weak_sample_signal
