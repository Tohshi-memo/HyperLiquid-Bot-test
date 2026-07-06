# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-06T17:52:28.423755+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `2.0472` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_crypto_metal_divergence: score `1.7508` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0197` n `12`; crypto_alt avg `0.0006` n `229`; crypto_major avg `-0.0315` n `8`; equity avg `-0.1725` n `91`; fx avg `-0.0067` n `6`; index avg `-0.0041` n `25`; metal avg `0.0184` n `20`; unknown avg `-0.0123` n `763`
- 1h: commodity avg `0.073` n `12`; crypto_alt avg `-0.1845` n `229`; crypto_major avg `-0.2429` n `8`; equity avg `-0.5427` n `91`; fx avg `-0.0072` n `6`; index avg `-0.0819` n `25`; metal avg `0.092` n `20`; unknown avg `0.0804` n `763`
- 4h: commodity avg `-0.0046` n `12`; crypto_alt avg `1.9472` n `229`; crypto_major avg `1.8255` n `8`; equity avg `-0.2217` n `90`; fx avg `0.029` n `6`; index avg `-0.0326` n `25`; metal avg `0.0747` n `20`; unknown avg `1.7518` n `763`
- 24h: commodity avg `-0.0607` n `12`; crypto_alt avg `1.1116` n `229`; crypto_major avg `0.792` n `8`; equity avg `-0.6096` n `90`; fx avg `0.1967` n `6`; index avg `0.0028` n `25`; metal avg `-0.206` n `20`; unknown avg `0.8416` n `729`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1144`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0986`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.088`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0842`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.075`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0727`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0727`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0721`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0624`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0609`, n `668`, weak_sample_signal
