# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-29T16:37:35.782599+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.336` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `2.2209` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.037` n `13`; crypto_alt avg `-0.1377` n `238`; crypto_major avg `-0.1182` n `8`; equity avg `-0.1145` n `156`; fx avg `-0.0049` n `6`; index avg `-0.0094` n `27`; metal avg `-0.0296` n `20`; unknown avg `1.4189` n `1238`
- 1h: commodity avg `0.1491` n `13`; crypto_alt avg `0.0849` n `238`; crypto_major avg `0.1447` n `8`; equity avg `-0.3528` n `156`; fx avg `0.0378` n `6`; index avg `-0.0404` n `27`; metal avg `-0.0356` n `20`; unknown avg `0.9826` n `1226`
- 4h: commodity avg `-0.1489` n `13`; crypto_alt avg `2.0088` n `238`; crypto_major avg `2.1871` n `8`; equity avg `0.9151` n `156`; fx avg `0.0825` n `6`; index avg `0.0153` n `27`; metal avg `-0.0338` n `20`; unknown avg `28.1376` n `1132`
- 24h: commodity avg `-0.8631` n `13`; crypto_alt avg `1.4327` n `238`; crypto_major avg `3.0277` n `8`; equity avg `-0.4086` n `155`; fx avg `0.0097` n `6`; index avg `-0.109` n `27`; metal avg `-0.4739` n `20`; unknown avg `45.5996` n `946`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1114`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0907`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0861`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0848`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0796`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.075`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0729`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0683`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0628`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0551`, n `668`, weak_sample_signal
