# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-13T13:22:30.431995+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0099` n `12`; crypto_alt avg `0.1182` n `228`; crypto_major avg `0.0121` n `8`; equity avg `-0.021` n `74`; fx avg `0.006` n `6`; index avg `0.0105` n `23`; metal avg `0.1469` n `18`; unknown avg `-0.0322` n `644`
- 1h: commodity avg `-0.0957` n `12`; crypto_alt avg `0.0483` n `228`; crypto_major avg `0.3296` n `8`; equity avg `0.1181` n `74`; fx avg `0.0067` n `6`; index avg `0.1553` n `23`; metal avg `0.1809` n `18`; unknown avg `1.3098` n `644`
- 4h: commodity avg `-1.1355` n `12`; crypto_alt avg `0.5103` n `228`; crypto_major avg `0.683` n `8`; equity avg `0.0019` n `74`; fx avg `0.0263` n `6`; index avg `0.1562` n `23`; metal avg `0.0689` n `18`; unknown avg `1.5929` n `635`
- 24h: commodity avg `-0.6763` n `12`; crypto_alt avg `1.4831` n `228`; crypto_major avg `0.6834` n `8`; equity avg `-0.0086` n `74`; fx avg `0.0476` n `6`; index avg `1.0026` n `23`; metal avg `0.8667` n `18`; unknown avg `27.7797` n `611`

## Correlations

- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0838`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0764`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0732`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.07`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0607`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0592`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0571`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0567`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0555`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0522`, n `668`, weak_sample_signal
