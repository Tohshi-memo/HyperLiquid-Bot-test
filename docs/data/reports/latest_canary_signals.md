# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-22T06:22:24.921287+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 1h_commodity_crypto_divergence: score `2.0523` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 1h_crypto_metal_divergence: score `2.0418` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 1h_crypto_equity_divergence: score `1.8305` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0007` n `12`; crypto_alt avg `0.3229` n `230`; crypto_major avg `0.324` n `8`; equity avg `0.0241` n `121`; fx avg `-0.005` n `6`; index avg `-0.0009` n `25`; metal avg `0.0031` n `20`; unknown avg `0.0636` n `794`
- 1h: commodity avg `0.0338` n `12`; crypto_alt avg `1.3928` n `230`; crypto_major avg `2.0861` n `8`; equity avg `0.2556` n `121`; fx avg `0.0045` n `6`; index avg `0.002` n `25`; metal avg `0.0443` n `20`; unknown avg `0.2288` n `778`
- 4h: commodity avg `0.0873` n `12`; crypto_alt avg `-2.1993` n `230`; crypto_major avg `-0.4902` n `8`; equity avg `-0.4314` n `121`; fx avg `0.022` n `6`; index avg `-0.0479` n `25`; metal avg `-0.1209` n `20`; unknown avg `0.0234` n `777`
- 24h: commodity avg `0.211` n `12`; crypto_alt avg `5.995` n `230`; crypto_major avg `6.1552` n `8`; equity avg `-0.1844` n `121`; fx avg `0.0227` n `6`; index avg `-0.0633` n `25`; metal avg `0.0316` n `20`; unknown avg `1.1213` n `777`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `0.1583`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1479`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1435`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1434`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1422`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1368`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1361`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1264`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1248`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0986`, n `668`, weak_sample_signal
