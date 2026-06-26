# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-26T04:37:32.312075+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0038` n `12`; crypto_alt avg `-0.308` n `228`; crypto_major avg `-0.2334` n `8`; equity avg `-0.2114` n `86`; fx avg `0.0083` n `6`; index avg `-0.0568` n `23`; metal avg `-0.0853` n `20`; unknown avg `175.9865` n `765`
- 1h: commodity avg `-0.0261` n `12`; crypto_alt avg `0.7007` n `228`; crypto_major avg `0.909` n `8`; equity avg `0.4635` n `86`; fx avg `-0.0124` n `6`; index avg `0.0381` n `23`; metal avg `0.0618` n `20`; unknown avg `1.2504` n `749`
- 4h: commodity avg `-0.2158` n `12`; crypto_alt avg `-0.7193` n `228`; crypto_major avg `-0.5615` n `8`; equity avg `-1.6205` n `86`; fx avg `-0.0172` n `6`; index avg `-0.3802` n `23`; metal avg `-0.4102` n `20`; unknown avg `-0.6757` n `749`
- 24h: commodity avg `0.252` n `12`; crypto_alt avg `-1.6006` n `228`; crypto_major avg `-1.4334` n `8`; equity avg `-4.0237` n `86`; fx avg `0.0217` n `6`; index avg `-0.6687` n `23`; metal avg `-0.132` n `20`; unknown avg `0.4868` n `701`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1655`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1357`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1244`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1177`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1004`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0769`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0731`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0728`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0717`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.07`, n `668`, weak_sample_signal
