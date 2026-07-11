# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-11T12:37:28.855666+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0114` n `12`; crypto_alt avg `0.0056` n `230`; crypto_major avg `-0.0309` n `8`; equity avg `0.0212` n `92`; fx avg `0.003` n `6`; index avg `0.0002` n `25`; metal avg `0.0008` n `20`; unknown avg `-0.0008` n `765`
- 1h: commodity avg `0.0578` n `12`; crypto_alt avg `0.0313` n `230`; crypto_major avg `-0.0216` n `8`; equity avg `-0.0012` n `92`; fx avg `0.0026` n `6`; index avg `-0.0007` n `25`; metal avg `-0.0076` n `20`; unknown avg `-0.0067` n `765`
- 4h: commodity avg `0.052` n `12`; crypto_alt avg `0.1967` n `230`; crypto_major avg `0.0571` n `8`; equity avg `0.02` n `92`; fx avg `-0.0081` n `6`; index avg `0.0006` n `25`; metal avg `-0.013` n `20`; unknown avg `-0.2142` n `761`
- 24h: commodity avg `-0.1693` n `12`; crypto_alt avg `0.2165` n `229`; crypto_major avg `-0.4709` n `8`; equity avg `-0.3336` n `92`; fx avg `-0.0988` n `6`; index avg `0.1189` n `25`; metal avg `0.1638` n `20`; unknown avg `2.8666` n `727`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1152`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1118`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1056`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1055`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1045`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1024`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1019`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0999`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0907`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0899`, n `668`, weak_sample_signal
