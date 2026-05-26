# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-26T18:07:21.213358+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.8973` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_equity_divergence: score `-1.8614` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0433` n `12`; crypto_alt avg `-0.1135` n `228`; crypto_major avg `0.0267` n `8`; equity avg `-0.1125` n `67`; fx avg `-0.0044` n `6`; index avg `-0.0316` n `23`; metal avg `-0.1775` n `18`; unknown avg `0.8126` n `418`
- 1h: commodity avg `-0.0236` n `12`; crypto_alt avg `-0.9254` n `228`; crypto_major avg `-0.5102` n `8`; equity avg `-0.1267` n `67`; fx avg `0.0019` n `6`; index avg `0.0476` n `23`; metal avg `-0.2522` n `18`; unknown avg `0.8675` n `418`
- 4h: commodity avg `-0.1323` n `12`; crypto_alt avg `-2.1462` n `228`; crypto_major avg `-1.8699` n `8`; equity avg `-0.0085` n `67`; fx avg `0.015` n `6`; index avg `0.0274` n `23`; metal avg `-0.477` n `18`; unknown avg `2.2632` n `416`
- 24h: commodity avg `1.0534` n `12`; crypto_alt avg `-2.5266` n `228`; crypto_major avg `-1.7095` n `8`; equity avg `-0.4496` n `67`; fx avg `-0.1152` n `6`; index avg `0.2633` n `23`; metal avg `-1.5365` n `18`; unknown avg `1.0321` n `395`

## Correlations

- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1731`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1716`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.168`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1582`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1362`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1321`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1313`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1288`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1231`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1204`, n `668`, weak_sample_signal
