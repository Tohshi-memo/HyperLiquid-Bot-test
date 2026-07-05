# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-05T02:07:26.213082+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.3181` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0076` n `12`; crypto_alt avg `-0.1642` n `229`; crypto_major avg `-0.2079` n `8`; equity avg `-0.0042` n `88`; fx avg `-0.0015` n `6`; index avg `0.0055` n `25`; metal avg `-0.0095` n `20`; unknown avg `-0.0256` n `765`
- 1h: commodity avg `0.0115` n `12`; crypto_alt avg `-0.6364` n `229`; crypto_major avg `-0.6246` n `8`; equity avg `0.0178` n `88`; fx avg `0.0042` n `6`; index avg `-0.0328` n `25`; metal avg `-0.0047` n `20`; unknown avg `0.1701` n `763`
- 4h: commodity avg `0.0235` n `12`; crypto_alt avg `-1.2321` n `229`; crypto_major avg `-1.3122` n `8`; equity avg `0.0119` n `88`; fx avg `0.0143` n `6`; index avg `0.0059` n `25`; metal avg `-0.0065` n `20`; unknown avg `-0.3209` n `763`
- 24h: commodity avg `0.0188` n `12`; crypto_alt avg `-0.3174` n `229`; crypto_major avg `-0.3437` n `8`; equity avg `0.234` n `88`; fx avg `0.0058` n `6`; index avg `0.0364` n `25`; metal avg `0.1097` n `20`; unknown avg `-0.8761` n `741`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0963`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0936`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0906`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0899`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0852`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0838`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0823`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0765`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.074`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.071`, n `668`, weak_sample_signal
