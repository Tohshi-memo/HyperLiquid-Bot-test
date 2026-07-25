# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-25T11:52:29.099464+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0169` n `12`; crypto_alt avg `0.0316` n `230`; crypto_major avg `0.0534` n `8`; equity avg `0.0589` n `100`; fx avg `-0.0045` n `6`; index avg `-0.0038` n `25`; metal avg `-0.0068` n `20`; unknown avg `0.0004` n `774`
- 1h: commodity avg `-0.0339` n `12`; crypto_alt avg `-0.085` n `230`; crypto_major avg `-0.0032` n `8`; equity avg `-0.0239` n `100`; fx avg `-0.011` n `6`; index avg `-0.0117` n `25`; metal avg `-0.0012` n `20`; unknown avg `-0.0752` n `774`
- 4h: commodity avg `-0.0531` n `12`; crypto_alt avg `-0.0658` n `230`; crypto_major avg `0.1812` n `8`; equity avg `-0.0549` n `100`; fx avg `-0.0178` n `6`; index avg `0.0041` n `25`; metal avg `-0.0088` n `20`; unknown avg `0.5892` n `774`
- 24h: commodity avg `-0.1408` n `12`; crypto_alt avg `-1.2503` n `230`; crypto_major avg `-0.8618` n `8`; equity avg `-2.8068` n `100`; fx avg `-0.0121` n `6`; index avg `-0.2371` n `25`; metal avg `-0.0907` n `20`; unknown avg `13.1272` n `757`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1595`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1497`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.121`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1174`, n `666`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.116`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1114`, n `666`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1105`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1092`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1014`, n `666`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1003`, n `668`, weak_sample_signal
