# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-26T03:07:26.293400+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.3244` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0527` n `12`; crypto_alt avg `-0.1086` n `228`; crypto_major avg `0.1135` n `8`; equity avg `-0.1058` n `86`; fx avg `-0.0144` n `6`; index avg `-0.0488` n `23`; metal avg `0.0624` n `20`; unknown avg `0.2583` n `765`
- 1h: commodity avg `-0.1101` n `12`; crypto_alt avg `-1.4548` n `228`; crypto_major avg `-1.2496` n `8`; equity avg `-1.1829` n `86`; fx avg `-0.0199` n `6`; index avg `-0.2521` n `23`; metal avg `-0.3274` n `20`; unknown avg `1.2341` n `765`
- 4h: commodity avg `-0.1418` n `12`; crypto_alt avg `-1.901` n `228`; crypto_major avg `-1.8098` n `8`; equity avg `-2.2155` n `86`; fx avg `0.0196` n `6`; index avg `-0.4854` n `23`; metal avg `-0.61` n `20`; unknown avg `-0.4726` n `749`
- 24h: commodity avg `0.3666` n `12`; crypto_alt avg `-3.1818` n `228`; crypto_major avg `-3.1487` n `8`; equity avg `-4.1966` n `86`; fx avg `0.0381` n `6`; index avg `-0.6788` n `23`; metal avg `-0.023` n `20`; unknown avg `0.1662` n `716`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1351`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1145`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1021`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0973`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0893`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.071`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0704`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0691`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0631`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0597`, n `668`, weak_sample_signal
