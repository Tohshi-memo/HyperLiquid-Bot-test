# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-03T04:22:31.577896+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0012` n `13`; crypto_alt avg `0.2318` n `239`; crypto_major avg `0.124` n `8`; equity avg `-0.1416` n `157`; fx avg `0.0004` n `6`; index avg `-0.0273` n `27`; metal avg `-0.0207` n `20`; unknown avg `-0.0335` n `1214`
- 1h: commodity avg `-0.0043` n `13`; crypto_alt avg `0.2137` n `239`; crypto_major avg `0.0951` n `8`; equity avg `-0.5594` n `157`; fx avg `0.0161` n `6`; index avg `-0.1249` n `27`; metal avg `-0.1223` n `20`; unknown avg `-0.2662` n `1202`
- 4h: commodity avg `0.1828` n `13`; crypto_alt avg `-0.7179` n `239`; crypto_major avg `-0.3582` n `8`; equity avg `-0.5849` n `157`; fx avg `-0.0369` n `6`; index avg `-0.0722` n `27`; metal avg `-0.3937` n `20`; unknown avg `0.3477` n `1202`
- 24h: commodity avg `-0.8339` n `13`; crypto_alt avg `-3.4197` n `238`; crypto_major avg `-2.4665` n `8`; equity avg `-4.542` n `157`; fx avg `-0.0278` n `6`; index avg `-0.3812` n `27`; metal avg `-0.1791` n `20`; unknown avg `8.1818` n `968`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `0.1657`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1638`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1571`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1521`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1257`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1118`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1075`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1069`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1063`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1013`, n `668`, weak_sample_signal
