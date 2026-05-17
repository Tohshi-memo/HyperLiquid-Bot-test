# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-17T16:52:13.472254+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0067` n `12`; crypto_alt avg `-0.2338` n `228`; crypto_major avg `-0.1639` n `8`; equity avg `0.0063` n `65`; fx avg `0.0006` n `5`; index avg `-0.0756` n `23`; metal avg `0.0131` n `18`; unknown avg `-0.2202` n `384`
- 1h: commodity avg `-0.0285` n `12`; crypto_alt avg `-0.0655` n `228`; crypto_major avg `-0.0131` n `8`; equity avg `0.0445` n `65`; fx avg `-0.0002` n `5`; index avg `-0.0157` n `23`; metal avg `0.0041` n `18`; unknown avg `-0.1095` n `384`
- 4h: commodity avg `-0.0166` n `12`; crypto_alt avg `-0.3718` n `228`; crypto_major avg `-0.4624` n `8`; equity avg `-0.0064` n `65`; fx avg `0.0204` n `5`; index avg `0.034` n `23`; metal avg `0.0168` n `18`; unknown avg `-0.2038` n `383`
- 24h: commodity avg `1.7794` n `12`; crypto_alt avg `-9.3591` n `228`; crypto_major avg `-2.5244` n `8`; equity avg `-2.5252` n `65`; fx avg `-0.1651` n `5`; index avg `-1.6108` n `23`; metal avg `-5.8244` n `18`; unknown avg `549.9745` n `367`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1361`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.114`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0959`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.093`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0867`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0858`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.075`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0734`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0707`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0694`, n `668`, weak_sample_signal
