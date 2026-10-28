# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-28T11:22:29.068049+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.45` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0029` n `13`; crypto_alt avg `-0.0134` n `238`; crypto_major avg `-0.0288` n `8`; equity avg `-0.0663` n `154`; fx avg `0.0145` n `6`; index avg `0.0036` n `27`; metal avg `0.0023` n `20`; unknown avg `0.1121` n `1237`
- 1h: commodity avg `0.0814` n `13`; crypto_alt avg `-0.1994` n `238`; crypto_major avg `-0.2777` n `8`; equity avg `0.0209` n `154`; fx avg `0.0099` n `6`; index avg `0.0084` n `27`; metal avg `0.0086` n `20`; unknown avg `1.438` n `1235`
- 4h: commodity avg `0.0151` n `13`; crypto_alt avg `0.6243` n `238`; crypto_major avg `0.5828` n `8`; equity avg `0.0567` n `154`; fx avg `0.0444` n `6`; index avg `0.0028` n `27`; metal avg `-0.0148` n `20`; unknown avg `87.5856` n `1186`
- 24h: commodity avg `0.2446` n `13`; crypto_alt avg `2.2123` n `238`; crypto_major avg `2.4238` n `8`; equity avg `2.9995` n `154`; fx avg `0.1036` n `6`; index avg `0.392` n `27`; metal avg `0.2327` n `20`; unknown avg `7.7007` n `1070`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1679`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1457`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1439`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1046`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.098`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0741`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.0629`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0607`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0598`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0591`, n `668`, weak_sample_signal
