# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-26T00:52:28.584540+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0219` n `12`; crypto_alt avg `0.0347` n `230`; crypto_major avg `0.0134` n `8`; equity avg `-0.012` n `100`; fx avg `-0.0095` n `6`; index avg `-0.0163` n `25`; metal avg `-0.0022` n `20`; unknown avg `-0.0328` n `774`
- 1h: commodity avg `-0.0337` n `12`; crypto_alt avg `0.1189` n `230`; crypto_major avg `0.132` n `8`; equity avg `-0.0261` n `100`; fx avg `-0.0167` n `6`; index avg `-0.0085` n `25`; metal avg `0.007` n `20`; unknown avg `-0.1444` n `774`
- 4h: commodity avg `-0.0588` n `12`; crypto_alt avg `0.0537` n `230`; crypto_major avg `0.0306` n `8`; equity avg `0.0634` n `100`; fx avg `-0.0083` n `6`; index avg `-0.0021` n `25`; metal avg `-0.0036` n `20`; unknown avg `-0.276` n `774`
- 24h: commodity avg `-0.6852` n `12`; crypto_alt avg `0.4772` n `230`; crypto_major avg `1.1137` n `8`; equity avg `0.4887` n `100`; fx avg `-0.0308` n `6`; index avg `0.136` n `25`; metal avg `0.0064` n `20`; unknown avg `-0.2387` n `758`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.18`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1732`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1511`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1351`, n `666`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1304`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1232`, n `666`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1224`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1221`, n `666`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1168`, n `666`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.116`, n `666`, weak_sample_signal
