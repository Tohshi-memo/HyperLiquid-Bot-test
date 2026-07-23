# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-23T00:37:25.606705+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0356` n `12`; crypto_alt avg `0.0465` n `230`; crypto_major avg `-0.0581` n `8`; equity avg `0.048` n `98`; fx avg `-0.029` n `6`; index avg `0.0105` n `25`; metal avg `0.0105` n `20`; unknown avg `0.0506` n `773`
- 1h: commodity avg `0.053` n `12`; crypto_alt avg `0.3806` n `230`; crypto_major avg `0.3777` n `8`; equity avg `0.4914` n `98`; fx avg `-0.0299` n `6`; index avg `0.127` n `25`; metal avg `0.0854` n `20`; unknown avg `-0.1757` n `773`
- 4h: commodity avg `0.2676` n `12`; crypto_alt avg `0.1032` n `230`; crypto_major avg `0.3625` n `8`; equity avg `0.3221` n `98`; fx avg `-0.0377` n `6`; index avg `0.064` n `25`; metal avg `-0.0362` n `20`; unknown avg `0.0316` n `773`
- 24h: commodity avg `0.7824` n `12`; crypto_alt avg `-0.467` n `230`; crypto_major avg `-0.6143` n `8`; equity avg `-0.944` n `98`; fx avg `-0.0653` n `6`; index avg `-0.1043` n `25`; metal avg `0.1651` n `20`; unknown avg `1.6651` n `739`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1598`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1168`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.112`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.101`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0995`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0951`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0833`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0821`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0813`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0669`, n `666`, weak_sample_signal
