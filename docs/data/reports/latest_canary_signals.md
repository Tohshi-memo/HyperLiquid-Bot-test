# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-11T14:07:30.618204+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0272` n `12`; crypto_alt avg `0.0207` n `230`; crypto_major avg `0.0361` n `8`; equity avg `0.6683` n `113`; fx avg `0.0218` n `6`; index avg `0.0689` n `25`; metal avg `-0.0214` n `20`; unknown avg `-0.014` n `785`
- 1h: commodity avg `-0.0071` n `12`; crypto_alt avg `-0.0708` n `230`; crypto_major avg `-0.1069` n `8`; equity avg `0.3757` n `113`; fx avg `-0.0085` n `6`; index avg `0.0027` n `25`; metal avg `-0.0715` n `20`; unknown avg `-0.0351` n `785`
- 4h: commodity avg `-0.4079` n `12`; crypto_alt avg `-0.2198` n `230`; crypto_major avg `-0.0081` n `8`; equity avg `0.9572` n `113`; fx avg `-0.048` n `6`; index avg `0.1019` n `25`; metal avg `-0.0957` n `20`; unknown avg `-0.1267` n `785`
- 24h: commodity avg `0.1466` n `12`; crypto_alt avg `-1.3181` n `230`; crypto_major avg `-0.2105` n `8`; equity avg `0.0514` n `113`; fx avg `-0.0657` n `6`; index avg `0.1047` n `25`; metal avg `0.3603` n `20`; unknown avg `-0.1518` n `752`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1935`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1871`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1825`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1742`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1364`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1256`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1211`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1006`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0965`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0961`, n `668`, weak_sample_signal
