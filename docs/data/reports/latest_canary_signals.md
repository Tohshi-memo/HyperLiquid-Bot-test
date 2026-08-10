# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-10T21:07:29.110825+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0015` n `12`; crypto_alt avg `-0.0109` n `230`; crypto_major avg `-0.0208` n `8`; equity avg `-0.0244` n `113`; fx avg `-0.0019` n `6`; index avg `0.0019` n `25`; metal avg `0.032` n `20`; unknown avg `0.0962` n `785`
- 1h: commodity avg `0.0376` n `12`; crypto_alt avg `0.007` n `230`; crypto_major avg `-0.0719` n `8`; equity avg `0.0692` n `113`; fx avg `-0.013` n `6`; index avg `-0.0009` n `25`; metal avg `0.0408` n `20`; unknown avg `3.0514` n `785`
- 4h: commodity avg `0.0963` n `12`; crypto_alt avg `0.0578` n `230`; crypto_major avg `0.5357` n `8`; equity avg `-0.4164` n `113`; fx avg `0.0165` n `6`; index avg `-0.0214` n `25`; metal avg `0.2524` n `20`; unknown avg `0.9963` n `785`
- 24h: commodity avg `1.195` n `12`; crypto_alt avg `-1.0071` n `230`; crypto_major avg `-0.897` n `8`; equity avg `-1.7396` n `113`; fx avg `0.2466` n `6`; index avg `-0.0925` n `25`; metal avg `0.2004` n `20`; unknown avg `103.6792` n `752`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.176`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1704`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1555`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1554`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1527`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1459`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1259`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1225`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1186`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1042`, n `668`, weak_sample_signal
