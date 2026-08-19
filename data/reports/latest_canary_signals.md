# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-19T17:53:18.741919+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `4.1104` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `3.8552` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `3.3424` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.034` n `12`; crypto_alt avg `0.136` n `230`; crypto_major avg `0.3751` n `8`; equity avg `0.1502` n `121`; fx avg `0.0115` n `6`; index avg `0.0102` n `25`; metal avg `0.0025` n `20`; unknown avg `0.3134` n `792`
- 1h: commodity avg `-0.1042` n `12`; crypto_alt avg `-0.2594` n `230`; crypto_major avg `-0.2018` n `8`; equity avg `-0.3893` n `121`; fx avg `0.0098` n `6`; index avg `-0.0419` n `25`; metal avg `-0.0671` n `20`; unknown avg `0.9535` n `792`
- 4h: commodity avg `0.0036` n `12`; crypto_alt avg `2.4416` n `230`; crypto_major avg `4.114` n `8`; equity avg `0.7716` n `121`; fx avg `0.0068` n `6`; index avg `0.0039` n `25`; metal avg `0.2588` n `20`; unknown avg `0.328` n `792`
- 24h: commodity avg `0.3113` n `12`; crypto_alt avg `2.7239` n `230`; crypto_major avg `4.8447` n `8`; equity avg `-0.3779` n `120`; fx avg `-0.1838` n `6`; index avg `-0.0126` n `25`; metal avg `0.8064` n `20`; unknown avg `0.4575` n `757`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `-0.183`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1572`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1528`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1419`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.1238`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1232`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1095`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0906`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0863`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0851`, n `668`, weak_sample_signal
