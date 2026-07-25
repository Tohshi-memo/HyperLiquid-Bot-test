# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-25T11:37:26.362644+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0383` n `12`; crypto_alt avg `-0.1289` n `230`; crypto_major avg `-0.087` n `8`; equity avg `-0.0749` n `100`; fx avg `0.0022` n `6`; index avg `-0.0113` n `25`; metal avg `-0.0007` n `20`; unknown avg `-0.0087` n `774`
- 1h: commodity avg `-0.0325` n `12`; crypto_alt avg `-0.0617` n `230`; crypto_major avg `-0.0203` n `8`; equity avg `-0.0628` n `100`; fx avg `-0.0118` n `6`; index avg `-0.0044` n `25`; metal avg `0.0054` n `20`; unknown avg `-0.0646` n `774`
- 4h: commodity avg `-0.0322` n `12`; crypto_alt avg `-0.1076` n `230`; crypto_major avg `0.1225` n `8`; equity avg `-0.1048` n `100`; fx avg `-0.0108` n `6`; index avg `-0.0008` n `25`; metal avg `-0.005` n `20`; unknown avg `0.5663` n `774`
- 24h: commodity avg `-0.022` n `12`; crypto_alt avg `-1.2947` n `230`; crypto_major avg `-0.9175` n `8`; equity avg `-2.8927` n `100`; fx avg `-0.0151` n `6`; index avg `-0.2556` n `25`; metal avg `-0.1226` n `20`; unknown avg `13.1288` n `757`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1585`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1483`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1198`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1168`, n `666`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1154`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1112`, n `666`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1098`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.109`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.101`, n `666`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1`, n `668`, weak_sample_signal
