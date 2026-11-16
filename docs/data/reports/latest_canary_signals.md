# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-16T02:07:35.795456+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0021` n `13`; crypto_alt avg `0.4328` n `239`; crypto_major avg `0.4566` n `8`; equity avg `0.5086` n `162`; fx avg `-0.0061` n `6`; index avg `0.0522` n `27`; metal avg `0.1336` n `20`; unknown avg `0.1991` n `1261`
- 1h: commodity avg `-0.0558` n `13`; crypto_alt avg `-0.1162` n `239`; crypto_major avg `-0.0373` n `8`; equity avg `-0.5107` n `162`; fx avg `0.0075` n `6`; index avg `-0.0528` n `27`; metal avg `-0.2237` n `20`; unknown avg `0.932` n `1259`
- 4h: commodity avg `-0.2631` n `13`; crypto_alt avg `-0.4535` n `239`; crypto_major avg `-0.4488` n `8`; equity avg `-0.2011` n `162`; fx avg `-0.0184` n `6`; index avg `0.0001` n `27`; metal avg `0.0093` n `20`; unknown avg `0.4195` n `1201`
- 24h: commodity avg `-0.3739` n `13`; crypto_alt avg `1.512` n `239`; crypto_major avg `2.641` n `8`; equity avg `1.0134` n `162`; fx avg `-0.0003` n `6`; index avg `0.1116` n `27`; metal avg `0.3251` n `20`; unknown avg `21.0597` n `1129`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.134`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1151`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1147`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1115`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1076`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1024`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0983`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0954`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0914`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0878`, n `668`, weak_sample_signal
