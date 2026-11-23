# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-23T02:52:40.853806+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0355` n `13`; crypto_alt avg `-0.134` n `239`; crypto_major avg `-0.0065` n `8`; equity avg `0.0474` n `166`; fx avg `0.012` n `6`; index avg `-0.0476` n `27`; metal avg `0.0594` n `20`; unknown avg `0.1475` n `1265`
- 1h: commodity avg `-0.0877` n `13`; crypto_alt avg `-0.5406` n `239`; crypto_major avg `-0.3773` n `8`; equity avg `-0.8988` n `166`; fx avg `0.0182` n `6`; index avg `-0.1554` n `27`; metal avg `-0.2117` n `20`; unknown avg `159.0991` n `1257`
- 4h: commodity avg `-0.348` n `13`; crypto_alt avg `-0.6625` n `239`; crypto_major avg `-0.6759` n `8`; equity avg `-0.5788` n `166`; fx avg `0.1144` n `6`; index avg `-0.0701` n `27`; metal avg `0.0626` n `20`; unknown avg `40.2388` n `1234`
- 24h: commodity avg `-0.4537` n `13`; crypto_alt avg `0.5194` n `239`; crypto_major avg `0.8751` n `8`; equity avg `0.6237` n `166`; fx avg `0.1997` n `6`; index avg `0.0564` n `27`; metal avg `0.1138` n `20`; unknown avg `244.4271` n `1025`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.1673`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1664`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1548`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1445`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1411`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1398`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.133`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1307`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1268`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1216`, n `668`, weak_sample_signal
