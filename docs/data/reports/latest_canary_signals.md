# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-11T15:22:33.226017+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `3.7561` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `3.7386` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- polymarket_volume_spike: score `3.59` - Polymarket crypto volume is unusually high.
- 4h_crypto_equity_divergence: score `3.203` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0188` n `12`; crypto_alt avg `0.1554` n `233`; crypto_major avg `0.2265` n `8`; equity avg `0.1224` n `136`; fx avg `-0.021` n `6`; index avg `0.039` n `26`; metal avg `0.0294` n `20`; unknown avg `-0.053` n `796`
- 1h: commodity avg `-0.0924` n `12`; crypto_alt avg `-0.0014` n `233`; crypto_major avg `-0.1863` n `8`; equity avg `-0.1752` n `136`; fx avg `0.0049` n `6`; index avg `0.0051` n `26`; metal avg `-0.1422` n `20`; unknown avg `1.1798` n `794`
- 4h: commodity avg `0.1307` n `12`; crypto_alt avg `4.0075` n `233`; crypto_major avg `3.8868` n `8`; equity avg `0.6838` n `136`; fx avg `-0.0319` n `6`; index avg `0.1531` n `26`; metal avg `0.1482` n `20`; unknown avg `5.699` n `772`
- 24h: commodity avg `-0.1144` n `12`; crypto_alt avg `2.3812` n `233`; crypto_major avg `3.1195` n `8`; equity avg `0.2513` n `136`; fx avg `-0.132` n `6`; index avg `0.2809` n `26`; metal avg `0.0292` n `20`; unknown avg `5.1389` n `697`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1251`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1189`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1177`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1159`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1125`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1047`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0936`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0929`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0782`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0777`, n `668`, weak_sample_signal
