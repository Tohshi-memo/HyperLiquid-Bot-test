# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-10T06:22:29.969958+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0387` n `12`; crypto_alt avg `-0.0892` n `229`; crypto_major avg `-0.113` n `8`; equity avg `-0.2095` n `91`; fx avg `-0.0166` n `6`; index avg `-0.0495` n `25`; metal avg `0.0256` n `20`; unknown avg `-0.002` n `765`
- 1h: commodity avg `-0.102` n `12`; crypto_alt avg `-0.1291` n `229`; crypto_major avg `-0.0772` n `8`; equity avg `-0.4771` n `91`; fx avg `-0.1208` n `6`; index avg `-0.0992` n `25`; metal avg `0.0281` n `20`; unknown avg `0.0036` n `733`
- 4h: commodity avg `-0.0905` n `12`; crypto_alt avg `-0.0842` n `229`; crypto_major avg `0.1242` n `8`; equity avg `-0.4531` n `91`; fx avg `-0.0662` n `6`; index avg `-0.0594` n `25`; metal avg `0.0501` n `20`; unknown avg `0.0141` n `733`
- 24h: commodity avg `-0.8601` n `12`; crypto_alt avg `0.6991` n `229`; crypto_major avg `0.8652` n `8`; equity avg `0.6919` n `91`; fx avg `-0.1085` n `6`; index avg `0.2243` n `25`; metal avg `0.5024` n `20`; unknown avg `-0.0032` n `732`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1144`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0965`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0895`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0851`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0798`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0778`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0773`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0772`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0715`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0694`, n `668`, weak_sample_signal
