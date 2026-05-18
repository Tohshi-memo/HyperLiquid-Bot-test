# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-18T10:07:17.924850+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1138` n `12`; crypto_alt avg `-0.1967` n `228`; crypto_major avg `-0.0201` n `8`; equity avg `-0.2034` n `66`; fx avg `0.0053` n `5`; index avg `-0.1149` n `23`; metal avg `0.0746` n `18`; unknown avg `0.0068` n `383`
- 1h: commodity avg `0.0861` n `12`; crypto_alt avg `-0.4051` n `228`; crypto_major avg `-0.2818` n `8`; equity avg `-0.367` n `66`; fx avg `0.0509` n `5`; index avg `-0.1375` n `23`; metal avg `-0.1048` n `18`; unknown avg `-0.1902` n `383`
- 4h: commodity avg `-0.1251` n `12`; crypto_alt avg `-0.6821` n `228`; crypto_major avg `-0.4745` n `8`; equity avg `0.5148` n `66`; fx avg `0.0149` n `5`; index avg `0.1775` n `23`; metal avg `0.5359` n `18`; unknown avg `-0.3489` n `383`
- 24h: commodity avg `0.7859` n `12`; crypto_alt avg `-3.5842` n `228`; crypto_major avg `-1.9837` n `8`; equity avg `0.1466` n `65`; fx avg `0.0966` n `5`; index avg `0.1461` n `23`; metal avg `0.0434` n `18`; unknown avg `-0.6919` n `363`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1458`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1265`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1208`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1175`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1138`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1116`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1116`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0902`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.083`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0824`, n `668`, weak_sample_signal
