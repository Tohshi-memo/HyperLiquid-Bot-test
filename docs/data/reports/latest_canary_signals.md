# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-14T18:52:29.996056+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.5` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0012` n `12`; crypto_alt avg `0.0011` n `230`; crypto_major avg `0.0204` n `8`; equity avg `0.0058` n `92`; fx avg `-0.0063` n `6`; index avg `-0.009` n `25`; metal avg `0.0347` n `20`; unknown avg `0.2113` n `768`
- 1h: commodity avg `0.1957` n `12`; crypto_alt avg `-0.2313` n `230`; crypto_major avg `0.1029` n `8`; equity avg `-0.0475` n `92`; fx avg `-0.0009` n `6`; index avg `-0.0169` n `25`; metal avg `-0.0714` n `20`; unknown avg `0.065` n `767`
- 4h: commodity avg `0.2042` n `12`; crypto_alt avg `-0.1827` n `230`; crypto_major avg `0.3682` n `8`; equity avg `0.3848` n `92`; fx avg `-0.0468` n `6`; index avg `0.058` n `25`; metal avg `-0.2862` n `20`; unknown avg `-0.2751` n `758`
- 24h: commodity avg `0.379` n `12`; crypto_alt avg `1.6055` n `230`; crypto_major avg `3.3716` n `8`; equity avg `1.1855` n `92`; fx avg `-0.0251` n `6`; index avg `0.3389` n `25`; metal avg `0.5392` n `20`; unknown avg `-0.0717` n `742`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1955`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1645`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1201`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1186`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1183`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0881`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0771`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0761`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0719`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0682`, n `668`, weak_sample_signal
