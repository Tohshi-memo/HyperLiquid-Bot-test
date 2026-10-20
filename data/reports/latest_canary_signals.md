# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-20T18:52:36.380365+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.015` n `13`; crypto_alt avg `0.0373` n `237`; crypto_major avg `0.0033` n `8`; equity avg `0.1589` n `151`; fx avg `0.0055` n `6`; index avg `0.0134` n `26`; metal avg `-0.0047` n `20`; unknown avg `2.8766` n `1199`
- 1h: commodity avg `0.0693` n `13`; crypto_alt avg `-0.5266` n `237`; crypto_major avg `-0.4131` n `8`; equity avg `-0.2265` n `151`; fx avg `0.0108` n `6`; index avg `-0.0529` n `26`; metal avg `-0.039` n `20`; unknown avg `22.6347` n `1191`
- 4h: commodity avg `0.3773` n `13`; crypto_alt avg `-0.769` n `237`; crypto_major avg `-0.7778` n `8`; equity avg `-0.5969` n `151`; fx avg `0.006` n `6`; index avg `-0.1103` n `26`; metal avg `-0.1552` n `20`; unknown avg `11.2885` n `1177`
- 24h: commodity avg `-0.1188` n `13`; crypto_alt avg `2.4178` n `237`; crypto_major avg `1.3592` n `8`; equity avg `0.1279` n `151`; fx avg `0.0361` n `6`; index avg `-0.0062` n `26`; metal avg `-0.0489` n `20`; unknown avg `4.241` n `1044`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1797`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.139`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1092`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1078`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1023`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.094`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0852`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0821`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0766`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.076`, n `668`, weak_sample_signal
