# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-15T09:37:27.286451+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.06` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0085` n `13`; crypto_alt avg `0.0011` n `236`; crypto_major avg `0.1043` n `8`; equity avg `-0.1559` n `151`; fx avg `0.0027` n `6`; index avg `-0.0133` n `26`; metal avg `0.0533` n `20`; unknown avg `0.3535` n `1136`
- 1h: commodity avg `-0.0006` n `13`; crypto_alt avg `-0.1059` n `236`; crypto_major avg `-0.0663` n `8`; equity avg `0.0843` n `151`; fx avg `0.0163` n `6`; index avg `0.0038` n `26`; metal avg `0.0709` n `20`; unknown avg `0.1984` n `1134`
- 4h: commodity avg `-0.0165` n `13`; crypto_alt avg `0.4428` n `236`; crypto_major avg `0.4557` n `8`; equity avg `-0.3268` n `151`; fx avg `-0.0371` n `6`; index avg `0.043` n `26`; metal avg `0.2873` n `20`; unknown avg `4.7291` n `1092`
- 24h: commodity avg `-0.3813` n `13`; crypto_alt avg `-4.0966` n `236`; crypto_major avg `-2.8812` n `8`; equity avg `-5.8144` n `151`; fx avg `0.0876` n `6`; index avg `-0.9538` n `26`; metal avg `-0.3138` n `20`; unknown avg `2.4178` n `970`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1185`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1011`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1004`, n `666`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0889`, n `666`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0776`, n `666`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0691`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0675`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0668`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0632`, n `666`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.063`, n `668`, weak_sample_signal
