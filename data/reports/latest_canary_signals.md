# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-12T07:47:29.598710+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.07` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0063` n `12`; crypto_alt avg `-0.0618` n `230`; crypto_major avg `-0.0784` n `8`; equity avg `0.0091` n `113`; fx avg `-0.0054` n `6`; index avg `-0.0011` n `25`; metal avg `0.0134` n `20`; unknown avg `-0.0121` n `786`
- 1h: commodity avg `0.1133` n `12`; crypto_alt avg `-0.253` n `230`; crypto_major avg `0.0388` n `8`; equity avg `0.1779` n `113`; fx avg `0.0093` n `6`; index avg `-0.0031` n `25`; metal avg `-0.0165` n `20`; unknown avg `0.0059` n `786`
- 4h: commodity avg `-0.0609` n `12`; crypto_alt avg `-0.6465` n `230`; crypto_major avg `-0.1735` n `8`; equity avg `0.1053` n `113`; fx avg `0.0138` n `6`; index avg `0.0012` n `25`; metal avg `0.0805` n `20`; unknown avg `-0.0532` n `770`
- 24h: commodity avg `-0.0853` n `12`; crypto_alt avg `-1.0771` n `230`; crypto_major avg `0.6658` n `8`; equity avg `2.0863` n `113`; fx avg `0.0234` n `6`; index avg `0.1892` n `25`; metal avg `0.3186` n `20`; unknown avg `-0.1259` n `769`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.2333`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2261`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.2128`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.2046`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1761`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1473`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.139`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1176`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1106`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1103`, n `668`, weak_sample_signal
