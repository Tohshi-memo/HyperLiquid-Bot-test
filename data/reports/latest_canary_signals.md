# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-10T02:07:28.279428+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0119` n `12`; crypto_alt avg `-0.2513` n `230`; crypto_major avg `-0.2668` n `8`; equity avg `-0.1353` n `112`; fx avg `0.0036` n `6`; index avg `-0.0234` n `25`; metal avg `0.0282` n `20`; unknown avg `0.4045` n `785`
- 1h: commodity avg `-0.017` n `12`; crypto_alt avg `0.1477` n `230`; crypto_major avg `0.2844` n `8`; equity avg `0.1141` n `112`; fx avg `0.043` n `6`; index avg `0.0542` n `25`; metal avg `0.0742` n `20`; unknown avg `0.3924` n `785`
- 4h: commodity avg `-0.0033` n `12`; crypto_alt avg `-0.8615` n `230`; crypto_major avg `-0.7995` n `8`; equity avg `-0.3114` n `112`; fx avg `0.1264` n `6`; index avg `0.0428` n `25`; metal avg `-0.1279` n `20`; unknown avg `0.6293` n `785`
- 24h: commodity avg `0.4503` n `12`; crypto_alt avg `0.8961` n `230`; crypto_major avg `0.0755` n `8`; equity avg `-0.1787` n `112`; fx avg `0.1225` n `6`; index avg `0.0318` n `25`; metal avg `-0.1723` n `20`; unknown avg `-0.2992` n `752`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1831`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1448`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1337`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1289`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1238`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.1204`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1161`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1024`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.102`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0959`, n `668`, weak_sample_signal
