# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-21T03:22:28.194527+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0153` n `12`; crypto_alt avg `0.268` n `228`; crypto_major avg `0.3932` n `8`; equity avg `0.0587` n `78`; fx avg `-0.0036` n `6`; index avg `0.0251` n `23`; metal avg `0.012` n `18`; unknown avg `0.0586` n `702`
- 1h: commodity avg `0.0099` n `12`; crypto_alt avg `0.2622` n `228`; crypto_major avg `0.2667` n `8`; equity avg `0.0399` n `78`; fx avg `0.0997` n `6`; index avg `-0.0002` n `23`; metal avg `0.0254` n `18`; unknown avg `0.0224` n `702`
- 4h: commodity avg `0.0182` n `12`; crypto_alt avg `0.295` n `228`; crypto_major avg `0.0198` n `8`; equity avg `0.0318` n `78`; fx avg `-0.0073` n `6`; index avg `-0.0074` n `23`; metal avg `0.0043` n `18`; unknown avg `1.2102` n `701`
- 24h: commodity avg `0.186` n `12`; crypto_alt avg `1.8478` n `228`; crypto_major avg `1.879` n `8`; equity avg `0.4639` n `78`; fx avg `0.0325` n `6`; index avg `0.0146` n `23`; metal avg `0.022` n `18`; unknown avg `1.8211` n `557`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0813`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0797`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0739`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0736`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0634`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.06`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0594`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0584`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0561`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0548`, n `668`, weak_sample_signal
