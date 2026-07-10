# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-10T03:22:29.551617+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0178` n `12`; crypto_alt avg `-0.0299` n `229`; crypto_major avg `-0.0079` n `8`; equity avg `-0.0914` n `91`; fx avg `0.0149` n `6`; index avg `-0.0012` n `25`; metal avg `-0.0335` n `20`; unknown avg `3.2396` n `765`
- 1h: commodity avg `0.0057` n `12`; crypto_alt avg `0.0097` n `229`; crypto_major avg `0.0195` n `8`; equity avg `0.2577` n `91`; fx avg `0.0389` n `6`; index avg `0.1031` n `25`; metal avg `0.0814` n `20`; unknown avg `3.068` n `765`
- 4h: commodity avg `0.0915` n `12`; crypto_alt avg `0.9087` n `229`; crypto_major avg `1.1127` n `8`; equity avg `0.1329` n `91`; fx avg `0.0049` n `6`; index avg `0.0121` n `25`; metal avg `0.2118` n `20`; unknown avg `0.6312` n `763`
- 24h: commodity avg `-1.0254` n `12`; crypto_alt avg `1.9001` n `229`; crypto_major avg `1.8594` n `8`; equity avg `2.1722` n `91`; fx avg `0.022` n `6`; index avg `0.5572` n `25`; metal avg `1.0564` n `20`; unknown avg `0.0155` n `746`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.0994`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0955`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0861`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0824`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0788`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0787`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0782`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0713`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0578`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.055`, n `668`, weak_sample_signal
