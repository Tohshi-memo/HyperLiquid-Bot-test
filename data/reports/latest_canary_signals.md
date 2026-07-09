# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-09T01:37:28.180451+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0974` n `12`; crypto_alt avg `-0.2099` n `229`; crypto_major avg `-0.3565` n `8`; equity avg `-0.0242` n `91`; fx avg `0.033` n `6`; index avg `-0.0712` n `25`; metal avg `0.0118` n `20`; unknown avg `-0.0714` n `764`
- 1h: commodity avg `-0.0179` n `12`; crypto_alt avg `0.3069` n `229`; crypto_major avg `0.0878` n `8`; equity avg `0.241` n `91`; fx avg `0.0718` n `6`; index avg `-0.0284` n `25`; metal avg `-0.0739` n `20`; unknown avg `0.0207` n `764`
- 4h: commodity avg `-0.195` n `12`; crypto_alt avg `0.7765` n `229`; crypto_major avg `0.5073` n `8`; equity avg `0.7198` n `91`; fx avg `0.0167` n `6`; index avg `0.0471` n `25`; metal avg `0.0405` n `20`; unknown avg `0.1483` n `764`
- 24h: commodity avg `0.3811` n `12`; crypto_alt avg `0.027` n `229`; crypto_major avg `-0.6056` n `8`; equity avg `1.4642` n `91`; fx avg `0.0131` n `6`; index avg `-0.0758` n `25`; metal avg `-0.6684` n `20`; unknown avg `0.1767` n `739`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.1023`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.093`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0776`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0706`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0628`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0616`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0589`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0577`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0531`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0531`, n `668`, weak_sample_signal
