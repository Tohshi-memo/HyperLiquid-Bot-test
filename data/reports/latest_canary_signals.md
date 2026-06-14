# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-14T21:07:31.801743+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0029` n `12`; crypto_alt avg `0.0449` n `228`; crypto_major avg `-0.0719` n `8`; equity avg `0.0493` n `74`; fx avg `0.0267` n `6`; index avg `0.0133` n `23`; metal avg `-0.0381` n `18`; unknown avg `-0.1045` n `645`
- 1h: commodity avg `-0.1981` n `12`; crypto_alt avg `0.5019` n `228`; crypto_major avg `0.3126` n `8`; equity avg `0.1226` n `74`; fx avg `0.0108` n `6`; index avg `0.0078` n `23`; metal avg `0.0564` n `18`; unknown avg `-0.0386` n `645`
- 4h: commodity avg `0.0587` n `12`; crypto_alt avg `0.2343` n `228`; crypto_major avg `0.2008` n `8`; equity avg `0.0924` n `74`; fx avg `-0.0038` n `6`; index avg `-0.014` n `23`; metal avg `0.0038` n `18`; unknown avg `0.0519` n `645`
- 24h: commodity avg `-0.1174` n `12`; crypto_alt avg `-0.7633` n `228`; crypto_major avg `-0.3446` n `8`; equity avg `0.321` n `74`; fx avg `-0.0572` n `6`; index avg `0.1145` n `23`; metal avg `0.1452` n `18`; unknown avg `1.0987` n `592`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1599`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1262`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1057`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0994`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0994`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0905`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0789`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0687`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0663`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0633`, n `668`, weak_sample_signal
