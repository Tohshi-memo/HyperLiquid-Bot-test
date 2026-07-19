# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-19T03:52:26.655014+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0006` n `12`; crypto_alt avg `-0.06` n `230`; crypto_major avg `0.0011` n `8`; equity avg `-0.0084` n `96`; fx avg `-0.0035` n `6`; index avg `-0.012` n `25`; metal avg `-0.0015` n `20`; unknown avg `-0.1399` n `770`
- 1h: commodity avg `0.0464` n `12`; crypto_alt avg `-0.2081` n `230`; crypto_major avg `-0.222` n `8`; equity avg `-0.032` n `96`; fx avg `0.0006` n `6`; index avg `0.0041` n `25`; metal avg `0.0205` n `20`; unknown avg `0.1916` n `770`
- 4h: commodity avg `-0.0066` n `12`; crypto_alt avg `-0.0767` n `230`; crypto_major avg `0.1414` n `8`; equity avg `0.1591` n `96`; fx avg `0.0523` n `6`; index avg `-0.0122` n `25`; metal avg `0.06` n `20`; unknown avg `-0.4453` n `770`
- 24h: commodity avg `0.3348` n `12`; crypto_alt avg `-0.188` n `230`; crypto_major avg `0.751` n `8`; equity avg `-0.2195` n `96`; fx avg `-0.0159` n `6`; index avg `-0.0201` n `25`; metal avg `-0.0057` n `20`; unknown avg `0.0403` n `737`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `0.1157`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1016`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0994`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0916`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0825`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0787`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0763`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0763`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0697`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0671`, n `668`, weak_sample_signal
