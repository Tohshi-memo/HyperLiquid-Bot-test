# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-11T12:52:32.133091+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1487` n `12`; crypto_alt avg `0.2406` n `228`; crypto_major avg `0.3328` n `8`; equity avg `0.3419` n `74`; fx avg `0.0243` n `6`; index avg `0.1664` n `23`; metal avg `0.2061` n `18`; unknown avg `0.0158` n `556`
- 1h: commodity avg `0.5727` n `12`; crypto_alt avg `-0.6544` n `228`; crypto_major avg `-0.621` n `8`; equity avg `-0.5021` n `74`; fx avg `0.0073` n `6`; index avg `-0.1543` n `23`; metal avg `-0.2842` n `18`; unknown avg `0.1063` n `556`
- 4h: commodity avg `0.539` n `12`; crypto_alt avg `-0.3245` n `228`; crypto_major avg `-0.1067` n `8`; equity avg `-0.4337` n `74`; fx avg `-0.0053` n `6`; index avg `-0.1534` n `23`; metal avg `-0.5643` n `18`; unknown avg `0.9424` n `556`
- 24h: commodity avg `-0.1383` n `12`; crypto_alt avg `0.763` n `228`; crypto_major avg `0.9032` n `8`; equity avg `-0.1031` n `74`; fx avg `0.0305` n `6`; index avg `-0.3591` n `23`; metal avg `-0.8796` n `18`; unknown avg `4.3802` n `527`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.155`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1076`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.107`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1024`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0954`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0892`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0831`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0818`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0804`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0803`, n `668`, weak_sample_signal
