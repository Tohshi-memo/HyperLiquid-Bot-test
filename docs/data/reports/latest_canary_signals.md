# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-29T00:37:29.516541+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0058` n `12`; crypto_alt avg `0.3811` n `234`; crypto_major avg `0.3244` n `8`; equity avg `0.097` n `141`; fx avg `-0.005` n `6`; index avg `0.0174` n `26`; metal avg `0.0625` n `20`; unknown avg `0.3203` n `963`
- 1h: commodity avg `-0.0239` n `12`; crypto_alt avg `0.2904` n `234`; crypto_major avg `0.1292` n `8`; equity avg `-0.0082` n `141`; fx avg `0.0168` n `6`; index avg `-0.0125` n `26`; metal avg `-0.0101` n `20`; unknown avg `-0.0866` n `955`
- 4h: commodity avg `-0.0416` n `12`; crypto_alt avg `0.6663` n `234`; crypto_major avg `0.0856` n `8`; equity avg `0.1412` n `141`; fx avg `-0.0114` n `6`; index avg `0.0144` n `26`; metal avg `0.0471` n `20`; unknown avg `-0.0656` n `929`
- 24h: commodity avg `0.0762` n `12`; crypto_alt avg `-2.9512` n `234`; crypto_major avg `-1.4305` n `8`; equity avg `-2.7183` n `141`; fx avg `-0.0373` n `6`; index avg `-0.2597` n `26`; metal avg `-0.7742` n `20`; unknown avg `152.0863` n `804`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.1757`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1636`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1322`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1137`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1096`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1059`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0997`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0951`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.088`, n `668`, weak_sample_signal
