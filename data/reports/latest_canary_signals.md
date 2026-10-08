# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-08T21:37:30.560204+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `2.1392` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_commodity_crypto_divergence: score `2.0904` - Commodity perps and crypto are moving differently; check macro-linked stress.

## Class Returns

- 15m: commodity avg `-0.0045` n `13`; crypto_alt avg `-0.0142` n `235`; crypto_major avg `0.0061` n `8`; equity avg `0.0134` n `150`; fx avg `0.0041` n `6`; index avg `-0.0033` n `26`; metal avg `0.0007` n `20`; unknown avg `0.0161` n `1077`
- 1h: commodity avg `0.1117` n `13`; crypto_alt avg `-0.0116` n `235`; crypto_major avg `0.191` n `8`; equity avg `0.0126` n `150`; fx avg `-0.0025` n `6`; index avg `-0.0036` n `26`; metal avg `0.0106` n `20`; unknown avg `-0.085` n `1067`
- 4h: commodity avg `0.0756` n `13`; crypto_alt avg `2.6934` n `235`; crypto_major avg `2.166` n `8`; equity avg `0.7471` n `150`; fx avg `0.0356` n `6`; index avg `0.1102` n `26`; metal avg `0.0268` n `20`; unknown avg `0.7252` n `1007`
- 24h: commodity avg `0.708` n `13`; crypto_alt avg `-2.3988` n `235`; crypto_major avg `-3.104` n `8`; equity avg `-2.7288` n `150`; fx avg `0.0647` n `6`; index avg `-0.3496` n `26`; metal avg `-0.0176` n `20`; unknown avg `6.0443` n `991`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.1814`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1639`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1427`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1352`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1284`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1248`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1208`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1192`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1168`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1109`, n `668`, weak_sample_signal
