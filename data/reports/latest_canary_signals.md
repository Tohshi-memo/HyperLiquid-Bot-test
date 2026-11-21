# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-21T12:37:26.604492+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.9592` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `2.8681` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `2.6178` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0101` n `13`; crypto_alt avg `0.4559` n `239`; crypto_major avg `0.5156` n `8`; equity avg `0.0908` n `166`; fx avg `-0.0077` n `6`; index avg `0.0081` n `27`; metal avg `0.0169` n `20`; unknown avg `160.629` n `1262`
- 1h: commodity avg `0.0174` n `13`; crypto_alt avg `0.6979` n `239`; crypto_major avg `0.9189` n `8`; equity avg `0.0262` n `166`; fx avg `-0.0091` n `6`; index avg `-0.0038` n `27`; metal avg `0.0353` n `20`; unknown avg `162.8555` n `1246`
- 4h: commodity avg `0.0225` n `13`; crypto_alt avg `2.2833` n `239`; crypto_major avg `2.9817` n `8`; equity avg `0.3639` n `166`; fx avg `0.0411` n `6`; index avg `0.033` n `27`; metal avg `0.1136` n `20`; unknown avg `167.3396` n `1222`
- 24h: commodity avg `0.5245` n `13`; crypto_alt avg `-3.6197` n `239`; crypto_major avg `-3.8371` n `8`; equity avg `-3.6645` n `166`; fx avg `-0.1267` n `6`; index avg `-0.414` n `27`; metal avg `-0.3444` n `20`; unknown avg `-0.1443` n `1145`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1531`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1494`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1401`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1217`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.099`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0958`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0926`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0904`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0842`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0777`, n `668`, weak_sample_signal
