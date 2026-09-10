# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-10T03:37:30.095834+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.012` n `12`; crypto_alt avg `-0.1015` n `233`; crypto_major avg `-0.1131` n `8`; equity avg `-0.0193` n `134`; fx avg `-0.0123` n `6`; index avg `0.001` n `26`; metal avg `-0.0154` n `20`; unknown avg `0.3354` n `797`
- 1h: commodity avg `-0.0505` n `12`; crypto_alt avg `0.3225` n `233`; crypto_major avg `0.2396` n `8`; equity avg `0.0752` n `134`; fx avg `0.0028` n `6`; index avg `0.0237` n `26`; metal avg `-0.04` n `20`; unknown avg `120.8708` n `795`
- 4h: commodity avg `-0.2367` n `12`; crypto_alt avg `-0.3463` n `233`; crypto_major avg `0.1609` n `8`; equity avg `-0.2832` n `134`; fx avg `0.0071` n `6`; index avg `0.027` n `26`; metal avg `0.01` n `20`; unknown avg `8.2282` n `789`
- 24h: commodity avg `-0.0463` n `12`; crypto_alt avg `-2.6722` n `233`; crypto_major avg `-1.5968` n `8`; equity avg `-1.2438` n `134`; fx avg `0.0136` n `6`; index avg `-0.2103` n `26`; metal avg `0.401` n `20`; unknown avg `1.1798` n `667`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.129`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1157`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1061`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1046`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1005`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0994`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0985`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0947`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0848`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0844`, n `668`, weak_sample_signal
