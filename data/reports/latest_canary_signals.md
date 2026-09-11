# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-11T10:22:30.265868+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0888` n `12`; crypto_alt avg `-0.2735` n `233`; crypto_major avg `-0.1269` n `8`; equity avg `-0.0502` n `136`; fx avg `-0.0064` n `6`; index avg `-0.0168` n `26`; metal avg `0.0291` n `20`; unknown avg `0.0172` n `796`
- 1h: commodity avg `-0.1841` n `12`; crypto_alt avg `-0.4685` n `233`; crypto_major avg `-0.2683` n `8`; equity avg `0.0036` n `136`; fx avg `-0.0087` n `6`; index avg `0.0164` n `26`; metal avg `0.0677` n `20`; unknown avg `-0.2178` n `794`
- 4h: commodity avg `-0.4623` n `12`; crypto_alt avg `-0.7519` n `233`; crypto_major avg `-0.3273` n `8`; equity avg `0.3005` n `136`; fx avg `-0.0654` n `6`; index avg `0.0864` n `26`; metal avg `0.0139` n `20`; unknown avg `0.0796` n `786`
- 24h: commodity avg `0.2204` n `12`; crypto_alt avg `-1.4784` n `233`; crypto_major avg `-1.502` n `8`; equity avg `-0.8586` n `136`; fx avg `-0.0562` n `6`; index avg `-0.1195` n `26`; metal avg `-0.6836` n `20`; unknown avg `1.2414` n `683`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1134`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1121`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0896`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.085`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0842`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0796`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0702`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0577`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0567`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0552`, n `668`, weak_sample_signal
