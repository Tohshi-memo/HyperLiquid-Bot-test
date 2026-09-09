# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-09T08:07:29.342868+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0158` n `12`; crypto_alt avg `0.1888` n `233`; crypto_major avg `0.1654` n `8`; equity avg `0.1421` n `134`; fx avg `0.0185` n `6`; index avg `0.0199` n `26`; metal avg `-0.0257` n `20`; unknown avg `0.0951` n `796`
- 1h: commodity avg `0.0686` n `12`; crypto_alt avg `0.1155` n `233`; crypto_major avg `0.0483` n `8`; equity avg `0.0596` n `134`; fx avg `0.0216` n `6`; index avg `-0.0` n `26`; metal avg `0.05` n `20`; unknown avg `0.4583` n `796`
- 4h: commodity avg `0.0966` n `12`; crypto_alt avg `1.1968` n `233`; crypto_major avg `0.8315` n `8`; equity avg `0.2778` n `134`; fx avg `-0.0143` n `6`; index avg `0.0213` n `26`; metal avg `0.2894` n `20`; unknown avg `1.0851` n `772`
- 24h: commodity avg `-0.1821` n `12`; crypto_alt avg `1.0337` n `232`; crypto_major avg `1.7921` n `8`; equity avg `1.6489` n `134`; fx avg `-0.0947` n `6`; index avg `0.1093` n `26`; metal avg `0.1181` n `20`; unknown avg `0.5144` n `689`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `0.1476`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1171`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1115`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.105`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0894`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0824`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0771`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.077`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0744`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0715`, n `668`, weak_sample_signal
