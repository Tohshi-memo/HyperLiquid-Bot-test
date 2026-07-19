# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-19T04:39:52.718799+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0171` n `12`; crypto_alt avg `0.1279` n `230`; crypto_major avg `0.1635` n `8`; equity avg `0.0354` n `96`; fx avg `-0.0188` n `6`; index avg `-0.0017` n `25`; metal avg `0.0111` n `20`; unknown avg `1.8677` n `770`
- 1h: commodity avg `-0.0456` n `12`; crypto_alt avg `0.0149` n `230`; crypto_major avg `0.1079` n `8`; equity avg `0.11` n `96`; fx avg `-0.0184` n `6`; index avg `-0.0221` n `25`; metal avg `-0.0079` n `20`; unknown avg `0.8008` n `770`
- 4h: commodity avg `-0.0866` n `12`; crypto_alt avg `0.0168` n `230`; crypto_major avg `0.2495` n `8`; equity avg `0.2212` n `96`; fx avg `-0.0097` n `6`; index avg `0.0095` n `25`; metal avg `0.0394` n `20`; unknown avg `-0.2047` n `770`
- 24h: commodity avg `0.3096` n `12`; crypto_alt avg `0.1517` n `230`; crypto_major avg `0.9487` n `8`; equity avg `-0.0318` n `96`; fx avg `-0.0357` n `6`; index avg `-0.049` n `25`; metal avg `-0.0136` n `20`; unknown avg `0.0215` n `737`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `0.1173`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0966`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.096`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0926`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0844`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0819`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0808`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0761`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0708`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0681`, n `668`, weak_sample_signal
