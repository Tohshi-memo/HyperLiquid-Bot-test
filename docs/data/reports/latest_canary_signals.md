# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-29T13:07:29.536824+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.2264` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `1.9688` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `1.766` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.1519` n `13`; crypto_alt avg `0.2067` n `238`; crypto_major avg `0.2313` n `8`; equity avg `0.178` n `155`; fx avg `-0.0267` n `6`; index avg `0.0395` n `27`; metal avg `0.0405` n `20`; unknown avg `0.8297` n `1233`
- 1h: commodity avg `-0.4797` n `13`; crypto_alt avg `0.8058` n `238`; crypto_major avg `0.6624` n `8`; equity avg `0.4285` n `155`; fx avg `-0.0226` n `6`; index avg `0.0542` n `27`; metal avg `0.0602` n `20`; unknown avg `25.4101` n `1231`
- 4h: commodity avg `-0.3884` n `13`; crypto_alt avg `1.3361` n `238`; crypto_major avg `1.838` n `8`; equity avg `0.072` n `155`; fx avg `0.0244` n `6`; index avg `-0.0361` n `27`; metal avg `-0.1308` n `20`; unknown avg `6.7991` n `1128`
- 24h: commodity avg `-0.7292` n `13`; crypto_alt avg `-0.3954` n `238`; crypto_major avg `0.9048` n `8`; equity avg `-1.0503` n `155`; fx avg `0.0019` n `6`; index avg `-0.0723` n `27`; metal avg `-0.5813` n `20`; unknown avg `11.7878` n `980`

## Correlations

- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1031`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0976`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0966`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0951`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0828`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0706`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0633`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0631`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0629`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0608`, n `668`, weak_sample_signal
