# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-21T19:52:26.379757+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0643` n `12`; crypto_alt avg `0.0072` n `228`; crypto_major avg `0.0651` n `8`; equity avg `-0.0011` n `78`; fx avg `-0.0159` n `6`; index avg `0.0046` n `23`; metal avg `-0.0151` n `18`; unknown avg `0.0055` n `702`
- 1h: commodity avg `-0.0208` n `12`; crypto_alt avg `0.0552` n `228`; crypto_major avg `0.1539` n `8`; equity avg `-0.0081` n `78`; fx avg `-0.0204` n `6`; index avg `0.0183` n `23`; metal avg `-0.0079` n `18`; unknown avg `0.2043` n `694`
- 4h: commodity avg `0.2188` n `12`; crypto_alt avg `-0.1226` n `228`; crypto_major avg `0.1577` n `8`; equity avg `-0.072` n `78`; fx avg `-0.1093` n `6`; index avg `0.0051` n `23`; metal avg `-0.0977` n `18`; unknown avg `-0.0371` n `694`
- 24h: commodity avg `0.3037` n `12`; crypto_alt avg `1.5862` n `228`; crypto_major avg `0.5272` n `8`; equity avg `0.3355` n `78`; fx avg `0.0936` n `6`; index avg `0.0159` n `23`; metal avg `-0.0762` n `18`; unknown avg `0.3547` n `645`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1018`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0965`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0888`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0822`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0791`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0786`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0726`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0721`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0665`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.064`, n `668`, weak_sample_signal
