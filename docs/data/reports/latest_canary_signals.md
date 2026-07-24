# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-24T06:07:33.374276+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0763` n `12`; crypto_alt avg `0.0472` n `230`; crypto_major avg `0.0678` n `8`; equity avg `-0.1393` n `100`; fx avg `-0.0104` n `6`; index avg `-0.0607` n `25`; metal avg `-0.0185` n `20`; unknown avg `0.0075` n `756`
- 1h: commodity avg `-0.1147` n `12`; crypto_alt avg `-0.0258` n `230`; crypto_major avg `0.0191` n `8`; equity avg `-0.2396` n `100`; fx avg `-0.0068` n `6`; index avg `-0.0643` n `25`; metal avg `-0.0535` n `20`; unknown avg `-0.026` n `756`
- 4h: commodity avg `-0.12` n `12`; crypto_alt avg `0.2521` n `230`; crypto_major avg `0.2357` n `8`; equity avg `-0.4317` n `100`; fx avg `0.0001` n `6`; index avg `-0.118` n `25`; metal avg `-0.1354` n `20`; unknown avg `0.1775` n `756`
- 24h: commodity avg `0.3374` n `12`; crypto_alt avg `-0.9514` n `230`; crypto_major avg `-1.5392` n `8`; equity avg `-2.0513` n `99`; fx avg `-0.1273` n `6`; index avg `-0.5788` n `25`; metal avg `-0.9919` n `20`; unknown avg `-0.0191` n `756`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1807`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1714`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1499`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1057`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1046`, n `666`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0985`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0953`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0899`, n `666`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0863`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0861`, n `666`, weak_sample_signal
