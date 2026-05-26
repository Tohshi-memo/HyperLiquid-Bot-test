# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-26T12:52:21.397276+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.2735` n `12`; crypto_alt avg `-0.1095` n `228`; crypto_major avg `-0.1042` n `8`; equity avg `-0.0228` n `67`; fx avg `0.0096` n `6`; index avg `-0.0003` n `23`; metal avg `-0.1327` n `18`; unknown avg `-0.736` n `417`
- 1h: commodity avg `0.2735` n `12`; crypto_alt avg `-0.1095` n `228`; crypto_major avg `-0.1042` n `8`; equity avg `-0.0228` n `67`; fx avg `0.0096` n `6`; index avg `-0.0003` n `23`; metal avg `-0.1327` n `18`; unknown avg `-0.736` n `417`
- 4h: commodity avg `-0.5294` n `12`; crypto_alt avg `1.1784` n `228`; crypto_major avg `1.1661` n `8`; equity avg `0.3905` n `67`; fx avg `-0.0172` n `6`; index avg `0.2869` n `23`; metal avg `0.0176` n `18`; unknown avg `0.0355` n `417`
- 24h: commodity avg `0.3035` n `12`; crypto_alt avg `0.2906` n `228`; crypto_major avg `-0.5703` n `8`; equity avg `-0.3196` n `67`; fx avg `-0.1462` n `6`; index avg `0.1226` n `23`; metal avg `-0.6532` n `18`; unknown avg `0.0987` n `395`

## Correlations

- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1869`, n `671`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1819`, n `671`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1727`, n `671`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1714`, n `671`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1482`, n `671`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1346`, n `671`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1324`, n `671`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1302`, n `671`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1296`, n `671`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1262`, n `671`, weak_sample_signal
