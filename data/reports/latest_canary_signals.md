# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-20T09:52:25.871392+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0033` n `12`; crypto_alt avg `0.0997` n `228`; crypto_major avg `0.0184` n `8`; equity avg `0.0226` n `78`; fx avg `-0.0005` n `6`; index avg `0.0098` n `23`; metal avg `0.0052` n `18`; unknown avg `-0.0717` n `687`
- 1h: commodity avg `0.0073` n `12`; crypto_alt avg `0.4596` n `228`; crypto_major avg `0.3496` n `8`; equity avg `0.0217` n `78`; fx avg `0.0054` n `6`; index avg `0.0368` n `23`; metal avg `0.0099` n `18`; unknown avg `-0.1016` n `687`
- 4h: commodity avg `0.0285` n `12`; crypto_alt avg `0.5289` n `228`; crypto_major avg `0.3743` n `8`; equity avg `-0.0889` n `78`; fx avg `0.0157` n `6`; index avg `-0.0358` n `23`; metal avg `0.0132` n `18`; unknown avg `-0.1367` n `639`
- 24h: commodity avg `0.5105` n `12`; crypto_alt avg `-2.7836` n `228`; crypto_major avg `-3.27` n `8`; equity avg `1.2256` n `78`; fx avg `-0.0924` n `6`; index avg `0.3076` n `23`; metal avg `-4.1036` n `18`; unknown avg `-0.023` n `530`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0971`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0954`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0881`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0752`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0617`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0574`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0568`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0556`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0527`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0522`, n `668`, weak_sample_signal
