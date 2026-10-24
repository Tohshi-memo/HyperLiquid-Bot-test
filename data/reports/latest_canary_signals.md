# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-24T16:07:25.830621+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.1934` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0076` n `13`; crypto_alt avg `0.2704` n `237`; crypto_major avg `0.2009` n `8`; equity avg `0.0111` n `152`; fx avg `0.0088` n `6`; index avg `0.0035` n `26`; metal avg `0.0037` n `20`; unknown avg `0.0435` n `1223`
- 1h: commodity avg `-0.0081` n `13`; crypto_alt avg `-0.3285` n `237`; crypto_major avg `-0.1046` n `8`; equity avg `-0.199` n `152`; fx avg `-0.014` n `6`; index avg `-0.0238` n `26`; metal avg `-0.0452` n `20`; unknown avg `-0.2429` n `1224`
- 4h: commodity avg `-0.0115` n `13`; crypto_alt avg `-1.7565` n `237`; crypto_major avg `-1.2591` n `8`; equity avg `-0.5084` n `152`; fx avg `-0.022` n `6`; index avg `-0.0657` n `26`; metal avg `-0.1228` n `20`; unknown avg `0.6297` n `1190`
- 24h: commodity avg `0.2975` n `13`; crypto_alt avg `-4.7219` n `237`; crypto_major avg `-3.5768` n `8`; equity avg `-1.4392` n `152`; fx avg `-0.0407` n `6`; index avg `-0.1962` n `26`; metal avg `-0.3305` n `20`; unknown avg `-0.8659` n `1043`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1913`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1905`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1877`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1598`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1514`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1448`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1394`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.13`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1212`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1188`, n `668`, weak_sample_signal
