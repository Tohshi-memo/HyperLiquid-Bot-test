# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-29T14:37:32.105685+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.9493` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `2.5717` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `1.9254` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.1291` n `13`; crypto_alt avg `0.9869` n `238`; crypto_major avg `0.8496` n `8`; equity avg `0.0221` n `156`; fx avg `0.0013` n `6`; index avg `0.0134` n `27`; metal avg `0.0768` n `20`; unknown avg `19.7736` n `1186`
- 1h: commodity avg `0.0688` n `13`; crypto_alt avg `1.1925` n `238`; crypto_major avg `1.1112` n `8`; equity avg `0.8229` n `156`; fx avg `0.0798` n `6`; index avg `0.1141` n `27`; metal avg `0.1237` n `20`; unknown avg `21.8107` n `1138`
- 4h: commodity avg `-0.4017` n `13`; crypto_alt avg `1.8479` n `238`; crypto_major avg `2.5476` n `8`; equity avg `0.6222` n `155`; fx avg `0.0242` n `6`; index avg `-0.0177` n `27`; metal avg `-0.0241` n `20`; unknown avg `28.0145` n `1132`
- 24h: commodity avg `-0.8185` n `13`; crypto_alt avg `1.1951` n `238`; crypto_major avg `2.582` n `8`; equity avg `-0.0428` n `155`; fx avg `0.0059` n `6`; index avg `-0.0498` n `27`; metal avg `-0.3719` n `20`; unknown avg `36.4089` n `946`

## Correlations

- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0987`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0969`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0963`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0921`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0867`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0802`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0687`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0664`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0604`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0581`, n `668`, weak_sample_signal
