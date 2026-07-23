# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-23T18:07:35.464503+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0939` n `12`; crypto_alt avg `-0.3764` n `230`; crypto_major avg `-0.1728` n `8`; equity avg `-0.3341` n `100`; fx avg `0.0045` n `6`; index avg `-0.034` n `25`; metal avg `-0.0237` n `20`; unknown avg `-0.1386` n `772`
- 1h: commodity avg `0.1707` n `12`; crypto_alt avg `-0.4554` n `230`; crypto_major avg `-0.2616` n `8`; equity avg `-0.2835` n `100`; fx avg `0.0075` n `6`; index avg `-0.0134` n `25`; metal avg `-0.096` n `20`; unknown avg `-0.4124` n `772`
- 4h: commodity avg `0.319` n `12`; crypto_alt avg `-0.8487` n `230`; crypto_major avg `-0.8877` n `8`; equity avg `-1.0892` n `100`; fx avg `-0.0035` n `6`; index avg `-0.1471` n `25`; metal avg `-0.1064` n `20`; unknown avg `-0.5504` n `772`
- 24h: commodity avg `1.1866` n `12`; crypto_alt avg `-1.9272` n `230`; crypto_major avg `-2.4417` n `8`; equity avg `-1.4494` n `99`; fx avg `-0.0782` n `6`; index avg `-0.3678` n `25`; metal avg `-0.8584` n `20`; unknown avg `-0.5636` n `740`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1579`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1424`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1404`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1334`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1128`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0973`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0938`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0885`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0851`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0743`, n `668`, weak_sample_signal
