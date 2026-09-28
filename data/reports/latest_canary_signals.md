# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-28T23:22:37.360800+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0182` n `12`; crypto_alt avg `0.2817` n `234`; crypto_major avg `0.0223` n `8`; equity avg `0.021` n `141`; fx avg `-0.0285` n `6`; index avg `0.0095` n `26`; metal avg `0.0137` n `20`; unknown avg `0.0123` n `963`
- 1h: commodity avg `-0.0165` n `12`; crypto_alt avg `1.151` n `234`; crypto_major avg `0.5841` n `8`; equity avg `0.0573` n `141`; fx avg `-0.0268` n `6`; index avg `0.0005` n `26`; metal avg `-0.011` n `20`; unknown avg `0.688` n `961`
- 4h: commodity avg `-0.0447` n `12`; crypto_alt avg `0.4264` n `234`; crypto_major avg `-0.1724` n `8`; equity avg `-0.1144` n `141`; fx avg `-0.0172` n `6`; index avg `0.0052` n `26`; metal avg `-0.0888` n `20`; unknown avg `0.3139` n `873`
- 24h: commodity avg `0.0142` n `12`; crypto_alt avg `-3.1464` n `234`; crypto_major avg `-1.8086` n `8`; equity avg `-2.8924` n `141`; fx avg `0.0368` n `6`; index avg `-0.2159` n `26`; metal avg `-0.9454` n `20`; unknown avg `75.2874` n `804`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.1743`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1611`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1311`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1127`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1082`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1053`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0984`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0984`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0968`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.093`, n `668`, weak_sample_signal
