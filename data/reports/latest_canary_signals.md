# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-10T19:37:36.006065+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0161` n `12`; crypto_alt avg `-0.0334` n `230`; crypto_major avg `0.0786` n `8`; equity avg `-0.0043` n `113`; fx avg `0.0026` n `6`; index avg `-0.0042` n `25`; metal avg `-0.0047` n `20`; unknown avg `-0.0294` n `785`
- 1h: commodity avg `-0.0815` n `12`; crypto_alt avg `0.1086` n `230`; crypto_major avg `0.3935` n `8`; equity avg `0.1465` n `113`; fx avg `0.0105` n `6`; index avg `0.0246` n `25`; metal avg `0.0956` n `20`; unknown avg `0.1018` n `785`
- 4h: commodity avg `0.0847` n `12`; crypto_alt avg `-0.0171` n `230`; crypto_major avg `0.2859` n `8`; equity avg `-0.0417` n `113`; fx avg `0.0166` n `6`; index avg `0.0092` n `25`; metal avg `0.2758` n `20`; unknown avg `-0.1282` n `785`
- 24h: commodity avg `1.168` n `12`; crypto_alt avg `-0.8803` n `230`; crypto_major avg `-1.0278` n `8`; equity avg `-1.3262` n `113`; fx avg `0.2645` n `6`; index avg `-0.0727` n `25`; metal avg `0.1916` n `20`; unknown avg `103.5558` n `752`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1731`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1665`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1534`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1529`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1517`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1477`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1283`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.122`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1194`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1032`, n `668`, weak_sample_signal
