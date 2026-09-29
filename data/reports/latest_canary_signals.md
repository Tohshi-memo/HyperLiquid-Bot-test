# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-29T09:22:31.482662+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0154` n `12`; crypto_alt avg `0.0969` n `234`; crypto_major avg `0.1097` n `8`; equity avg `-0.0337` n `141`; fx avg `-0.017` n `6`; index avg `-0.0098` n `26`; metal avg `0.0159` n `20`; unknown avg `0.3749` n `963`
- 1h: commodity avg `-0.058` n `12`; crypto_alt avg `-0.4355` n `234`; crypto_major avg `-0.5579` n `8`; equity avg `-0.2408` n `141`; fx avg `-0.0423` n `6`; index avg `-0.0332` n `26`; metal avg `0.0027` n `20`; unknown avg `1.7228` n `961`
- 4h: commodity avg `-0.41` n `12`; crypto_alt avg `1.6876` n `234`; crypto_major avg `0.8749` n `8`; equity avg `0.8034` n `141`; fx avg `-0.0562` n `6`; index avg `0.1231` n `26`; metal avg `0.076` n `20`; unknown avg `0.9307` n `927`
- 24h: commodity avg `-0.5463` n `12`; crypto_alt avg `1.0158` n `234`; crypto_major avg `0.7476` n `8`; equity avg `-0.054` n `141`; fx avg `-0.1015` n `6`; index avg `-0.0292` n `26`; metal avg `-0.1509` n `20`; unknown avg `49.8647` n `808`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.1837`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.172`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.155`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1549`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1415`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1325`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1237`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1125`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1102`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1067`, n `668`, weak_sample_signal
