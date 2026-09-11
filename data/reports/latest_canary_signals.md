# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-11T02:52:30.121773+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0035` n `12`; crypto_alt avg `-0.0193` n `233`; crypto_major avg `0.0135` n `8`; equity avg `0.0024` n `136`; fx avg `-0.0244` n `6`; index avg `0.0073` n `26`; metal avg `0.0731` n `20`; unknown avg `-0.3543` n `796`
- 1h: commodity avg `-0.0208` n `12`; crypto_alt avg `-0.1981` n `233`; crypto_major avg `-0.1037` n `8`; equity avg `-0.2193` n `136`; fx avg `-0.0354` n `6`; index avg `-0.0032` n `26`; metal avg `-0.0115` n `20`; unknown avg `-0.5753` n `790`
- 4h: commodity avg `-0.2195` n `12`; crypto_alt avg `-0.358` n `233`; crypto_major avg `-0.2186` n `8`; equity avg `-0.1012` n `136`; fx avg `-0.046` n `6`; index avg `0.0164` n `26`; metal avg `0.0191` n `20`; unknown avg `-0.4943` n `778`
- 24h: commodity avg `1.0982` n `12`; crypto_alt avg `-2.28` n `233`; crypto_major avg `-2.4603` n `8`; equity avg `-1.9819` n `136`; fx avg `0.0983` n `6`; index avg `-0.3351` n `26`; metal avg `-1.339` n `20`; unknown avg `-0.9772` n `677`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.142`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1376`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1153`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1131`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.112`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0967`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0946`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.092`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0881`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0862`, n `668`, weak_sample_signal
