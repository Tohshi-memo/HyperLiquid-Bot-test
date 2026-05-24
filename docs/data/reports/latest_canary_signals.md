# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-24T06:37:14.185796+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0004` n `12`; crypto_alt avg `-0.0204` n `228`; crypto_major avg `0.0869` n `8`; equity avg `0.0792` n `67`; fx avg `-0.012` n `6`; index avg `0.0475` n `23`; metal avg `-0.0409` n `18`; unknown avg `0.2446` n `396`
- 1h: commodity avg `-0.0571` n `12`; crypto_alt avg `0.1632` n `228`; crypto_major avg `0.227` n `8`; equity avg `-0.0274` n `67`; fx avg `0.0066` n `6`; index avg `-0.04` n `23`; metal avg `-0.005` n `18`; unknown avg `1.128` n `386`
- 4h: commodity avg `-0.3049` n `12`; crypto_alt avg `-0.2393` n `228`; crypto_major avg `0.2715` n `8`; equity avg `0.0359` n `67`; fx avg `0.0041` n `6`; index avg `-0.027` n `23`; metal avg `0.0812` n `18`; unknown avg `0.9531` n `386`
- 24h: commodity avg `-3.0645` n `12`; crypto_alt avg `1.8926` n `228`; crypto_major avg `2.8059` n `8`; equity avg `2.2232` n `67`; fx avg `0.0343` n `6`; index avg `1.2617` n `23`; metal avg `1.1935` n `18`; unknown avg `2.9137` n `386`

## Correlations

- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1267`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.115`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1063`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1004`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0933`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0908`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.087`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0777`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0773`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0763`, n `668`, weak_sample_signal
