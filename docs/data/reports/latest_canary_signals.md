# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-16T16:52:37.208424+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.0903` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.1213` n `12`; crypto_alt avg `0.1088` n `228`; crypto_major avg `0.1261` n `8`; equity avg `0.1696` n `77`; fx avg `-0.0108` n `6`; index avg `0.1022` n `23`; metal avg `0.0055` n `18`; unknown avg `0.0689` n `687`
- 1h: commodity avg `0.0203` n `12`; crypto_alt avg `-0.1247` n `228`; crypto_major avg `-0.2222` n `8`; equity avg `0.2253` n `77`; fx avg `0.0032` n `6`; index avg `0.1135` n `23`; metal avg `0.2791` n `18`; unknown avg `-0.0785` n `687`
- 4h: commodity avg `-0.0947` n `12`; crypto_alt avg `-1.4834` n `228`; crypto_major avg `-1.7233` n `8`; equity avg `-0.8025` n `77`; fx avg `0.0662` n `6`; index avg `-0.633` n `23`; metal avg `-0.2617` n `18`; unknown avg `0.8203` n `687`
- 24h: commodity avg `-0.9586` n `12`; crypto_alt avg `-2.2867` n `228`; crypto_major avg `-1.683` n `8`; equity avg `-0.8126` n `77`; fx avg `-0.0136` n `6`; index avg `-0.7132` n `23`; metal avg `0.3953` n `18`; unknown avg `0.3284` n `623`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `0.0758`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0658`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0633`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0629`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0602`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0554`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0478`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0472`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0454`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.044`, n `668`, weak_sample_signal
