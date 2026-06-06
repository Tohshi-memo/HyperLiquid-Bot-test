# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-06T14:22:22.547299+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0483` n `12`; crypto_alt avg `0.2574` n `228`; crypto_major avg `0.1433` n `8`; equity avg `0.1106` n `74`; fx avg `-0.0002` n `6`; index avg `0.1234` n `23`; metal avg `-0.1014` n `18`; unknown avg `0.171` n `515`
- 1h: commodity avg `0.0584` n `12`; crypto_alt avg `0.2637` n `228`; crypto_major avg `0.0413` n `8`; equity avg `-0.0499` n `74`; fx avg `-0.0012` n `6`; index avg `0.0889` n `23`; metal avg `-0.1993` n `18`; unknown avg `0.6447` n `513`
- 4h: commodity avg `0.1931` n `12`; crypto_alt avg `1.4615` n `228`; crypto_major avg `0.8431` n `8`; equity avg `0.9685` n `74`; fx avg `0.0057` n `6`; index avg `0.6618` n `23`; metal avg `-0.0686` n `18`; unknown avg `0.0443` n `411`
- 24h: commodity avg `-0.4571` n `12`; crypto_alt avg `-1.9822` n `228`; crypto_major avg `-1.8182` n `8`; equity avg `-4.0023` n `74`; fx avg `-0.1685` n `6`; index avg `-2.1831` n `23`; metal avg `-2.0776` n `18`; unknown avg `0.0557` n `400`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.1201`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1141`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.08`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.079`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0789`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0745`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0729`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0692`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0643`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0621`, n `668`, weak_sample_signal
