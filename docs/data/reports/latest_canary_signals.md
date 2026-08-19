# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-19T16:07:30.473206+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `4.9069` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_equity_divergence: score `4.5658` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_crypto_metal_divergence: score `4.1534` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- polymarket_volume_spike: score `2.18` - Polymarket crypto volume is unusually high.
- 1h_commodity_crypto_divergence: score `2.0105` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 1h_crypto_metal_divergence: score `1.925` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 1h_crypto_equity_divergence: score `1.5207` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0645` n `12`; crypto_alt avg `0.2008` n `230`; crypto_major avg `0.4398` n `8`; equity avg `0.4053` n `121`; fx avg `0.0087` n `6`; index avg `0.0509` n `25`; metal avg `0.0557` n `20`; unknown avg `0.5169` n `792`
- 1h: commodity avg `0.0482` n `12`; crypto_alt avg `0.7551` n `230`; crypto_major avg `2.0587` n `8`; equity avg `0.538` n `121`; fx avg `0.0111` n `6`; index avg `0.0141` n `25`; metal avg `0.1337` n `20`; unknown avg `0.599` n `792`
- 4h: commodity avg `0.0945` n `12`; crypto_alt avg `2.5508` n `230`; crypto_major avg `5.0014` n `8`; equity avg `0.4356` n `120`; fx avg `0.0625` n `6`; index avg `0.066` n `25`; metal avg `0.848` n `20`; unknown avg `1.3328` n `792`
- 24h: commodity avg `0.4044` n `12`; crypto_alt avg `2.3916` n `230`; crypto_major avg `4.924` n `8`; equity avg `-0.2205` n `120`; fx avg `-0.1775` n `6`; index avg `0.0446` n `25`; metal avg `0.7835` n `20`; unknown avg `0.4201` n `757`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1487`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1426`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1196`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1148`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1146`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.1125`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0959`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0932`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0894`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0837`, n `668`, weak_sample_signal
