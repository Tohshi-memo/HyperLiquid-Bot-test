# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-10T10:07:26.536406+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0537` n `12`; crypto_alt avg `0.0191` n `230`; crypto_major avg `0.0344` n `8`; equity avg `-0.0117` n `112`; fx avg `0.0018` n `6`; index avg `0.0022` n `25`; metal avg `-0.017` n `20`; unknown avg `0.0021` n `785`
- 1h: commodity avg `-0.0463` n `12`; crypto_alt avg `-0.1153` n `230`; crypto_major avg `-0.2281` n `8`; equity avg `-0.1214` n `112`; fx avg `-0.0074` n `6`; index avg `-0.0165` n `25`; metal avg `-0.0576` n `20`; unknown avg `-0.014` n `785`
- 4h: commodity avg `0.1882` n `12`; crypto_alt avg `-0.1258` n `230`; crypto_major avg `-0.1688` n `8`; equity avg `0.0988` n `112`; fx avg `0.0714` n `6`; index avg `0.0295` n `25`; metal avg `-0.1213` n `20`; unknown avg `54.7415` n `785`
- 24h: commodity avg `0.3693` n `12`; crypto_alt avg `0.818` n `230`; crypto_major avg `-0.0183` n `8`; equity avg `-0.0691` n `112`; fx avg `0.2348` n `6`; index avg `0.0745` n `25`; metal avg `-0.142` n `20`; unknown avg `56.9061` n `753`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1843`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1434`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1386`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.132`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1317`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1233`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1177`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1166`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1103`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0978`, n `668`, weak_sample_signal
