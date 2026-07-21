# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-21T01:37:25.561421+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0181` n `12`; crypto_alt avg `0.0085` n `230`; crypto_major avg `0.0899` n `8`; equity avg `-0.0622` n `98`; fx avg `-0.0111` n `6`; index avg `0.0723` n `25`; metal avg `-0.0203` n `20`; unknown avg `0.1817` n `771`
- 1h: commodity avg `-0.0614` n `12`; crypto_alt avg `-0.0472` n `230`; crypto_major avg `0.0316` n `8`; equity avg `0.2976` n `98`; fx avg `0.0194` n `6`; index avg `0.1784` n `25`; metal avg `0.069` n `20`; unknown avg `0.0219` n `771`
- 4h: commodity avg `-0.0073` n `12`; crypto_alt avg `-0.0435` n `230`; crypto_major avg `0.068` n `8`; equity avg `0.4748` n `98`; fx avg `0.0338` n `6`; index avg `0.186` n `25`; metal avg `0.1113` n `20`; unknown avg `-0.3836` n `770`
- 24h: commodity avg `-0.3493` n `12`; crypto_alt avg `1.2172` n `230`; crypto_major avg `1.0518` n `8`; equity avg `0.2693` n `98`; fx avg `-0.1041` n `6`; index avg `0.1268` n `25`; metal avg `0.249` n `20`; unknown avg `-0.1365` n `747`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1567`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1289`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1235`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0977`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0938`, n `666`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0919`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0885`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.088`, n `666`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0792`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0752`, n `666`, weak_sample_signal
