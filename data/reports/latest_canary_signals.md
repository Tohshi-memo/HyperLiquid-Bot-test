# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-04T17:37:28.459153+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0501` n `12`; crypto_alt avg `-0.1155` n `232`; crypto_major avg `-0.1702` n `8`; equity avg `-0.0863` n `133`; fx avg `-0.0004` n `6`; index avg `-0.0219` n `26`; metal avg `-0.0743` n `20`; unknown avg `0.181` n `793`
- 1h: commodity avg `0.0924` n `12`; crypto_alt avg `-0.2793` n `232`; crypto_major avg `-0.3627` n `8`; equity avg `-0.1356` n `133`; fx avg `-0.0082` n `6`; index avg `-0.0431` n `26`; metal avg `-0.0905` n `20`; unknown avg `1.2219` n `791`
- 4h: commodity avg `0.3477` n `12`; crypto_alt avg `0.2774` n `232`; crypto_major avg `-0.2772` n `8`; equity avg `0.6175` n `133`; fx avg `0.0475` n `6`; index avg `0.0389` n `26`; metal avg `-0.0015` n `20`; unknown avg `0.4189` n `767`
- 24h: commodity avg `0.0511` n `12`; crypto_alt avg `-1.3561` n `232`; crypto_major avg `-2.2434` n `8`; equity avg `1.4032` n `133`; fx avg `-0.1168` n `6`; index avg `0.1666` n `26`; metal avg `-0.4314` n `20`; unknown avg `0.8319` n `686`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1454`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1283`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1279`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1083`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0982`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0953`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.091`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0867`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.085`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0837`, n `668`, weak_sample_signal
