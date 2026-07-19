# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-19T00:37:27.035161+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0333` n `12`; crypto_alt avg `-0.0714` n `230`; crypto_major avg `-0.0225` n `8`; equity avg `0.0807` n `96`; fx avg `0.0416` n `6`; index avg `-0.0118` n `25`; metal avg `0.0015` n `20`; unknown avg `0.0479` n `770`
- 1h: commodity avg `0.0579` n `12`; crypto_alt avg `-0.0479` n `230`; crypto_major avg `-0.0073` n `8`; equity avg `0.0603` n `96`; fx avg `0.0465` n `6`; index avg `-0.032` n `25`; metal avg `0.0212` n `20`; unknown avg `-0.1577` n `770`
- 4h: commodity avg `0.0545` n `12`; crypto_alt avg `0.1941` n `230`; crypto_major avg `0.1763` n `8`; equity avg `0.0989` n `96`; fx avg `0.0431` n `6`; index avg `-0.0249` n `25`; metal avg `0.0065` n `20`; unknown avg `0.1728` n `770`
- 24h: commodity avg `0.4043` n `12`; crypto_alt avg `-0.3138` n `230`; crypto_major avg `0.5734` n `8`; equity avg `-0.1967` n `96`; fx avg `-0.0319` n `6`; index avg `0.0088` n `25`; metal avg `-0.0598` n `20`; unknown avg `0.037` n `737`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `0.1134`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.096`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0956`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0878`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.081`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.078`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0746`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0733`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0706`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.07`, n `668`, weak_sample_signal
