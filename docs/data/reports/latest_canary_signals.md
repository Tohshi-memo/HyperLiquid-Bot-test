# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-11T09:52:28.801365+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0233` n `12`; crypto_alt avg `0.111` n `230`; crypto_major avg `0.1173` n `8`; equity avg `0.0901` n `113`; fx avg `-0.0043` n `6`; index avg `-0.0006` n `25`; metal avg `0.0095` n `20`; unknown avg `-0.0046` n `785`
- 1h: commodity avg `-0.0255` n `12`; crypto_alt avg `0.1473` n `230`; crypto_major avg `0.22` n `8`; equity avg `0.1415` n `113`; fx avg `-0.008` n `6`; index avg `0.0251` n `25`; metal avg `0.0286` n `20`; unknown avg `0.0035` n `785`
- 4h: commodity avg `0.2829` n `12`; crypto_alt avg `-0.153` n `230`; crypto_major avg `0.2329` n `8`; equity avg `-0.1796` n `113`; fx avg `0.0179` n `6`; index avg `-0.009` n `25`; metal avg `0.176` n `20`; unknown avg `0.031` n `753`
- 24h: commodity avg `1.0503` n `12`; crypto_alt avg `-0.974` n `230`; crypto_major avg `-0.4292` n `8`; equity avg `-1.3503` n `113`; fx avg `0.0114` n `6`; index avg `-0.0187` n `25`; metal avg `0.3507` n `20`; unknown avg `0.2085` n `752`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1822`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1769`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.173`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.169`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1411`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1404`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1185`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1166`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.11`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1076`, n `668`, weak_sample_signal
