# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-20T19:07:31.723185+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0347` n `13`; crypto_alt avg `-0.0368` n `237`; crypto_major avg `0.0763` n `8`; equity avg `0.1346` n `151`; fx avg `-0.0066` n `6`; index avg `0.0203` n `26`; metal avg `0.0094` n `20`; unknown avg `9.2837` n `1197`
- 1h: commodity avg `0.1168` n `13`; crypto_alt avg `-0.2865` n `237`; crypto_major avg `-0.145` n `8`; equity avg `-0.0298` n `151`; fx avg `0.0021` n `6`; index avg `-0.0211` n `26`; metal avg `-0.0285` n `20`; unknown avg `0.4858` n `1193`
- 4h: commodity avg `0.3279` n `13`; crypto_alt avg `-0.7766` n `237`; crypto_major avg `-0.7603` n `8`; equity avg `-0.3805` n `151`; fx avg `-0.0035` n `6`; index avg `-0.0924` n `26`; metal avg `-0.1303` n `20`; unknown avg `18.4298` n `1177`
- 24h: commodity avg `-0.0803` n `13`; crypto_alt avg `2.5255` n `237`; crypto_major avg `1.6176` n `8`; equity avg `0.257` n `151`; fx avg `0.0262` n `6`; index avg `0.0083` n `26`; metal avg `-0.0054` n `20`; unknown avg `4.4375` n `1044`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1799`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1394`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1092`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1075`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1019`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0941`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0852`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0815`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0762`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0756`, n `668`, weak_sample_signal
