# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-28T07:07:25.619720+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.6` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0279` n `13`; crypto_alt avg `-0.0989` n `238`; crypto_major avg `0.0215` n `8`; equity avg `0.0188` n `154`; fx avg `0.0126` n `6`; index avg `0.0041` n `27`; metal avg `0.0115` n `20`; unknown avg `162.4055` n `1230`
- 1h: commodity avg `0.0864` n `13`; crypto_alt avg `-0.1862` n `238`; crypto_major avg `-0.0249` n `8`; equity avg `0.0994` n `154`; fx avg `0.0174` n `6`; index avg `0.0079` n `27`; metal avg `-0.0079` n `20`; unknown avg `-0.2907` n `1228`
- 4h: commodity avg `0.1664` n `13`; crypto_alt avg `-0.4199` n `238`; crypto_major avg `-0.0674` n `8`; equity avg `0.4041` n `154`; fx avg `-0.0227` n `6`; index avg `0.0176` n `27`; metal avg `-0.0931` n `20`; unknown avg `0.391` n `1202`
- 24h: commodity avg `-0.0746` n `13`; crypto_alt avg `1.8514` n `238`; crypto_major avg `2.2267` n `8`; equity avg `4.2356` n `154`; fx avg `0.0966` n `6`; index avg `0.5765` n `27`; metal avg `0.389` n `20`; unknown avg `92.5841` n `1014`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1761`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1734`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1631`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.109`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.102`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0744`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0691`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0645`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.0637`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0635`, n `668`, weak_sample_signal
