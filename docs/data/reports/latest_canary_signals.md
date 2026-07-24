# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-24T03:52:24.416582+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0329` n `12`; crypto_alt avg `-0.0048` n `230`; crypto_major avg `0.0496` n `8`; equity avg `0.0012` n `100`; fx avg `-0.0041` n `6`; index avg `-0.003` n `25`; metal avg `0.0209` n `20`; unknown avg `0.2648` n `772`
- 1h: commodity avg `0.0339` n `12`; crypto_alt avg `0.4019` n `230`; crypto_major avg `0.5537` n `8`; equity avg `-0.0976` n `100`; fx avg `0.0078` n `6`; index avg `0.0151` n `25`; metal avg `0.1029` n `20`; unknown avg `1.1689` n `772`
- 4h: commodity avg `0.0112` n `12`; crypto_alt avg `0.4008` n `230`; crypto_major avg `0.3572` n `8`; equity avg `-0.8226` n `100`; fx avg `-0.1074` n `6`; index avg `-0.2761` n `25`; metal avg `-0.1529` n `20`; unknown avg `0.5769` n `772`
- 24h: commodity avg `0.5355` n `12`; crypto_alt avg `-0.8322` n `230`; crypto_major avg `-1.5431` n `8`; equity avg `-2.2342` n `99`; fx avg `-0.1062` n `6`; index avg `-0.5817` n `25`; metal avg `-1.008` n `20`; unknown avg `-0.2466` n `740`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1809`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1651`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1534`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1142`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1115`, n `666`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1017`, n `666`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1008`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0963`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0948`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0923`, n `666`, weak_sample_signal
