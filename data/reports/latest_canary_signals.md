# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-25T16:07:26.032109+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0116` n `12`; crypto_alt avg `0.0597` n `230`; crypto_major avg `0.045` n `8`; equity avg `-0.0367` n `100`; fx avg `-0.0024` n `6`; index avg `0.0095` n `25`; metal avg `-0.0074` n `20`; unknown avg `-0.0092` n `774`
- 1h: commodity avg `-0.0097` n `12`; crypto_alt avg `0.3079` n `230`; crypto_major avg `0.2261` n `8`; equity avg `-0.0311` n `100`; fx avg `-0.0063` n `6`; index avg `0.0045` n `25`; metal avg `-0.0163` n `20`; unknown avg `0.2393` n `774`
- 4h: commodity avg `-0.3553` n `12`; crypto_alt avg `0.6438` n `230`; crypto_major avg `0.6577` n `8`; equity avg `-0.0321` n `100`; fx avg `-0.0041` n `6`; index avg `0.0124` n `25`; metal avg `0.0143` n `20`; unknown avg `0.0085` n `774`
- 24h: commodity avg `-0.3177` n `12`; crypto_alt avg `0.112` n `230`; crypto_major avg `0.4481` n `8`; equity avg `-1.5397` n `100`; fx avg `-0.0384` n `6`; index avg `-0.2119` n `25`; metal avg `-0.2398` n `20`; unknown avg `-0.3115` n `757`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1644`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1619`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1334`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1287`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1251`, n `666`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1228`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1156`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.115`, n `666`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1091`, n `666`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1085`, n `668`, weak_sample_signal
