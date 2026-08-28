# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-28T21:22:24.835450+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.0179` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0147` n `12`; crypto_alt avg `-0.1266` n `231`; crypto_major avg `-0.1029` n `8`; equity avg `-0.037` n `127`; fx avg `0.0196` n `6`; index avg `0.0008` n `26`; metal avg `-0.0103` n `20`; unknown avg `0.0537` n `793`
- 1h: commodity avg `0.022` n `12`; crypto_alt avg `-0.1578` n `231`; crypto_major avg `-0.0818` n `8`; equity avg `-0.0069` n `127`; fx avg `-0.0125` n `6`; index avg `0.0106` n `26`; metal avg `0.0361` n `20`; unknown avg `-0.0696` n `793`
- 4h: commodity avg `0.0536` n `12`; crypto_alt avg `-0.6039` n `231`; crypto_major avg `-1.027` n `8`; equity avg `-0.0362` n `127`; fx avg `-0.0304` n `6`; index avg `-0.0091` n `26`; metal avg `-0.174` n `20`; unknown avg `-0.5473` n `793`
- 24h: commodity avg `-0.087` n `12`; crypto_alt avg `-3.5092` n `231`; crypto_major avg `-3.7658` n `8`; equity avg `-2.1799` n `127`; fx avg `-0.1232` n `6`; index avg `-0.1856` n `26`; metal avg `-0.358` n `20`; unknown avg `-0.7326` n `760`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1272`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1243`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1129`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1125`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1103`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.094`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0923`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0862`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0766`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0764`, n `668`, weak_sample_signal
