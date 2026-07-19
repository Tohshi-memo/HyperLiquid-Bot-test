# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-19T09:52:31.711797+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0073` n `12`; crypto_alt avg `-0.0513` n `230`; crypto_major avg `-0.048` n `8`; equity avg `0.0245` n `96`; fx avg `-0.0042` n `6`; index avg `-0.0025` n `25`; metal avg `0.0029` n `20`; unknown avg `-0.0115` n `770`
- 1h: commodity avg `0.0188` n `12`; crypto_alt avg `-0.1879` n `230`; crypto_major avg `-0.2434` n `8`; equity avg `-0.1151` n `96`; fx avg `-0.0123` n `6`; index avg `-0.002` n `25`; metal avg `-0.0146` n `20`; unknown avg `-0.0935` n `770`
- 4h: commodity avg `0.0724` n `12`; crypto_alt avg `-0.0889` n `230`; crypto_major avg `-0.0372` n `8`; equity avg `0.0873` n `96`; fx avg `-0.0047` n `6`; index avg `0.0324` n `25`; metal avg `-0.0471` n `20`; unknown avg `0.0001` n `752`
- 24h: commodity avg `0.3158` n `12`; crypto_alt avg `0.5267` n `230`; crypto_major avg `1.1318` n `8`; equity avg `0.2473` n `96`; fx avg `-0.0254` n `6`; index avg `-0.0257` n `25`; metal avg `-0.0829` n `20`; unknown avg `0.038` n `751`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1401`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.13`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.116`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1111`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1104`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0981`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0938`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0878`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0878`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0877`, n `668`, weak_sample_signal
