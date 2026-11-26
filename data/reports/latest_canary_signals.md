# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-26T19:07:31.043368+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `1.6819` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0167` n `13`; crypto_alt avg `0.1076` n `239`; crypto_major avg `0.1118` n `8`; equity avg `0.0617` n `168`; fx avg `-0.0038` n `6`; index avg `0.0059` n `27`; metal avg `-0.0002` n `20`; unknown avg `4.7115` n `1251`
- 1h: commodity avg `0.0482` n `13`; crypto_alt avg `0.3005` n `239`; crypto_major avg `0.3886` n `8`; equity avg `0.2321` n `168`; fx avg `-0.0005` n `6`; index avg `0.0191` n `27`; metal avg `0.0001` n `20`; unknown avg `167.2435` n `1217`
- 4h: commodity avg `0.0239` n `13`; crypto_alt avg `1.5923` n `239`; crypto_major avg `1.5757` n `8`; equity avg `0.3572` n `168`; fx avg `-0.0135` n `6`; index avg `0.0184` n `27`; metal avg `-0.1062` n `20`; unknown avg `171.6041` n `1191`
- 24h: commodity avg `0.1538` n `13`; crypto_alt avg `2.0574` n `239`; crypto_major avg `1.201` n `8`; equity avg `1.0085` n `168`; fx avg `-0.0287` n `6`; index avg `0.0543` n `27`; metal avg `0.236` n `20`; unknown avg `8.0681` n `1023`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1161`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1116`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1095`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.109`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0981`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0961`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0958`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.094`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0854`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.08`, n `668`, weak_sample_signal
