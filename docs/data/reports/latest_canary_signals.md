# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-06T18:07:21.478613+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.3352` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0415` n `12`; crypto_alt avg `-0.0925` n `228`; crypto_major avg `-0.1832` n `8`; equity avg `0.0058` n `74`; fx avg `0.0083` n `6`; index avg `-0.0122` n `23`; metal avg `0.0108` n `18`; unknown avg `0.1486` n `515`
- 1h: commodity avg `0.057` n `12`; crypto_alt avg `-0.6903` n `228`; crypto_major avg `-0.6213` n `8`; equity avg `-0.1773` n `74`; fx avg `0.1277` n `6`; index avg `-0.1305` n `23`; metal avg `0.0367` n `18`; unknown avg `0.8651` n `515`
- 4h: commodity avg `0.207` n `12`; crypto_alt avg `-1.3739` n `228`; crypto_major avg `-1.3122` n `8`; equity avg `-0.1487` n `74`; fx avg `0.1868` n `6`; index avg `0.023` n `23`; metal avg `-0.0456` n `18`; unknown avg `-3.7631` n `515`
- 24h: commodity avg `0.5226` n `12`; crypto_alt avg `-2.8554` n `228`; crypto_major avg `-2.223` n `8`; equity avg `-1.7734` n `74`; fx avg `0.1545` n `6`; index avg `-0.9391` n `23`; metal avg `-1.0001` n `18`; unknown avg `-0.6866` n `400`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.1244`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1194`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0958`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0871`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0764`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0677`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0639`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0589`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0549`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0511`, n `668`, weak_sample_signal
