# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-11T16:22:29.283390+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0193` n `12`; crypto_alt avg `-0.0204` n `230`; crypto_major avg `0.0217` n `8`; equity avg `0.0458` n `92`; fx avg `0.0007` n `6`; index avg `0.0035` n `25`; metal avg `-0.0049` n `20`; unknown avg `-0.0538` n `765`
- 1h: commodity avg `-0.0234` n `12`; crypto_alt avg `-0.4104` n `230`; crypto_major avg `-0.3751` n `8`; equity avg `-0.0597` n `92`; fx avg `-0.0139` n `6`; index avg `-0.0106` n `25`; metal avg `-0.0068` n `20`; unknown avg `0.19` n `765`
- 4h: commodity avg `-0.0717` n `12`; crypto_alt avg `0.1562` n `230`; crypto_major avg `0.3137` n `8`; equity avg `-0.0593` n `92`; fx avg `-0.0298` n `6`; index avg `0.0155` n `25`; metal avg `-0.0188` n `20`; unknown avg `0.1519` n `765`
- 24h: commodity avg `0.1` n `12`; crypto_alt avg `0.7244` n `229`; crypto_major avg `0.4901` n `8`; equity avg `0.1165` n `92`; fx avg `-0.0414` n `6`; index avg `0.0419` n `25`; metal avg `0.0248` n `20`; unknown avg `2.2678` n `727`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1162`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1123`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1116`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1109`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1057`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.103`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1018`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1015`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0906`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0896`, n `668`, weak_sample_signal
