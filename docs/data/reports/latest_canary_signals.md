# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-14T07:37:35.831432+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0001` n `12`; crypto_alt avg `-0.0822` n `228`; crypto_major avg `-0.107` n `8`; equity avg `0.046` n `74`; fx avg `-0.0002` n `6`; index avg `0.0058` n `23`; metal avg `0.008` n `18`; unknown avg `0.0078` n `645`
- 1h: commodity avg `-0.0783` n `12`; crypto_alt avg `-0.0206` n `228`; crypto_major avg `0.0292` n `8`; equity avg `0.0781` n `74`; fx avg `0.0056` n `6`; index avg `-0.0011` n `23`; metal avg `-0.0014` n `18`; unknown avg `0.1597` n `643`
- 4h: commodity avg `-0.1572` n `12`; crypto_alt avg `-0.4888` n `228`; crypto_major avg `-0.4331` n `8`; equity avg `0.0533` n `74`; fx avg `-0.0021` n `6`; index avg `0.0174` n `23`; metal avg `0.0092` n `18`; unknown avg `2.4153` n `625`
- 24h: commodity avg `-0.7591` n `12`; crypto_alt avg `0.2789` n `228`; crypto_major avg `0.8089` n `8`; equity avg `0.6386` n `74`; fx avg `-0.0116` n `6`; index avg `0.2279` n `23`; metal avg `0.2532` n `18`; unknown avg `-0.4433` n `599`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1064`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1004`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.096`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.071`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.067`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0659`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.063`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0629`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0622`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0612`, n `668`, weak_sample_signal
