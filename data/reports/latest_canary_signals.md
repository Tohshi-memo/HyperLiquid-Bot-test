# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-19T14:37:25.410151+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0021` n `12`; crypto_alt avg `0.0956` n `230`; crypto_major avg `0.1812` n `8`; equity avg `0.0065` n `96`; fx avg `0.0001` n `6`; index avg `-0.0039` n `25`; metal avg `0.0019` n `20`; unknown avg `-0.0103` n `770`
- 1h: commodity avg `-0.0072` n `12`; crypto_alt avg `0.0653` n `230`; crypto_major avg `0.1726` n `8`; equity avg `-0.0456` n `96`; fx avg `-0.0028` n `6`; index avg `0.0061` n `25`; metal avg `-0.0063` n `20`; unknown avg `0.0466` n `770`
- 4h: crypto_alt avg `-0.0475` n `225`; crypto_major avg `0.066` n `7`; metal avg `0.0349` n `1`; unknown avg `-0.0809` n `703`
- 24h: commodity avg `0.2332` n `12`; crypto_alt avg `0.4037` n `230`; crypto_major avg `0.9597` n `8`; equity avg `0.2805` n `96`; fx avg `-0.006` n `6`; index avg `-0.0236` n `25`; metal avg `-0.0297` n `20`; unknown avg `0.128` n `752`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1378`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1277`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1262`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1232`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1228`, n `666`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1117`, n `666`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1054`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1004`, n `666`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0919`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0905`, n `666`, weak_sample_signal
