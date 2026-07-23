# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-23T00:52:31.778744+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0209` n `12`; crypto_alt avg `0.0097` n `230`; crypto_major avg `-0.0404` n `8`; equity avg `0.0491` n `98`; fx avg `-0.0062` n `6`; index avg `0.0227` n `25`; metal avg `-0.0039` n `20`; unknown avg `0.0942` n `773`
- 1h: commodity avg `0.0585` n `12`; crypto_alt avg `0.2844` n `230`; crypto_major avg `0.204` n `8`; equity avg `0.374` n `98`; fx avg `-0.0331` n `6`; index avg `0.1104` n `25`; metal avg `0.0388` n `20`; unknown avg `-0.1414` n `773`
- 4h: commodity avg `0.2685` n `12`; crypto_alt avg `0.0937` n `230`; crypto_major avg `0.337` n `8`; equity avg `0.3983` n `98`; fx avg `-0.0483` n `6`; index avg `0.1145` n `25`; metal avg `-0.0126` n `20`; unknown avg `0.0512` n `773`
- 24h: commodity avg `0.7452` n `12`; crypto_alt avg `-0.507` n `230`; crypto_major avg `-0.6909` n `8`; equity avg `-0.7635` n `98`; fx avg `-0.0853` n `6`; index avg `-0.0395` n `25`; metal avg `0.1568` n `20`; unknown avg `1.733` n `739`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1596`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1155`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1108`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1003`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1002`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0936`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0807`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0805`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0783`, n `666`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0646`, n `666`, weak_sample_signal
