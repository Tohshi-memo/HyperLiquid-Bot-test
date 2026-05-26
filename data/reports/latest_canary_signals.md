# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-26T00:37:14.042235+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0646` n `12`; crypto_alt avg `-0.2623` n `228`; crypto_major avg `-0.2314` n `8`; equity avg `0.1943` n `67`; fx avg `-0.0497` n `6`; index avg `0.0727` n `23`; metal avg `0.2525` n `18`; unknown avg `-0.0636` n `407`
- 1h: commodity avg `0.1892` n `12`; crypto_alt avg `-0.5725` n `228`; crypto_major avg `-0.4785` n `8`; equity avg `-0.3313` n `67`; fx avg `-0.0311` n `6`; index avg `-0.139` n `23`; metal avg `-0.037` n `18`; unknown avg `-0.2869` n `405`
- 4h: commodity avg `0.319` n `12`; crypto_alt avg `-1.1729` n `228`; crypto_major avg `-0.7192` n `8`; equity avg `-0.6337` n `67`; fx avg `-0.0317` n `6`; index avg `-0.3814` n `23`; metal avg `-0.4243` n `18`; unknown avg `-0.4792` n `405`
- 24h: commodity avg `-0.1204` n `12`; crypto_alt avg `0.5983` n `228`; crypto_major avg `-0.702` n `8`; equity avg `0.1461` n `67`; fx avg `-0.0312` n `6`; index avg `0.2232` n `23`; metal avg `-0.0594` n `18`; unknown avg `0.6871` n `386`

## Correlations

- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.176`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1683`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1682`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1616`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1481`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.145`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1428`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1314`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.128`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1248`, n `668`, weak_sample_signal
