# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-11T05:52:32.973097+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0826` n `12`; crypto_alt avg `-0.1358` n `228`; crypto_major avg `0.0176` n `8`; equity avg `-0.0515` n `74`; fx avg `0.0191` n `6`; index avg `-0.0189` n `23`; metal avg `-0.0057` n `18`; unknown avg `-0.0281` n `550`
- 1h: commodity avg `-0.2098` n `12`; crypto_alt avg `-0.5324` n `228`; crypto_major avg `-0.1165` n `8`; equity avg `-0.1491` n `74`; fx avg `0.0137` n `6`; index avg `-0.0619` n `23`; metal avg `0.1794` n `18`; unknown avg `-0.0904` n `550`
- 4h: commodity avg `-0.442` n `12`; crypto_alt avg `0.7341` n `228`; crypto_major avg `0.3679` n `8`; equity avg `0.0481` n `74`; fx avg `-0.0086` n `6`; index avg `0.1142` n `23`; metal avg `-0.0462` n `18`; unknown avg `7.2895` n `550`
- 24h: commodity avg `1.4927` n `12`; crypto_alt avg `1.4076` n `228`; crypto_major avg `1.0705` n `8`; equity avg `-0.1551` n `74`; fx avg `0.0305` n `6`; index avg `-0.4192` n `23`; metal avg `-0.4587` n `18`; unknown avg `2.8203` n `537`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1415`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1101`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1078`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0961`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0926`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0905`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0902`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0899`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0858`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0763`, n `668`, weak_sample_signal
