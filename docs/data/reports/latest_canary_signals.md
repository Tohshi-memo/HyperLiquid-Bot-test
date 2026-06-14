# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-14T02:07:24.836384+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0131` n `12`; crypto_alt avg `-0.0765` n `228`; crypto_major avg `-0.0631` n `8`; equity avg `0.1276` n `74`; fx avg `0.0197` n `6`; index avg `-0.0092` n `23`; metal avg `-0.0281` n `18`; unknown avg `-0.1831` n `645`
- 1h: commodity avg `0.0117` n `12`; crypto_alt avg `0.2136` n `228`; crypto_major avg `0.0258` n `8`; equity avg `0.1653` n `74`; fx avg `0.0118` n `6`; index avg `-0.0128` n `23`; metal avg `-0.024` n `18`; unknown avg `91.9839` n `645`
- 4h: commodity avg `-0.3108` n `12`; crypto_alt avg `-0.2393` n `228`; crypto_major avg `0.0691` n `8`; equity avg `0.2174` n `74`; fx avg `0.0085` n `6`; index avg `-0.076` n `23`; metal avg `0.1688` n `18`; unknown avg `4.5693` n `644`
- 24h: commodity avg `-0.8104` n `12`; crypto_alt avg `1.3347` n `228`; crypto_major avg `1.2582` n `8`; equity avg `0.5073` n `74`; fx avg `0.0102` n `6`; index avg `0.292` n `23`; metal avg `0.2194` n `18`; unknown avg `0.1441` n `611`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.092`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0886`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0649`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0643`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0642`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0599`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0598`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0579`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0575`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0553`, n `668`, weak_sample_signal
