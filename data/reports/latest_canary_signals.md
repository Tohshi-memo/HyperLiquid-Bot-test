# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-21T14:07:27.243712+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `3.6024` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `3.4961` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `2.6112` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0001` n `13`; crypto_alt avg `0.0001` n `239`; crypto_major avg `-0.1054` n `8`; equity avg `-0.0245` n `166`; fx avg `0.0015` n `6`; index avg `0.0002` n `27`; metal avg `-0.0216` n `20`; unknown avg `0.0878` n `1254`
- 1h: commodity avg `0.0091` n `13`; crypto_alt avg `1.1669` n `239`; crypto_major avg `1.3921` n `8`; equity avg `0.7058` n `166`; fx avg `0.0096` n `6`; index avg `0.0828` n `27`; metal avg `0.0856` n `20`; unknown avg `160.0001` n `1256`
- 4h: commodity avg `0.0622` n `13`; crypto_alt avg `2.5844` n `239`; crypto_major avg `3.6646` n `8`; equity avg `1.0534` n `166`; fx avg `0.0045` n `6`; index avg `0.1216` n `27`; metal avg `0.1685` n `20`; unknown avg `0.4811` n `1220`
- 24h: commodity avg `0.4235` n `13`; crypto_alt avg `-2.2309` n `239`; crypto_major avg `-2.2265` n `8`; equity avg `-3.4381` n `166`; fx avg `-0.1012` n `6`; index avg `-0.3688` n `27`; metal avg `-0.2055` n `20`; unknown avg `-0.1396` n `1147`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1517`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1491`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1388`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1214`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1088`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.104`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1025`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0927`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0926`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0846`, n `668`, weak_sample_signal
