# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-13T23:37:47.323082+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0221` n `12`; crypto_alt avg `-0.0789` n `228`; crypto_major avg `-0.0329` n `8`; equity avg `-0.0324` n `74`; fx avg `0.0065` n `6`; index avg `-0.0083` n `23`; metal avg `-0.0007` n `18`; unknown avg `0.1575` n `645`
- 1h: commodity avg `-0.113` n `12`; crypto_alt avg `-0.1546` n `228`; crypto_major avg `0.0676` n `8`; equity avg `-0.0188` n `74`; fx avg `0.0063` n `6`; index avg `-0.0421` n `23`; metal avg `-0.0089` n `18`; unknown avg `1.0515` n `645`
- 4h: commodity avg `0.1451` n `12`; crypto_alt avg `0.1445` n `228`; crypto_major avg `0.5242` n `8`; equity avg `0.0855` n `74`; fx avg `-0.0278` n `6`; index avg `0.0678` n `23`; metal avg `0.0046` n `18`; unknown avg `7.5627` n `644`
- 24h: commodity avg `-0.4028` n `12`; crypto_alt avg `2.7225` n `228`; crypto_major avg `1.7558` n `8`; equity avg `0.4038` n `74`; fx avg `0.0069` n `6`; index avg `0.4204` n `23`; metal avg `0.3059` n `18`; unknown avg `0.9329` n `611`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0871`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0867`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0665`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0616`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0609`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0596`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0594`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0592`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0567`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0533`, n `668`, weak_sample_signal
