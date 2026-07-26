# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-26T11:07:32.915677+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0136` n `12`; crypto_alt avg `-0.0267` n `230`; crypto_major avg `-0.0002` n `8`; equity avg `0.0153` n `100`; fx avg `0.0015` n `6`; index avg `-0.0018` n `25`; metal avg `0.0209` n `20`; unknown avg `-0.0015` n `775`
- 1h: commodity avg `0.0493` n `12`; crypto_alt avg `0.0184` n `230`; crypto_major avg `0.0053` n `8`; equity avg `0.1539` n `100`; fx avg `0.0096` n `6`; index avg `0.0319` n `25`; metal avg `0.0721` n `20`; unknown avg `0.0704` n `775`
- 4h: commodity avg `-0.3326` n `12`; crypto_alt avg `-0.1285` n `230`; crypto_major avg `-0.0488` n `8`; equity avg `0.1612` n `100`; fx avg `-0.039` n `6`; index avg `0.0554` n `25`; metal avg `0.1447` n `20`; unknown avg `-0.0364` n `775`
- 24h: commodity avg `-0.8303` n `12`; crypto_alt avg `1.4566` n `230`; crypto_major avg `1.5975` n `8`; equity avg `0.7471` n `100`; fx avg `0.0139` n `6`; index avg `0.1714` n `25`; metal avg `0.1876` n `20`; unknown avg `0.0998` n `758`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1887`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1765`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1607`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1466`, n `667`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.136`, n `667`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1313`, n `667`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1304`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1286`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1256`, n `667`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.125`, n `667`, weak_sample_signal
