# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-24T07:37:19.118867+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1328` n `12`; crypto_alt avg `0.0421` n `228`; crypto_major avg `-0.0186` n `8`; equity avg `-0.0572` n `67`; fx avg `-0.005` n `6`; index avg `-0.0027` n `23`; metal avg `0.0212` n `18`; unknown avg `0.0984` n `396`
- 1h: commodity avg `0.253` n `12`; crypto_alt avg `0.2085` n `228`; crypto_major avg `0.2075` n `8`; equity avg `0.088` n `67`; fx avg `0.0006` n `6`; index avg `0.0573` n `23`; metal avg `-0.0039` n `18`; unknown avg `-0.2816` n `396`
- 4h: commodity avg `0.1485` n `12`; crypto_alt avg `-0.0292` n `228`; crypto_major avg `0.2807` n `8`; equity avg `0.0724` n `67`; fx avg `0.0071` n `6`; index avg `0.0135` n `23`; metal avg `-0.0273` n `18`; unknown avg `-0.1743` n `386`
- 24h: commodity avg `-2.7616` n `12`; crypto_alt avg `2.4776` n `228`; crypto_major avg `3.1451` n `8`; equity avg `2.3812` n `67`; fx avg `0.0266` n `6`; index avg `1.3433` n `23`; metal avg `1.1178` n `18`; unknown avg `1.7714` n `386`

## Correlations

- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1293`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1207`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1148`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1108`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1085`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1049`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1039`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1022`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0962`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0934`, n `668`, weak_sample_signal
