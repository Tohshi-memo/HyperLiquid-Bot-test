# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-23T19:07:15.708699+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1925` n `12`; crypto_alt avg `-0.1671` n `228`; crypto_major avg `-0.1191` n `8`; equity avg `-0.0206` n `67`; fx avg `-0.0037` n `6`; index avg `0.001` n `23`; metal avg `-0.0139` n `18`; unknown avg `-0.3238` n `396`
- 1h: commodity avg `-0.7317` n `12`; crypto_alt avg `0.6287` n `228`; crypto_major avg `0.3995` n `8`; equity avg `0.4254` n `67`; fx avg `-0.0063` n `6`; index avg `0.3116` n `23`; metal avg `0.059` n `18`; unknown avg `0.3966` n `396`
- 4h: commodity avg `-0.701` n `12`; crypto_alt avg `1.1269` n `228`; crypto_major avg `0.6598` n `8`; equity avg `0.5055` n `67`; fx avg `0.0074` n `6`; index avg `0.1412` n `23`; metal avg `0.1565` n `18`; unknown avg `0.7521` n `396`
- 24h: commodity avg `-0.6176` n `12`; crypto_alt avg `0.1366` n `228`; crypto_major avg `0.0635` n `8`; equity avg `0.1171` n `67`; fx avg `-0.0198` n `6`; index avg `0.0918` n `23`; metal avg `0.0657` n `18`; unknown avg `-0.9362` n `376`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1094`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1074`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0912`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0865`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0779`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0756`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0753`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.071`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.069`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0621`, n `668`, weak_sample_signal
