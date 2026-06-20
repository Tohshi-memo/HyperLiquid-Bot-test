# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-20T16:07:26.413077+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0037` n `12`; crypto_alt avg `-0.0445` n `228`; crypto_major avg `-0.1057` n `8`; equity avg `-0.0256` n `78`; fx avg `0.0246` n `6`; index avg `-0.013` n `23`; metal avg `-0.0151` n `18`; unknown avg `0.1142` n `701`
- 1h: commodity avg `-0.0044` n `12`; crypto_alt avg `0.3317` n `228`; crypto_major avg `0.1337` n `8`; equity avg `0.0082` n `78`; fx avg `0.0222` n `6`; index avg `-0.0012` n `23`; metal avg `-0.0018` n `18`; unknown avg `0.0933` n `701`
- 4h: commodity avg `0.1646` n `12`; crypto_alt avg `0.2279` n `228`; crypto_major avg `-0.079` n `8`; equity avg `-0.0223` n `78`; fx avg `0.0309` n `6`; index avg `-0.0129` n `23`; metal avg `0.0046` n `18`; unknown avg `0.0466` n `701`
- 24h: commodity avg `0.5973` n `12`; crypto_alt avg `-2.7814` n `228`; crypto_major avg `-3.259` n `8`; equity avg `1.1538` n `78`; fx avg `-0.0344` n `6`; index avg `0.2781` n `23`; metal avg `-4.0893` n `18`; unknown avg `0.0868` n `492`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0846`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0844`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0803`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0642`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0633`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0607`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0587`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0576`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.057`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0564`, n `668`, weak_sample_signal
