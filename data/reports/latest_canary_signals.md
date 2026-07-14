# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-14T14:37:31.929607+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.4694` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_equity_divergence: score `2.1814` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_crypto_metal_divergence: score `1.6491` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.0088` n `12`; crypto_alt avg `0.0901` n `230`; crypto_major avg `0.0284` n `8`; equity avg `0.1272` n `92`; fx avg `0.0006` n `6`; index avg `0.0434` n `25`; metal avg `-0.0343` n `20`; unknown avg `-0.0673` n `766`
- 1h: commodity avg `-0.0848` n `12`; crypto_alt avg `-0.1698` n `230`; crypto_major avg `-0.1453` n `8`; equity avg `-0.139` n `92`; fx avg `0.0082` n `6`; index avg `-0.0154` n `25`; metal avg `0.0587` n `20`; unknown avg `19.1556` n `766`
- 4h: commodity avg `-0.2374` n `12`; crypto_alt avg `1.6478` n `230`; crypto_major avg `2.232` n `8`; equity avg `0.0506` n `92`; fx avg `-0.0067` n `6`; index avg `0.2082` n `25`; metal avg `0.5829` n `20`; unknown avg `1.0148` n `766`
- 24h: commodity avg `0.9667` n `12`; crypto_alt avg `0.7497` n `230`; crypto_major avg `2.1229` n `8`; equity avg `-0.2824` n `92`; fx avg `-0.0125` n `6`; index avg `0.0818` n `25`; metal avg `0.6713` n `20`; unknown avg `-0.1692` n `750`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1827`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1686`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1114`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1113`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1086`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0777`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0773`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0744`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0628`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0569`, n `668`, weak_sample_signal
