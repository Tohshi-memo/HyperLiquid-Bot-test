# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-13T07:22:25.078492+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.012` n `12`; crypto_alt avg `0.0464` n `230`; crypto_major avg `0.123` n `8`; equity avg `0.1285` n `92`; fx avg `-0.0081` n `6`; index avg `0.0315` n `25`; metal avg `0.0336` n `20`; unknown avg `0.0197` n `766`
- 1h: commodity avg `-0.0625` n `12`; crypto_alt avg `0.1478` n `230`; crypto_major avg `0.18` n `8`; equity avg `0.2112` n `92`; fx avg `-0.0214` n `6`; index avg `0.0882` n `25`; metal avg `0.1037` n `20`; unknown avg `0.1107` n `766`
- 4h: commodity avg `-0.0455` n `12`; crypto_alt avg `0.7018` n `230`; crypto_major avg `-0.0347` n `8`; equity avg `-0.2152` n `92`; fx avg `-0.0191` n `6`; index avg `-0.0424` n `25`; metal avg `0.1155` n `20`; unknown avg `0.0058` n `750`
- 24h: commodity avg `0.0235` n `12`; crypto_alt avg `-1.2478` n `230`; crypto_major avg `-1.0156` n `8`; equity avg `-2.2669` n `92`; fx avg `0.0148` n `6`; index avg `-0.4522` n `25`; metal avg `-0.3643` n `20`; unknown avg `-0.0578` n `743`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1858`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1714`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1292`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1071`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1003`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0999`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0994`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0953`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0911`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0865`, n `668`, weak_sample_signal
