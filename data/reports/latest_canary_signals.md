# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-19T15:53:33.985346+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `4.4734` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_equity_divergence: score `4.3286` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_crypto_metal_divergence: score `3.6931` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 1h_commodity_crypto_divergence: score `3.144` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 1h_crypto_metal_divergence: score `3.0847` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 1h_crypto_equity_divergence: score `2.7307` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0575` n `12`; crypto_alt avg `-0.704` n `230`; crypto_major avg `-0.0954` n `8`; equity avg `0.0273` n `121`; fx avg `-0.0139` n `6`; index avg `-0.0161` n `25`; metal avg `0.069` n `20`; unknown avg `-0.0696` n `792`
- 1h: commodity avg `0.029` n `12`; crypto_alt avg `1.605` n `230`; crypto_major avg `3.173` n `8`; equity avg `0.4423` n `121`; fx avg `0.0261` n `6`; index avg `0.013` n `25`; metal avg `0.0883` n `20`; unknown avg `0.0501` n `792`
- 4h: commodity avg `0.048` n `12`; crypto_alt avg `2.332` n `230`; crypto_major avg `4.5214` n `8`; equity avg `0.1928` n `120`; fx avg `0.0399` n `6`; index avg `0.0536` n `25`; metal avg `0.8283` n `20`; unknown avg `1.2422` n `792`
- 24h: commodity avg `0.2941` n `12`; crypto_alt avg `2.2846` n `230`; crypto_major avg `4.4455` n `8`; equity avg `-0.5167` n `120`; fx avg `-0.1925` n `6`; index avg `0.0047` n `25`; metal avg `0.7439` n `20`; unknown avg `0.3673` n `757`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1476`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.146`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1204`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.1153`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1135`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0987`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.096`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.093`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0899`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0844`, n `668`, weak_sample_signal
