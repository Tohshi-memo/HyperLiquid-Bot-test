# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-17T11:22:15.324509+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0421` n `12`; crypto_alt avg `-0.1166` n `228`; crypto_major avg `-0.1168` n `8`; equity avg `0.0016` n `65`; fx avg `0.0006` n `5`; index avg `-0.0058` n `23`; metal avg `-0.0061` n `18`; unknown avg `-0.0631` n `383`
- 1h: commodity avg `-0.0473` n `12`; crypto_alt avg `-0.428` n `228`; crypto_major avg `-0.154` n `8`; equity avg `0.0469` n `65`; fx avg `0.0019` n `5`; index avg `0.0269` n `23`; metal avg `-0.0159` n `18`; unknown avg `-0.1113` n `383`
- 4h: commodity avg `-0.0651` n `12`; crypto_alt avg `-0.0872` n `228`; crypto_major avg `0.3544` n `8`; equity avg `0.2683` n `65`; fx avg `0.007` n `5`; index avg `0.1372` n `23`; metal avg `-0.0487` n `18`; unknown avg `-0.0049` n `383`
- 24h: commodity avg `1.7365` n `12`; crypto_alt avg `-8.9796` n `228`; crypto_major avg `-2.2857` n `8`; equity avg `-2.6242` n `65`; fx avg `-0.167` n `5`; index avg `-1.6653` n `23`; metal avg `-5.8602` n `18`; unknown avg `550.1506` n `367`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1376`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1162`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.092`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0908`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0816`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0754`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0732`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0704`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0663`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0643`, n `668`, weak_sample_signal
