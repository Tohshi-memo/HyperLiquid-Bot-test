# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-17T12:07:15.299594+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0031` n `12`; crypto_alt avg `0.0147` n `228`; crypto_major avg `-0.0252` n `8`; equity avg `0.0065` n `65`; fx avg `-0.0187` n `5`; index avg `-0.005` n `23`; metal avg `0.0011` n `18`; unknown avg `-0.059` n `383`
- 1h: commodity avg `-0.0284` n `12`; crypto_alt avg `-0.1202` n `228`; crypto_major avg `-0.122` n `8`; equity avg `0.036` n `65`; fx avg `-0.0188` n `5`; index avg `0.0063` n `23`; metal avg `0.0057` n `18`; unknown avg `-0.1288` n `383`
- 4h: commodity avg `0.0223` n `12`; crypto_alt avg `-0.1591` n `228`; crypto_major avg `0.2749` n `8`; equity avg `0.2976` n `65`; fx avg `-0.0141` n `5`; index avg `0.1629` n `23`; metal avg `-0.0524` n `18`; unknown avg `-0.1095` n `383`
- 24h: commodity avg `1.7518` n `12`; crypto_alt avg `-8.9831` n `228`; crypto_major avg `-2.297` n `8`; equity avg `-2.5964` n `65`; fx avg `-0.1861` n `5`; index avg `-1.6538` n `23`; metal avg `-5.849` n `18`; unknown avg `550.0626` n `367`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1417`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1195`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0904`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0895`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0799`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0758`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0722`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0707`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0658`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0638`, n `668`, weak_sample_signal
