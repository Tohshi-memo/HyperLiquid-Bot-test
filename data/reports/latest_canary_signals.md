# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-22T22:22:25.894541+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.19` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0068` n `12`; crypto_alt avg `-0.1213` n `228`; crypto_major avg `-0.0807` n `8`; equity avg `-0.0502` n `86`; fx avg `-0.0005` n `6`; index avg `0.0077` n `23`; metal avg `0.0196` n `20`; unknown avg `0.4651` n `716`
- 1h: commodity avg `-0.0143` n `12`; crypto_alt avg `-0.1971` n `228`; crypto_major avg `-0.1064` n `8`; equity avg `-0.0352` n `86`; fx avg `-0.0065` n `6`; index avg `0.0151` n `23`; metal avg `0.0254` n `20`; unknown avg `0.6828` n `716`
- 4h: commodity avg `0.0479` n `12`; crypto_alt avg `-1.0525` n `228`; crypto_major avg `-1.2056` n `8`; equity avg `-0.536` n `86`; fx avg `-0.024` n `6`; index avg `-0.0156` n `23`; metal avg `0.037` n `20`; unknown avg `1.9082` n `708`
- 24h: commodity avg `-0.9112` n `12`; crypto_alt avg `-0.1283` n `228`; crypto_major avg `0.0942` n `8`; equity avg `-0.4363` n `85`; fx avg `0.0871` n `6`; index avg `0.1817` n `23`; metal avg `0.4291` n `18`; unknown avg `0.5995` n `631`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1088`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1041`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0949`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0846`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0818`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0815`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0794`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0672`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0625`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0612`, n `668`, weak_sample_signal
