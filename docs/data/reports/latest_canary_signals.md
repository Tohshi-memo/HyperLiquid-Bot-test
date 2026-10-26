# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-26T03:22:28.283291+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0095` n `13`; crypto_alt avg `-0.2765` n `237`; crypto_major avg `-0.1636` n `8`; equity avg `-0.1109` n `152`; fx avg `0.0033` n `6`; index avg `-0.0366` n `26`; metal avg `0.0464` n `20`; unknown avg `0.2322` n `1240`
- 1h: commodity avg `-0.0685` n `13`; crypto_alt avg `-0.0358` n `237`; crypto_major avg `-0.0451` n `8`; equity avg `-0.0319` n `152`; fx avg `0.0061` n `6`; index avg `-0.0076` n `26`; metal avg `0.1704` n `20`; unknown avg `1.3245` n `1234`
- 4h: commodity avg `-0.2957` n `13`; crypto_alt avg `-0.9229` n `237`; crypto_major avg `-0.8061` n `8`; equity avg `-1.1052` n `152`; fx avg `-0.0008` n `6`; index avg `-0.1349` n `26`; metal avg `0.0647` n `20`; unknown avg `5.9263` n `1162`
- 24h: commodity avg `-0.6286` n `13`; crypto_alt avg `-1.702` n `237`; crypto_major avg `-1.5214` n `8`; equity avg `-0.8019` n `152`; fx avg `0.0569` n `6`; index avg `-0.0305` n `26`; metal avg `0.2371` n `20`; unknown avg `0.1194` n `989`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.2457`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1886`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1859`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1738`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1662`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1471`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1301`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.129`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1176`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0944`, n `668`, weak_sample_signal
