# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-20T13:37:31.128339+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.242` n `12`; crypto_alt avg `-0.5491` n `228`; crypto_major avg `-0.408` n `8`; equity avg `-0.4535` n `66`; fx avg `0.0015` n `6`; index avg `-0.0118` n `23`; metal avg `-0.2181` n `18`; unknown avg `0.1237` n `384`
- 1h: commodity avg `0.3187` n `12`; crypto_alt avg `-0.5409` n `228`; crypto_major avg `-0.2593` n `8`; equity avg `-0.4549` n `66`; fx avg `0.004` n `6`; index avg `-0.067` n `23`; metal avg `-0.4635` n `18`; unknown avg `0.9663` n `384`
- 4h: commodity avg `-0.182` n `12`; crypto_alt avg `-0.5436` n `228`; crypto_major avg `-0.0417` n `8`; equity avg `-0.1767` n `66`; fx avg `0.0434` n `6`; index avg `0.0573` n `23`; metal avg `-0.322` n `18`; unknown avg `1.6223` n `384`
- 24h: commodity avg `-0.6914` n `12`; crypto_alt avg `0.1122` n `228`; crypto_major avg `0.1956` n `8`; equity avg `0.6348` n `66`; fx avg `-0.0648` n `6`; index avg `0.1393` n `23`; metal avg `0.2988` n `18`; unknown avg `0.2571` n `373`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0858`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0803`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0751`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0749`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0749`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0596`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0563`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0561`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0494`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0458`, n `668`, weak_sample_signal
