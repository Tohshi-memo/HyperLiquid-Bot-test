# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-10T10:22:30.940554+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.066` n `12`; crypto_alt avg `0.0217` n `230`; crypto_major avg `0.0621` n `8`; equity avg `-0.0075` n `112`; fx avg `-0.0073` n `6`; index avg `0.0008` n `25`; metal avg `0.0243` n `20`; unknown avg `0.0067` n `785`
- 1h: commodity avg `-0.0626` n `12`; crypto_alt avg `-0.0731` n `230`; crypto_major avg `-0.1361` n `8`; equity avg `-0.0961` n `112`; fx avg `-0.0096` n `6`; index avg `-0.0069` n `25`; metal avg `-0.0309` n `20`; unknown avg `-0.047` n `785`
- 4h: commodity avg `0.1326` n `12`; crypto_alt avg `-0.0375` n `230`; crypto_major avg `-0.0417` n `8`; equity avg `-0.0017` n `112`; fx avg `0.0513` n `6`; index avg `0.0128` n `25`; metal avg `-0.0796` n `20`; unknown avg `0.0513` n `785`
- 24h: commodity avg `0.33` n `12`; crypto_alt avg `0.8397` n `230`; crypto_major avg `-0.0903` n `8`; equity avg `-0.1161` n `112`; fx avg `0.2274` n `6`; index avg `0.0647` n `25`; metal avg `-0.1329` n `20`; unknown avg `56.906` n `753`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1843`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1442`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1398`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1349`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1316`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1246`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1185`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.117`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.113`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0976`, n `668`, weak_sample_signal
