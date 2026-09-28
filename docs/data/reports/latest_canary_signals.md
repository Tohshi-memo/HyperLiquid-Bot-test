# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-28T07:22:36.442620+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0947` n `12`; crypto_alt avg `-0.5694` n `234`; crypto_major avg `-0.1438` n `8`; equity avg `-0.0932` n `141`; fx avg `-0.0021` n `6`; index avg `-0.0132` n `26`; metal avg `-0.028` n `20`; unknown avg `2.0153` n `962`
- 1h: commodity avg `0.065` n `12`; crypto_alt avg `-0.6072` n `234`; crypto_major avg `-0.0895` n `8`; equity avg `-0.5833` n `141`; fx avg `-0.029` n `6`; index avg `-0.0321` n `26`; metal avg `-0.1588` n `20`; unknown avg `1.6313` n `960`
- 4h: commodity avg `0.1972` n `12`; crypto_alt avg `-1.7454` n `234`; crypto_major avg `-0.9508` n `8`; equity avg `-0.8209` n `141`; fx avg `0.007` n `6`; index avg `-0.0701` n `26`; metal avg `-0.2472` n `20`; unknown avg `1.4437` n `930`
- 24h: commodity avg `-0.2791` n `12`; crypto_alt avg `-3.4627` n `234`; crypto_major avg `-2.4972` n `8`; equity avg `-2.3149` n `141`; fx avg `0.0662` n `6`; index avg `-0.2282` n `26`; metal avg `-0.9644` n `20`; unknown avg `4.0584` n `815`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.2248`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1924`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1636`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1621`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1581`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1531`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1217`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1193`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1134`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1121`, n `668`, weak_sample_signal
