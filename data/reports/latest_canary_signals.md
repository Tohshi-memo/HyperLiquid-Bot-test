# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-29T04:37:29.467760+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0248` n `12`; crypto_alt avg `-0.2848` n `234`; crypto_major avg `-0.2502` n `8`; equity avg `-0.045` n `141`; fx avg `0.007` n `6`; index avg `-0.0059` n `26`; metal avg `-0.0221` n `20`; unknown avg `0.2976` n `963`
- 1h: commodity avg `0.0529` n `12`; crypto_alt avg `0.0809` n `234`; crypto_major avg `-0.0689` n `8`; equity avg `-0.1489` n `141`; fx avg `-0.0046` n `6`; index avg `-0.0436` n `26`; metal avg `-0.0937` n `20`; unknown avg `11.6328` n `955`
- 4h: commodity avg `0.2006` n `12`; crypto_alt avg `-1.503` n `234`; crypto_major avg `-0.7615` n `8`; equity avg `-0.6081` n `141`; fx avg `-0.032` n `6`; index avg `-0.1134` n `26`; metal avg `-0.1278` n `20`; unknown avg `0.6514` n `955`
- 24h: commodity avg `0.1312` n `12`; crypto_alt avg `-2.4279` n `234`; crypto_major avg `-1.1062` n `8`; equity avg `-2.27` n `141`; fx avg `-0.0608` n `6`; index avg `-0.2604` n `26`; metal avg `-0.5521` n `20`; unknown avg `7.8433` n `810`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.177`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1662`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1306`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1227`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1186`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1157`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1104`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1002`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0977`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0925`, n `668`, weak_sample_signal
