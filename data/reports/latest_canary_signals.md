# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-26T01:07:29.309609+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.01` n `12`; crypto_alt avg `0.0193` n `230`; crypto_major avg `0.0186` n `8`; equity avg `0.046` n `100`; fx avg `-0.0036` n `6`; index avg `0.0106` n `25`; metal avg `0.0019` n `20`; unknown avg `0.134` n `774`
- 1h: commodity avg `-0.0211` n `12`; crypto_alt avg `0.0726` n `230`; crypto_major avg `0.0497` n `8`; equity avg `0.0087` n `100`; fx avg `-0.006` n `6`; index avg `-0.0068` n `25`; metal avg `-0.0008` n `20`; unknown avg `0.0024` n `774`
- 4h: commodity avg `-0.0588` n `12`; crypto_alt avg `0.1096` n `230`; crypto_major avg `0.1267` n `8`; equity avg `0.1212` n `100`; fx avg `-0.0097` n `6`; index avg `0.0246` n `25`; metal avg `0.0003` n `20`; unknown avg `-0.2451` n `774`
- 24h: commodity avg `-0.6055` n `12`; crypto_alt avg `0.2879` n `230`; crypto_major avg `1.0116` n `8`; equity avg `0.4604` n `100`; fx avg `-0.0515` n `6`; index avg `0.1302` n `25`; metal avg `0.0149` n `20`; unknown avg `-0.2585` n `758`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1799`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1729`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1512`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.135`, n `666`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1302`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1235`, n `666`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1224`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.122`, n `666`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1168`, n `666`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1167`, n `666`, weak_sample_signal
