# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-08T15:22:28.464176+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0029` n `12`; crypto_alt avg `0.0333` n `230`; crypto_major avg `-0.0459` n `8`; equity avg `0.1106` n `112`; fx avg `-0.0001` n `6`; index avg `0.014` n `25`; metal avg `0.0042` n `20`; unknown avg `0.0154` n `784`
- 1h: commodity avg `-0.0861` n `12`; crypto_alt avg `0.2535` n `230`; crypto_major avg `0.3057` n `8`; equity avg `0.0972` n `112`; fx avg `-0.001` n `6`; index avg `0.0111` n `25`; metal avg `-0.0055` n `20`; unknown avg `0.1047` n `784`
- 4h: commodity avg `-0.0227` n `12`; crypto_alt avg `0.6401` n `230`; crypto_major avg `0.6416` n `8`; equity avg `0.2398` n `112`; fx avg `-0.0025` n `6`; index avg `0.0371` n `25`; metal avg `-0.0233` n `20`; unknown avg `-0.2229` n `784`
- 24h: commodity avg `-0.2604` n `12`; crypto_alt avg `1.0046` n `230`; crypto_major avg `0.9899` n `8`; equity avg `0.8929` n `112`; fx avg `-0.0219` n `6`; index avg `0.0531` n `25`; metal avg `0.016` n `20`; unknown avg `-0.0489` n `750`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1167`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0813`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0705`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0687`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0659`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0612`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0606`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0536`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0518`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0494`, n `668`, weak_sample_signal
