# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-29T10:22:33.267490+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0052` n `12`; crypto_alt avg `-0.1605` n `234`; crypto_major avg `-0.1455` n `8`; equity avg `-0.0084` n `141`; fx avg `-0.0172` n `6`; index avg `0.0045` n `26`; metal avg `-0.0228` n `20`; unknown avg `206.5987` n `963`
- 1h: commodity avg `-0.0995` n `12`; crypto_alt avg `0.3272` n `234`; crypto_major avg `0.2196` n `8`; equity avg `0.1153` n `141`; fx avg `0.0078` n `6`; index avg `0.011` n `26`; metal avg `0.0407` n `20`; unknown avg `202.6829` n `961`
- 4h: commodity avg `-0.4447` n `12`; crypto_alt avg `1.3145` n `234`; crypto_major avg `0.43` n `8`; equity avg `0.4903` n `141`; fx avg `-0.0406` n `6`; index avg `0.0529` n `26`; metal avg `0.0524` n `20`; unknown avg `148.1609` n `943`
- 24h: commodity avg `-0.7044` n `12`; crypto_alt avg `1.8259` n `234`; crypto_major avg `1.1473` n `8`; equity avg `0.0234` n `141`; fx avg `-0.0885` n `6`; index avg `0.0022` n `26`; metal avg `-0.1899` n `20`; unknown avg `61.9853` n `808`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.1824`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1708`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1589`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1586`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1389`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1323`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1239`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.123`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1162`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1111`, n `668`, weak_sample_signal
