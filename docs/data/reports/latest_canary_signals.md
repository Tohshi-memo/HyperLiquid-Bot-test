# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-04T09:52:34.650730+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.109` n `12`; crypto_alt avg `0.0162` n `230`; crypto_major avg `0.0348` n `8`; equity avg `0.0388` n `107`; fx avg `-0.0012` n `6`; index avg `0.0002` n `25`; metal avg `0.0199` n `20`; unknown avg `0.0156` n `781`
- 1h: commodity avg `0.0147` n `12`; crypto_alt avg `-0.1834` n `230`; crypto_major avg `-0.1279` n `8`; equity avg `-0.229` n `107`; fx avg `0.0091` n `6`; index avg `-0.027` n `25`; metal avg `-0.018` n `20`; unknown avg `0.0696` n `781`
- 4h: commodity avg `0.2096` n `12`; crypto_alt avg `-0.2798` n `230`; crypto_major avg `-0.2142` n `8`; equity avg `0.1698` n `107`; fx avg `0.0692` n `6`; index avg `-0.0118` n `25`; metal avg `0.0089` n `20`; unknown avg `0.9094` n `765`
- 24h: commodity avg `0.4545` n `12`; crypto_alt avg `0.7555` n `230`; crypto_major avg `0.9966` n `8`; equity avg `3.2679` n `107`; fx avg `0.0925` n `6`; index avg `0.3343` n `25`; metal avg `0.1309` n `20`; unknown avg `1.0655` n `763`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1395`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1227`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1158`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0839`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0838`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.083`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0818`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0795`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0781`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0751`, n `668`, weak_sample_signal
