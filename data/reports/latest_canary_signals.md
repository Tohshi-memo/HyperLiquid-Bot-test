# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-26T22:07:15.981848+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0385` n `12`; crypto_alt avg `-0.266` n `228`; crypto_major avg `-0.2052` n `8`; equity avg `-0.0651` n `67`; fx avg `0.0152` n `6`; index avg `-0.0564` n `23`; metal avg `0.0649` n `18`; unknown avg `0.0904` n `418`
- 1h: commodity avg `-0.3779` n `12`; crypto_alt avg `-0.2645` n `228`; crypto_major avg `-0.2023` n `8`; equity avg `0.0376` n `67`; fx avg `0.018` n `6`; index avg `0.0076` n `23`; metal avg `0.0063` n `18`; unknown avg `0.0089` n `418`
- 4h: commodity avg `-0.3585` n `12`; crypto_alt avg `-0.38` n `228`; crypto_major avg `-0.6875` n `8`; equity avg `0.0894` n `67`; fx avg `0.033` n `6`; index avg `0.0865` n `23`; metal avg `0.7379` n `18`; unknown avg `-0.6767` n `418`
- 24h: commodity avg `0.6781` n `12`; crypto_alt avg `-2.0604` n `228`; crypto_major avg `-1.8479` n `8`; equity avg `-0.317` n `67`; fx avg `-0.1144` n `6`; index avg `0.4375` n `23`; metal avg `-0.8494` n `18`; unknown avg `0.0222` n `395`

## Correlations

- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1758`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1753`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.174`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1584`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1482`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1456`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1417`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.136`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1355`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1313`, n `668`, weak_sample_signal
