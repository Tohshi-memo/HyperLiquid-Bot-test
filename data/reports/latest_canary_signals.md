# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-10T21:52:28.436988+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.2451` n `12`; crypto_alt avg `0.0574` n `233`; crypto_major avg `0.0545` n `8`; equity avg `-0.0214` n `136`; fx avg `0.004` n `6`; index avg `-0.006` n `26`; metal avg `-0.0164` n `20`; unknown avg `8.6104` n `796`
- 1h: commodity avg `0.2586` n `12`; crypto_alt avg `-0.0391` n `233`; crypto_major avg `-0.0805` n `8`; equity avg `-0.1128` n `136`; fx avg `0.0129` n `6`; index avg `-0.0065` n `26`; metal avg `0.015` n `20`; unknown avg `10.6497` n `794`
- 4h: commodity avg `0.5943` n `12`; crypto_alt avg `-0.2654` n `233`; crypto_major avg `-0.178` n `8`; equity avg `-0.5967` n `136`; fx avg `0.0184` n `6`; index avg `-0.0192` n `26`; metal avg `-0.1764` n `20`; unknown avg `5.373` n `750`
- 24h: commodity avg `1.4469` n `12`; crypto_alt avg `-2.0869` n `233`; crypto_major avg `-1.8738` n `8`; equity avg `-2.0588` n `136`; fx avg `0.1157` n `6`; index avg `-0.3238` n `26`; metal avg `-1.2412` n `20`; unknown avg `-0.6132` n `673`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1265`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1244`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.124`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1029`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1023`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.099`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0981`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0897`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0866`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0856`, n `668`, weak_sample_signal
