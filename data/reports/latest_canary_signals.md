# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-14T00:22:33.909418+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0109` n `12`; crypto_alt avg `0.0844` n `228`; crypto_major avg `-0.0313` n `8`; equity avg `-0.0182` n `74`; fx avg `-0.0001` n `6`; index avg `-0.0016` n `23`; metal avg `-0.0069` n `18`; unknown avg `-0.2374` n `645`
- 1h: commodity avg `-0.2421` n `12`; crypto_alt avg `-0.2242` n `228`; crypto_major avg `-0.1843` n `8`; equity avg `-0.057` n `74`; fx avg `0.006` n `6`; index avg `-0.0141` n `23`; metal avg `-0.0135` n `18`; unknown avg `-0.0636` n `645`
- 4h: commodity avg `-0.1677` n `12`; crypto_alt avg `0.1412` n `228`; crypto_major avg `0.3474` n `8`; equity avg `0.0426` n `74`; fx avg `-0.0171` n `6`; index avg `-0.0381` n `23`; metal avg `-0.0098` n `18`; unknown avg `8.3877` n `644`
- 24h: commodity avg `-0.6264` n `12`; crypto_alt avg `2.0105` n `228`; crypto_major avg `1.4189` n `8`; equity avg `0.2607` n `74`; fx avg `-0.0189` n `6`; index avg `0.3058` n `23`; metal avg `0.2435` n `18`; unknown avg `0.9212` n `611`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0879`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0862`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0641`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0625`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0601`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0599`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.057`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0568`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0566`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0533`, n `668`, weak_sample_signal
