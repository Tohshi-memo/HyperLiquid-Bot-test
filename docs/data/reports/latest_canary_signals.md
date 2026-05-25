# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-25T22:52:19.598063+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0077` n `12`; crypto_alt avg `0.1626` n `228`; crypto_major avg `0.0772` n `8`; equity avg `0.0006` n `67`; fx avg `-0.0016` n `6`; index avg `-0.0062` n `23`; metal avg `0.0882` n `18`; unknown avg `-0.0358` n `405`
- 1h: commodity avg `-0.4717` n `12`; crypto_alt avg `-0.5963` n `228`; crypto_major avg `-0.194` n `8`; equity avg `-0.1278` n `67`; fx avg `0.0176` n `6`; index avg `-0.226` n `23`; metal avg `0.0184` n `18`; unknown avg `0.3686` n `405`
- 4h: commodity avg `-0.3937` n `12`; crypto_alt avg `-1.2042` n `228`; crypto_major avg `-0.6513` n `8`; equity avg `-0.1546` n `67`; fx avg `0.0341` n `6`; index avg `-0.0996` n `23`; metal avg `0.0135` n `18`; unknown avg `-0.1334` n `405`
- 24h: commodity avg `-0.3645` n `12`; crypto_alt avg `1.721` n `228`; crypto_major avg `0.1136` n `8`; equity avg `0.7976` n `67`; fx avg `-0.0626` n `6`; index avg `0.4815` n `23`; metal avg `0.6154` n `18`; unknown avg `1.1995` n `386`

## Correlations

- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.169`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1664`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1614`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1555`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1459`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1445`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1365`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1301`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1265`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1217`, n `668`, weak_sample_signal
