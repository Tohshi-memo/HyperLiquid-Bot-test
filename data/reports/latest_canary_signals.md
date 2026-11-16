# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-16T14:37:32.595419+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 1h_commodity_crypto_divergence: score `2.5732` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 1h_crypto_equity_divergence: score `2.3468` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 1h_crypto_metal_divergence: score `2.333` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `2.2166` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_crypto_metal_divergence: score `1.5138` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.0465` n `13`; crypto_alt avg `1.3104` n `239`; crypto_major avg `1.6505` n `8`; equity avg `-0.2359` n `162`; fx avg `0.0002` n `6`; index avg `-0.0073` n `27`; metal avg `0.1263` n `20`; unknown avg `0.489` n `1259`
- 1h: commodity avg `-0.1943` n `13`; crypto_alt avg `2.1827` n `239`; crypto_major avg `2.3789` n `8`; equity avg `0.0321` n `162`; fx avg `-0.0103` n `6`; index avg `0.0234` n `27`; metal avg `0.0459` n `20`; unknown avg `11.4828` n `1253`
- 4h: commodity avg `-0.3971` n `13`; crypto_alt avg `1.4902` n `239`; crypto_major avg `1.5374` n `8`; equity avg `-0.6792` n `162`; fx avg `0.0133` n `6`; index avg `-0.0578` n `27`; metal avg `0.0236` n `20`; unknown avg `11.3941` n `1245`
- 24h: commodity avg `-0.6735` n `13`; crypto_alt avg `0.7332` n `239`; crypto_major avg `1.1382` n `8`; equity avg `-1.4907` n `162`; fx avg `-0.0169` n `6`; index avg `-0.1085` n `27`; metal avg `0.0768` n `20`; unknown avg `241.1296` n `1048`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1369`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1145`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1088`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1082`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1053`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1028`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0883`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.086`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0833`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0752`, n `668`, weak_sample_signal
