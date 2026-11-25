# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-25T19:37:32.142553+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `3.5771` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `2.5846` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.0387` n `13`; crypto_alt avg `-0.1162` n `239`; crypto_major avg `-0.2216` n `8`; equity avg `0.0975` n `168`; fx avg `0.0032` n `6`; index avg `0.0089` n `27`; metal avg `0.0206` n `20`; unknown avg `157.7721` n `1267`
- 1h: commodity avg `-0.0693` n `13`; crypto_alt avg `1.1519` n `239`; crypto_major avg `1.2358` n `8`; equity avg `1.241` n `168`; fx avg `0.0067` n `6`; index avg `0.0976` n `27`; metal avg `0.2267` n `20`; unknown avg `277.2108` n `1265`
- 4h: commodity avg `0.0051` n `13`; crypto_alt avg `3.8411` n `239`; crypto_major avg `3.5822` n `8`; equity avg `4.7617` n `168`; fx avg `0.0732` n `6`; index avg `0.4587` n `27`; metal avg `0.9976` n `20`; unknown avg `13.6965` n `1256`
- 24h: commodity avg `0.2874` n `13`; crypto_alt avg `2.2872` n `239`; crypto_major avg `1.505` n `8`; equity avg `-0.393` n `168`; fx avg `0.0371` n `6`; index avg `-0.0702` n `27`; metal avg `-0.0237` n `20`; unknown avg `1.0474` n `1085`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1633`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1279`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1225`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1196`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.105`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1033`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1018`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0991`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.095`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0856`, n `668`, weak_sample_signal
