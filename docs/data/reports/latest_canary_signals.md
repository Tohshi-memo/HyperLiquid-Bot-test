# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-22T22:52:25.673586+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0523` n `12`; crypto_alt avg `0.0735` n `230`; crypto_major avg `0.1474` n `8`; equity avg `-0.0032` n `98`; fx avg `-0.0006` n `6`; index avg `-0.0089` n `25`; metal avg `-0.0209` n `20`; unknown avg `0.1662` n `773`
- 1h: commodity avg `0.0888` n `12`; crypto_alt avg `-0.2048` n `230`; crypto_major avg `-0.0621` n `8`; equity avg `-0.1937` n `98`; fx avg `-0.0109` n `6`; index avg `-0.0478` n `25`; metal avg `-0.1204` n `20`; unknown avg `-0.0923` n `773`
- 4h: commodity avg `0.1437` n `12`; crypto_alt avg `-0.0242` n `230`; crypto_major avg `0.0308` n `8`; equity avg `0.0463` n `98`; fx avg `-0.0307` n `6`; index avg `-0.0637` n `25`; metal avg `-0.1557` n `20`; unknown avg `0.0132` n `773`
- 24h: commodity avg `0.6847` n `12`; crypto_alt avg `-0.2918` n `230`; crypto_major avg `-0.3872` n `8`; equity avg `-1.0868` n `98`; fx avg `-0.0554` n `6`; index avg `-0.1958` n `25`; metal avg `0.145` n `20`; unknown avg `1.6955` n `739`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1632`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1239`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.12`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1016`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1003`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0945`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0932`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0894`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0828`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0785`, n `666`, weak_sample_signal
