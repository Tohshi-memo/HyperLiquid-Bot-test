# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-30T08:37:31.474712+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.2` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0009` n `12`; crypto_alt avg `-0.2654` n `234`; crypto_major avg `-0.1914` n `8`; equity avg `0.0019` n `142`; fx avg `-0.001` n `6`; index avg `0.007` n `26`; metal avg `-0.0072` n `20`; unknown avg `0.5313` n `963`
- 1h: commodity avg `0.1386` n `12`; crypto_alt avg `-0.1533` n `234`; crypto_major avg `-0.3152` n `8`; equity avg `-0.0374` n `142`; fx avg `0.0211` n `6`; index avg `-0.006` n `26`; metal avg `-0.0182` n `20`; unknown avg `1.3565` n `945`
- 4h: commodity avg `0.016` n `12`; crypto_alt avg `-0.13` n `234`; crypto_major avg `-0.3695` n `8`; equity avg `-0.0133` n `142`; fx avg `0.0144` n `6`; index avg `0.0145` n `26`; metal avg `0.1654` n `20`; unknown avg `0.7017` n `915`
- 24h: commodity avg `-0.6441` n `12`; crypto_alt avg `-0.2578` n `234`; crypto_major avg `-1.1199` n `8`; equity avg `0.234` n `142`; fx avg `-0.0587` n `6`; index avg `0.0935` n `26`; metal avg `0.388` n `20`; unknown avg `2914.6454` n `826`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `-0.1567`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1531`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1451`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1391`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1318`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1229`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1155`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1113`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1093`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0972`, n `668`, weak_sample_signal
