# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-29T06:37:35.279087+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0194` n `12`; crypto_alt avg `0.0718` n `234`; crypto_major avg `-0.0356` n `8`; equity avg `0.0725` n `141`; fx avg `-0.0002` n `6`; index avg `0.0281` n `26`; metal avg `0.0358` n `20`; unknown avg `1.4605` n `961`
- 1h: commodity avg `-0.1275` n `12`; crypto_alt avg `1.5395` n `234`; crypto_major avg `1.2664` n `8`; equity avg `0.8061` n `141`; fx avg `-0.0009` n `6`; index avg `0.1726` n `26`; metal avg `0.1925` n `20`; unknown avg `2.5696` n `943`
- 4h: commodity avg `0.0288` n `12`; crypto_alt avg `2.2481` n `234`; crypto_major avg `1.5238` n `8`; equity avg `0.3431` n `141`; fx avg `-0.0251` n `6`; index avg `0.0438` n `26`; metal avg `0.0567` n `20`; unknown avg `2.8244` n `937`
- 24h: commodity avg `0.0318` n `12`; crypto_alt avg `-0.4545` n `234`; crypto_major avg `0.5634` n `8`; equity avg `-1.4081` n `141`; fx avg `-0.1238` n `6`; index avg `-0.0723` n `26`; metal avg `-0.3027` n `20`; unknown avg `60.9377` n `808`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.1778`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.167`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1402`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1377`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1277`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1193`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1175`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1056`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0932`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0926`, n `668`, weak_sample_signal
