# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-22T03:52:31.491349+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0447` n `12`; crypto_alt avg `-0.2365` n `228`; crypto_major avg `-0.4194` n `8`; equity avg `-0.0537` n `79`; fx avg `-0.0061` n `6`; index avg `-0.0006` n `23`; metal avg `-0.0201` n `18`; unknown avg `-0.2398` n `701`
- 1h: commodity avg `0.0206` n `12`; crypto_alt avg `-0.3503` n `228`; crypto_major avg `-0.7296` n `8`; equity avg `0.1288` n `79`; fx avg `-0.0108` n `6`; index avg `0.0238` n `23`; metal avg `-0.0783` n `18`; unknown avg `-0.0881` n `701`
- 4h: commodity avg `-0.4259` n `12`; crypto_alt avg `1.091` n `228`; crypto_major avg `0.6291` n `8`; equity avg `0.4672` n `79`; fx avg `0.1095` n `6`; index avg `0.2043` n `23`; metal avg `0.4243` n `18`; unknown avg `0.9985` n `685`
- 24h: commodity avg `-0.3076` n `12`; crypto_alt avg `-0.1269` n `228`; crypto_major avg `-1.1477` n `8`; equity avg `-0.4352` n `79`; fx avg `0.019` n `6`; index avg `0.0092` n `23`; metal avg `0.0843` n `18`; unknown avg `0.1133` n `629`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1106`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1003`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0984`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0886`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0838`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0836`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0826`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0792`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0773`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0758`, n `668`, weak_sample_signal
