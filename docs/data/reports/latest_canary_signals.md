# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-08T21:22:37.485374+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0065` n `12`; crypto_alt avg `-0.1345` n `233`; crypto_major avg `-0.0574` n `8`; equity avg `-0.0012` n `134`; fx avg `-0.0092` n `6`; index avg `-0.0113` n `26`; metal avg `0.0045` n `20`; unknown avg `61.5173` n `797`
- 1h: commodity avg `0.0264` n `12`; crypto_alt avg `-0.2447` n `233`; crypto_major avg `-0.0312` n `8`; equity avg `0.0083` n `134`; fx avg `-0.0128` n `6`; index avg `-0.0193` n `26`; metal avg `0.0017` n `20`; unknown avg `2.26` n `789`
- 4h: commodity avg `0.39` n `12`; crypto_alt avg `-0.7742` n `233`; crypto_major avg `-0.2314` n `8`; equity avg `-0.5905` n `134`; fx avg `-0.0532` n `6`; index avg `-0.1157` n `26`; metal avg `-0.2508` n `20`; unknown avg `0.2966` n `765`
- 24h: commodity avg `0.086` n `12`; crypto_alt avg `-0.743` n `232`; crypto_major avg `-0.1945` n `8`; equity avg `0.2867` n `134`; fx avg `-0.1066` n `6`; index avg `-0.1832` n `26`; metal avg `-0.2961` n `20`; unknown avg `5.8766` n `714`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `0.1308`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1034`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0978`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.087`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0827`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0815`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0802`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0802`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0768`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0755`, n `668`, weak_sample_signal
