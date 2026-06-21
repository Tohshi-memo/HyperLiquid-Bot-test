# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-21T14:22:25.951423+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0275` n `12`; crypto_alt avg `-0.1135` n `228`; crypto_major avg `-0.0959` n `8`; equity avg `-0.0091` n `78`; fx avg `0.0068` n `6`; index avg `-0.0` n `23`; metal avg `-0.0142` n `18`; unknown avg `-0.0859` n `702`
- 1h: commodity avg `0.1379` n `12`; crypto_alt avg `-0.1332` n `228`; crypto_major avg `-0.0683` n `8`; equity avg `-0.0698` n `78`; fx avg `0.125` n `6`; index avg `0.0086` n `23`; metal avg `-0.0273` n `18`; unknown avg `-0.0596` n `702`
- 4h: commodity avg `0.0732` n `12`; crypto_alt avg `-0.2876` n `228`; crypto_major avg `-0.4895` n `8`; equity avg `-0.093` n `78`; fx avg `0.0495` n `6`; index avg `-0.0075` n `23`; metal avg `-0.07` n `18`; unknown avg `0.1194` n `702`
- 24h: commodity avg `-0.1023` n `12`; crypto_alt avg `2.5297` n `228`; crypto_major avg `0.7606` n `8`; equity avg `0.606` n `78`; fx avg `0.0506` n `6`; index avg `0.0539` n `23`; metal avg `-0.019` n `18`; unknown avg `1.3445` n `653`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0759`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0648`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0643`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0623`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0572`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0566`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.056`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0557`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0554`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0544`, n `668`, weak_sample_signal
