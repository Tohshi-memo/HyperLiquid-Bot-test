# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-08T12:37:35.759144+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0007` n `12`; crypto_alt avg `0.0414` n `230`; crypto_major avg `0.0277` n `8`; equity avg `-0.0124` n `112`; fx avg `0.0014` n `6`; index avg `-0.0006` n `25`; metal avg `-0.0146` n `20`; unknown avg `-0.0769` n `784`
- 1h: commodity avg `0.014` n `12`; crypto_alt avg `0.1687` n `230`; crypto_major avg `0.0648` n `8`; equity avg `-0.0154` n `112`; fx avg `0.0041` n `6`; index avg `-0.0141` n `25`; metal avg `-0.0254` n `20`; unknown avg `-0.0726` n `784`
- 4h: commodity avg `0.0684` n `12`; crypto_alt avg `0.267` n `230`; crypto_major avg `0.2832` n `8`; equity avg `0.1588` n `112`; fx avg `-0.0146` n `6`; index avg `0.0223` n `25`; metal avg `-0.0159` n `20`; unknown avg `0.3601` n `784`
- 24h: commodity avg `0.1298` n `12`; crypto_alt avg `0.2962` n `230`; crypto_major avg `0.0092` n `8`; equity avg `0.1944` n `112`; fx avg `0.0644` n `6`; index avg `-0.0814` n `25`; metal avg `-0.133` n `20`; unknown avg `0.3956` n `750`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1171`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0849`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0753`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0688`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0658`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0629`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0567`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.054`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.053`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0505`, n `668`, weak_sample_signal
