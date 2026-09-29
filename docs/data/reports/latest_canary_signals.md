# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-29T09:07:38.994173+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0648` n `12`; crypto_alt avg `-0.0588` n `234`; crypto_major avg `-0.0341` n `8`; equity avg `-0.0717` n `141`; fx avg `-0.0028` n `6`; index avg `-0.0025` n `26`; metal avg `0.0093` n `20`; unknown avg `-0.1175` n `961`
- 1h: commodity avg `-0.2507` n `12`; crypto_alt avg `0.0531` n `234`; crypto_major avg `-0.2553` n `8`; equity avg `0.0746` n `141`; fx avg `-0.0221` n `6`; index avg `0.0096` n `26`; metal avg `0.0551` n `20`; unknown avg `0.2321` n `961`
- 4h: commodity avg `-0.4171` n `12`; crypto_alt avg `1.9162` n `234`; crypto_major avg `1.0721` n `8`; equity avg `0.9` n `141`; fx avg `-0.0642` n `6`; index avg `0.1399` n `26`; metal avg `0.0847` n `20`; unknown avg `1.3213` n `927`
- 24h: commodity avg `-0.5701` n `12`; crypto_alt avg `1.5943` n `234`; crypto_major avg `1.1257` n `8`; equity avg `-0.0062` n `141`; fx avg `-0.0882` n `6`; index avg `0.0001` n `26`; metal avg `-0.1525` n `20`; unknown avg `45.6626` n `808`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.1828`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1712`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1527`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1523`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1447`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.134`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.123`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1144`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.108`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1046`, n `668`, weak_sample_signal
