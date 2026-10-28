# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-28T07:22:34.353891+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.57` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0008` n `13`; crypto_alt avg `-0.0664` n `238`; crypto_major avg `0.0157` n `8`; equity avg `0.0875` n `154`; fx avg `-0.0227` n `6`; index avg `0.0098` n `27`; metal avg `0.0167` n `20`; unknown avg `0.0637` n `1234`
- 1h: commodity avg `0.0662` n `13`; crypto_alt avg `-0.4345` n `238`; crypto_major avg `-0.1278` n `8`; equity avg `0.1705` n `154`; fx avg `-0.0041` n `6`; index avg `0.0256` n `27`; metal avg `0.0031` n `20`; unknown avg `0.5362` n `1228`
- 4h: commodity avg `0.1641` n `13`; crypto_alt avg `-0.4589` n `238`; crypto_major avg `-0.133` n `8`; equity avg `0.2739` n `154`; fx avg `-0.0548` n `6`; index avg `0.0164` n `27`; metal avg `-0.0862` n `20`; unknown avg `0.6453` n `1202`
- 24h: commodity avg `-0.0809` n `13`; crypto_alt avg `1.5014` n `238`; crypto_major avg `2.0681` n `8`; equity avg `4.2438` n `154`; fx avg `0.0525` n `6`; index avg `0.5743` n `27`; metal avg `0.3583` n `20`; unknown avg `16.5057` n `1014`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.173`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1713`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.161`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1085`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1039`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.074`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0675`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0637`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.0637`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0623`, n `668`, weak_sample_signal
