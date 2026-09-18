# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-18T14:07:34.884094+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `2.4572` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 1h_crypto_equity_divergence: score `2.2305` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 1h_crypto_metal_divergence: score `2.0826` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_metal_divergence: score `1.9249` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.0063` n `12`; crypto_alt avg `-0.3968` n `234`; crypto_major avg `-0.3717` n `8`; equity avg `-0.5183` n `140`; fx avg `0.0009` n `6`; index avg `-0.0714` n `26`; metal avg `-0.0663` n `20`; unknown avg `1.6057` n `904`
- 1h: commodity avg `0.1622` n `12`; crypto_alt avg `0.6531` n `234`; crypto_major avg `1.9161` n `8`; equity avg `-0.3144` n `140`; fx avg `0.0164` n `6`; index avg `-0.0764` n `26`; metal avg `-0.1665` n `20`; unknown avg `2.791` n `904`
- 4h: commodity avg `0.3662` n `12`; crypto_alt avg `0.3208` n `234`; crypto_major avg `1.6573` n `8`; equity avg `-0.7999` n `140`; fx avg `-0.0383` n `6`; index avg `-0.1356` n `26`; metal avg `-0.2676` n `20`; unknown avg `1.6338` n `895`
- 24h: commodity avg `0.2614` n `12`; crypto_alt avg `6.036` n `234`; crypto_major avg `5.7828` n `8`; equity avg `0.6073` n `140`; fx avg `0.226` n `6`; index avg `-0.0599` n `26`; metal avg `-0.0399` n `20`; unknown avg `5.1255` n `729`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1443`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1328`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.132`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.128`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1261`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1234`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1207`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1152`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1118`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1098`, n `668`, weak_sample_signal
