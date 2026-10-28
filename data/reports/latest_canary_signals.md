# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-28T05:07:29.005482+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.6` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0025` n `13`; crypto_alt avg `-0.1332` n `238`; crypto_major avg `-0.1329` n `8`; equity avg `0.0394` n `154`; fx avg `-0.0245` n `6`; index avg `0.0131` n `27`; metal avg `-0.0177` n `20`; unknown avg `0.3424` n `1232`
- 1h: commodity avg `0.0322` n `13`; crypto_alt avg `-0.1094` n `238`; crypto_major avg `-0.094` n `8`; equity avg `-0.1265` n `154`; fx avg `-0.0133` n `6`; index avg `-0.0374` n `27`; metal avg `-0.0498` n `20`; unknown avg `57.7521` n `1232`
- 4h: commodity avg `0.0192` n `13`; crypto_alt avg `0.2229` n `238`; crypto_major avg `0.2569` n `8`; equity avg `0.6137` n `154`; fx avg `0.0774` n `6`; index avg `0.0171` n `27`; metal avg `-0.1562` n `20`; unknown avg `22.8073` n `1214`
- 24h: commodity avg `0.0766` n `13`; crypto_alt avg `1.8829` n `237`; crypto_major avg `1.8877` n `8`; equity avg `3.137` n `154`; fx avg `0.1078` n `6`; index avg `0.3657` n `27`; metal avg `0.1714` n `20`; unknown avg `16.0015` n `1016`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1829`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1573`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1544`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1191`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0963`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0893`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0762`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0739`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.0703`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0629`, n `668`, weak_sample_signal
