# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-23T02:07:29.774487+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0799` n `13`; crypto_alt avg `-0.1549` n `237`; crypto_major avg `-0.2635` n `8`; equity avg `-0.2964` n `151`; fx avg `-0.0023` n `6`; index avg `-0.0571` n `26`; metal avg `0.0039` n `20`; unknown avg `0.0239` n `1231`
- 1h: commodity avg `0.1341` n `13`; crypto_alt avg `0.456` n `237`; crypto_major avg `0.1445` n `8`; equity avg `-0.1285` n `151`; fx avg `0.0408` n `6`; index avg `-0.0836` n `26`; metal avg `-0.0932` n `20`; unknown avg `-0.1131` n `1231`
- 4h: commodity avg `0.1995` n `13`; crypto_alt avg `0.2733` n `237`; crypto_major avg `0.0574` n `8`; equity avg `0.282` n `151`; fx avg `-0.0366` n `6`; index avg `-0.0706` n `26`; metal avg `-0.1957` n `20`; unknown avg `0.0436` n `1185`
- 24h: commodity avg `0.5454` n `13`; crypto_alt avg `-3.033` n `237`; crypto_major avg `-2.0037` n `8`; equity avg `-3.8308` n `151`; fx avg `-0.1592` n `6`; index avg `-0.5153` n `26`; metal avg `-0.7797` n `20`; unknown avg `52.7789` n `905`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1871`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1806`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1757`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1509`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1495`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1482`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1354`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1179`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1142`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0998`, n `668`, weak_sample_signal
