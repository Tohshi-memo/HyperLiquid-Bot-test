# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-24T12:07:26.932906+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0357` n `12`; crypto_alt avg `0.0733` n `230`; crypto_major avg `0.0283` n `8`; equity avg `0.084` n `100`; fx avg `-0.0025` n `6`; index avg `0.0345` n `25`; metal avg `0.0673` n `20`; unknown avg `-0.0383` n `773`
- 1h: commodity avg `0.0975` n `12`; crypto_alt avg `-0.1182` n `230`; crypto_major avg `-0.2038` n `8`; equity avg `-0.0555` n `100`; fx avg `-0.0068` n `6`; index avg `-0.0023` n `25`; metal avg `-0.0007` n `20`; unknown avg `-0.0631` n `773`
- 4h: commodity avg `-0.0288` n `12`; crypto_alt avg `-0.6063` n `230`; crypto_major avg `-0.6458` n `8`; equity avg `0.195` n `100`; fx avg `-0.0668` n `6`; index avg `0.073` n `25`; metal avg `0.1726` n `20`; unknown avg `0.0011` n `772`
- 24h: commodity avg `-0.142` n `12`; crypto_alt avg `-1.4041` n `230`; crypto_major avg `-1.8348` n `8`; equity avg `-1.1941` n `99`; fx avg `-0.1626` n `6`; index avg `-0.3326` n `25`; metal avg `-0.2322` n `20`; unknown avg `0.1283` n `756`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1468`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1439`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1171`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1003`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1001`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0955`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0909`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0876`, n `666`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.086`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0843`, n `666`, weak_sample_signal
