# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-10T04:49:35.551300+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0458` n `12`; crypto_alt avg `-0.0186` n `230`; crypto_major avg `-0.034` n `8`; equity avg `-0.0499` n `112`; fx avg `0.0062` n `6`; index avg `-0.014` n `25`; metal avg `-0.0345` n `20`; unknown avg `-0.0091` n `785`
- 1h: commodity avg `-0.0878` n `12`; crypto_alt avg `-0.0233` n `230`; crypto_major avg `-0.0679` n `8`; equity avg `-0.1196` n `112`; fx avg `0.0163` n `6`; index avg `-0.0272` n `25`; metal avg `0.0281` n `20`; unknown avg `1.0026` n `785`
- 4h: commodity avg `-0.0771` n `12`; crypto_alt avg `-0.0111` n `230`; crypto_major avg `-0.0165` n `8`; equity avg `-0.2541` n `112`; fx avg `0.052` n `6`; index avg `-0.0051` n `25`; metal avg `0.0207` n `20`; unknown avg `0.5589` n `785`
- 24h: commodity avg `0.2742` n `12`; crypto_alt avg `0.4892` n `230`; crypto_major avg `-0.1181` n `8`; equity avg `-0.2921` n `112`; fx avg `0.1057` n `6`; index avg `-0.011` n `25`; metal avg `-0.1271` n `20`; unknown avg `-0.3229` n `752`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1929`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1457`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1404`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.135`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1305`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1236`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1167`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.104`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1001`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0967`, n `668`, weak_sample_signal
