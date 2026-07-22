# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-22T18:22:33.759998+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.048` n `12`; crypto_alt avg `-0.1606` n `230`; crypto_major avg `-0.1865` n `8`; equity avg `-0.156` n `98`; fx avg `0.0042` n `6`; index avg `-0.019` n `25`; metal avg `-0.0329` n `20`; unknown avg `0.0221` n `773`
- 1h: commodity avg `0.0557` n `12`; crypto_alt avg `-0.2418` n `230`; crypto_major avg `-0.0155` n `8`; equity avg `-0.5102` n `98`; fx avg `0.0081` n `6`; index avg `-0.0666` n `25`; metal avg `-0.0584` n `20`; unknown avg `0.0714` n `773`
- 4h: commodity avg `0.0921` n `12`; crypto_alt avg `-0.0332` n `230`; crypto_major avg `0.3116` n `8`; equity avg `-0.421` n `98`; fx avg `0.0023` n `6`; index avg `-0.0084` n `25`; metal avg `-0.1924` n `20`; unknown avg `-0.0916` n `773`
- 24h: commodity avg `0.6822` n `12`; crypto_alt avg `-0.2805` n `230`; crypto_major avg `-0.597` n `8`; equity avg `-0.6281` n `98`; fx avg `-0.0339` n `6`; index avg `-0.1321` n `25`; metal avg `0.2975` n `20`; unknown avg `0.799` n `739`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1697`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1262`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1132`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.108`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0973`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0917`, n `666`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0829`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0739`, n `666`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0739`, n `666`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0736`, n `668`, weak_sample_signal
