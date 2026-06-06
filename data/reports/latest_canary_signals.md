# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-06T01:33:40.356034+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0172` n `12`; crypto_alt avg `0.7321` n `228`; crypto_major avg `0.7448` n `8`; equity avg `-0.0938` n `74`; fx avg `-0.0128` n `6`; index avg `-0.1275` n `23`; metal avg `-0.0035` n `18`; unknown avg `0.2729` n `425`
- 1h: commodity avg `-0.0799` n `12`; crypto_alt avg `0.0963` n `228`; crypto_major avg `0.2018` n `8`; equity avg `-0.4582` n `74`; fx avg `-0.0223` n `6`; index avg `-0.2041` n `23`; metal avg `0.0017` n `18`; unknown avg `-0.0492` n `425`
- 4h: commodity avg `0.6851` n `12`; crypto_alt avg `-0.6621` n `228`; crypto_major avg `-0.3982` n `8`; equity avg `-0.8039` n `74`; fx avg `-0.0335` n `6`; index avg `-0.1365` n `23`; metal avg `-0.1523` n `18`; unknown avg `1.2007` n `425`
- 24h: commodity avg `-1.0457` n `12`; crypto_alt avg `-5.818` n `228`; crypto_major avg `-4.9852` n `8`; equity avg `-5.6618` n `74`; fx avg `-0.2176` n `6`; index avg `-3.5969` n `23`; metal avg `-3.8192` n `18`; unknown avg `-0.5214` n `404`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1268`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1204`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0922`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0909`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0757`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0741`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0737`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0724`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0708`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0619`, n `668`, weak_sample_signal
