# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-29T05:52:34.747809+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0705` n `12`; crypto_alt avg `0.8804` n `234`; crypto_major avg `0.6702` n `8`; equity avg `0.2125` n `141`; fx avg `-0.0073` n `6`; index avg `0.0523` n `26`; metal avg `0.1088` n `20`; unknown avg `2.6983` n `963`
- 1h: commodity avg `-0.037` n `12`; crypto_alt avg `0.3679` n `234`; crypto_major avg `0.2518` n `8`; equity avg `-0.0709` n `141`; fx avg `-0.0258` n `6`; index avg `-0.0129` n `26`; metal avg `0.0319` n `20`; unknown avg `1.2462` n `961`
- 4h: commodity avg `0.0435` n `12`; crypto_alt avg `0.796` n `234`; crypto_major avg `0.6939` n `8`; equity avg `-0.3853` n `141`; fx avg `-0.0647` n `6`; index avg `-0.1012` n `26`; metal avg `-0.0346` n `20`; unknown avg `0.6278` n `955`
- 24h: commodity avg `0.0284` n `12`; crypto_alt avg `-1.3795` n `234`; crypto_major avg `-0.1761` n `8`; equity avg `-2.0567` n `141`; fx avg `-0.1302` n `6`; index avg `-0.2331` n `26`; metal avg `-0.3805` n `20`; unknown avg `9.2005` n `810`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.1774`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1669`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.136`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1346`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1202`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.116`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1102`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0981`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0892`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0866`, n `668`, weak_sample_signal
