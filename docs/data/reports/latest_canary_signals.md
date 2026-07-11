# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-11T15:07:25.048211+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.028` n `12`; crypto_alt avg `0.0737` n `230`; crypto_major avg `0.0184` n `8`; equity avg `0.0097` n `92`; fx avg `-0.0004` n `6`; index avg `0.0021` n `25`; metal avg `-0.0358` n `20`; unknown avg `0.0518` n `765`
- 1h: commodity avg `-0.0269` n `12`; crypto_alt avg `0.2747` n `230`; crypto_major avg `0.3257` n `8`; equity avg `0.0714` n `92`; fx avg `-0.0166` n `6`; index avg `0.0121` n `25`; metal avg `-0.0142` n `20`; unknown avg `0.1699` n `765`
- 4h: commodity avg `-0.0057` n `12`; crypto_alt avg `0.6956` n `230`; crypto_major avg `0.5465` n `8`; equity avg `-0.0739` n `92`; fx avg `-0.0086` n `6`; index avg `0.007` n `25`; metal avg `-0.0317` n `20`; unknown avg `0.0988` n `765`
- 24h: commodity avg `0.0934` n `12`; crypto_alt avg `1.1762` n `229`; crypto_major avg `0.8184` n `8`; equity avg `0.5013` n `92`; fx avg `-0.0513` n `6`; index avg `0.1489` n `25`; metal avg `0.0882` n `20`; unknown avg `3.0267` n `727`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1158`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1118`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1098`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1097`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1051`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1018`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1016`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1011`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0908`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0893`, n `668`, weak_sample_signal
