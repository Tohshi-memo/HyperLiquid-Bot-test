# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-11T07:07:28.051173+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0737` n `12`; crypto_alt avg `0.1579` n `233`; crypto_major avg `0.0874` n `8`; equity avg `0.0956` n `136`; fx avg `-0.0285` n `6`; index avg `0.0153` n `26`; metal avg `0.0019` n `20`; unknown avg `0.2926` n `794`
- 1h: commodity avg `-0.019` n `12`; crypto_alt avg `-0.0377` n `233`; crypto_major avg `0.0885` n `8`; equity avg `0.177` n `136`; fx avg `-0.0165` n `6`; index avg `0.0391` n `26`; metal avg `0.0024` n `20`; unknown avg `0.5893` n `794`
- 4h: commodity avg `-0.432` n `12`; crypto_alt avg `1.0601` n `233`; crypto_major avg `1.0008` n `8`; equity avg `0.9084` n `136`; fx avg `-0.0175` n `6`; index avg `0.2028` n `26`; metal avg `0.3479` n `20`; unknown avg `27.2305` n `764`
- 24h: commodity avg `0.7756` n `12`; crypto_alt avg `-1.3363` n `233`; crypto_major avg `-1.3324` n `8`; equity avg `-1.3205` n `136`; fx avg `0.0503` n `6`; index avg `-0.2204` n `26`; metal avg `-0.972` n `20`; unknown avg `0.747` n `685`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1198`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1161`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.098`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0916`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0913`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0812`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0781`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0701`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0629`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0593`, n `668`, weak_sample_signal
