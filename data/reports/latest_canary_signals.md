# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-28T08:07:23.672625+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1898` n `12`; crypto_alt avg `0.14` n `228`; crypto_major avg `0.0877` n `8`; equity avg `0.1607` n `67`; fx avg `-0.0023` n `6`; index avg `0.0917` n `23`; metal avg `0.1112` n `18`; unknown avg `-0.0307` n `419`
- 1h: commodity avg `-0.0316` n `12`; crypto_alt avg `0.4994` n `228`; crypto_major avg `0.4453` n `8`; equity avg `0.1139` n `67`; fx avg `-0.0066` n `6`; index avg `0.011` n `23`; metal avg `0.0702` n `18`; unknown avg `0.186` n `419`
- 4h: commodity avg `-0.4585` n `12`; crypto_alt avg `0.0867` n `228`; crypto_major avg `0.5863` n `8`; equity avg `1.385` n `67`; fx avg `0.0332` n `6`; index avg `0.4336` n `23`; metal avg `0.6601` n `18`; unknown avg `0.0466` n `409`
- 24h: commodity avg `0.5374` n `12`; crypto_alt avg `-4.8164` n `228`; crypto_major avg `-3.3439` n `8`; equity avg `-1.1168` n `67`; fx avg `-0.1114` n `6`; index avg `-0.7688` n `23`; metal avg `-1.3135` n `18`; unknown avg `-1.712` n `408`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1805`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1752`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1695`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1587`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1585`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1505`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1411`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1324`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1295`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1272`, n `668`, weak_sample_signal
