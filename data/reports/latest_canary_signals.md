# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-11T15:52:50.977420+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.2007` n `12`; crypto_alt avg `-0.2607` n `228`; crypto_major avg `-0.4716` n `8`; equity avg `-0.2388` n `74`; fx avg `0.0003` n `6`; index avg `-0.0724` n `23`; metal avg `0.121` n `18`; unknown avg `-0.157` n `556`
- 1h: commodity avg `0.193` n `12`; crypto_alt avg `-0.3477` n `228`; crypto_major avg `-0.4628` n `8`; equity avg `0.1099` n `74`; fx avg `-0.0146` n `6`; index avg `0.0258` n `23`; metal avg `0.1246` n `18`; unknown avg `0.1162` n `556`
- 4h: commodity avg `0.467` n `12`; crypto_alt avg `-0.4937` n `228`; crypto_major avg `-0.8256` n `8`; equity avg `-0.2833` n `74`; fx avg `-0.0741` n `6`; index avg `0.0107` n `23`; metal avg `0.3641` n `18`; unknown avg `0.5032` n `556`
- 24h: commodity avg `-0.6517` n `12`; crypto_alt avg `0.1148` n `228`; crypto_major avg `-0.6219` n `8`; equity avg `-0.0955` n `74`; fx avg `-0.0264` n `6`; index avg `0.1576` n `23`; metal avg `-0.4559` n `18`; unknown avg `2.6085` n `528`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1498`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1103`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1093`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1067`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1032`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.086`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0846`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0823`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0819`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0814`, n `668`, weak_sample_signal
