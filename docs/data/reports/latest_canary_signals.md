# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-22T08:37:31.610318+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.66` - Polymarket crypto volume is unusually high.
- 4h_index_leads_crypto: score `1.0113` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0679` n `13`; crypto_alt avg `-0.417` n `237`; crypto_major avg `-0.3306` n `8`; equity avg `-0.0277` n `151`; fx avg `-0.0066` n `6`; index avg `-0.0001` n `26`; metal avg `-0.0334` n `20`; unknown avg `44.8248` n `1201`
- 1h: commodity avg `0.0665` n `13`; crypto_alt avg `-0.8115` n `237`; crypto_major avg `-0.667` n `8`; equity avg `-0.2871` n `151`; fx avg `0.0016` n `6`; index avg `-0.0292` n `26`; metal avg `-0.0358` n `20`; unknown avg `10.566` n `1181`
- 4h: commodity avg `0.3408` n `13`; crypto_alt avg `-1.7454` n `237`; crypto_major avg `-1.1298` n `8`; equity avg `-0.6578` n `151`; fx avg `-0.076` n `6`; index avg `-0.1185` n `26`; metal avg `-0.1153` n `20`; unknown avg `5.8668` n `1151`
- 24h: commodity avg `-0.1225` n `13`; crypto_alt avg `-2.8486` n `237`; crypto_major avg `-2.128` n `8`; equity avg `-2.4558` n `151`; fx avg `-0.1085` n `6`; index avg `-0.388` n `26`; metal avg `-0.5972` n `20`; unknown avg `135.9786` n `928`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1571`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1494`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1397`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1376`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.128`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1257`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1212`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.121`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1129`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1029`, n `668`, weak_sample_signal
