# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-20T04:52:21.486856+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0886` n `12`; crypto_alt avg `0.199` n `228`; crypto_major avg `0.0748` n `8`; equity avg `-0.0466` n `66`; fx avg `0.0273` n `6`; index avg `0.0049` n `23`; metal avg `-0.0129` n `18`; unknown avg `-0.0352` n `384`
- 1h: commodity avg `0.0512` n `12`; crypto_alt avg `0.215` n `228`; crypto_major avg `0.1514` n `8`; equity avg `0.0779` n `66`; fx avg `0.0146` n `6`; index avg `0.0671` n `23`; metal avg `0.0012` n `18`; unknown avg `-0.3074` n `384`
- 4h: commodity avg `0.0011` n `12`; crypto_alt avg `0.4252` n `228`; crypto_major avg `0.1366` n `8`; equity avg `0.0685` n `66`; fx avg `-0.0109` n `6`; index avg `-0.1728` n `23`; metal avg `-0.6887` n `18`; unknown avg `-0.5172` n `384`
- 24h: commodity avg `0.707` n `12`; crypto_alt avg `-1.0753` n `228`; crypto_major avg `-0.861` n `8`; equity avg `0.1618` n `66`; fx avg `-0.1096` n `6`; index avg `-0.4986` n `23`; metal avg `-2.0737` n `18`; unknown avg `0.6208` n `363`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1119`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0739`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.065`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0649`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0643`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0609`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0572`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0477`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0446`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0401`, n `668`, weak_sample_signal
