# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-12T01:07:30.695103+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1193` n `12`; crypto_alt avg `-0.3096` n `228`; crypto_major avg `-0.2736` n `8`; equity avg `-0.361` n `74`; fx avg `0.0002` n `6`; index avg `-0.0666` n `23`; metal avg `-0.3159` n `18`; unknown avg `0.1029` n `556`
- 1h: commodity avg `-0.001` n `12`; crypto_alt avg `-0.2958` n `228`; crypto_major avg `-0.3894` n `8`; equity avg `-0.1164` n `74`; fx avg `-0.0561` n `6`; index avg `-0.1574` n `23`; metal avg `-0.5062` n `18`; unknown avg `-0.0057` n `556`
- 4h: commodity avg `-0.0011` n `12`; crypto_alt avg `-0.1161` n `228`; crypto_major avg `0.0421` n `8`; equity avg `0.6448` n `74`; fx avg `0.0389` n `6`; index avg `0.247` n `23`; metal avg `-0.2209` n `18`; unknown avg `-0.3557` n `556`
- 24h: commodity avg `-2.5977` n `12`; crypto_alt avg `3.1502` n `228`; crypto_major avg `3.4555` n `8`; equity avg `3.9326` n `74`; fx avg `-0.0146` n `6`; index avg `2.2438` n `23`; metal avg `3.1699` n `18`; unknown avg `2.6295` n `530`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.1106`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1023`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0997`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0947`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0924`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0857`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0839`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0658`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0655`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0644`, n `668`, weak_sample_signal
