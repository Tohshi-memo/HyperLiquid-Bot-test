# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-18T16:22:30.262236+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.2943` - Commodity perps and crypto are moving differently; check macro-linked stress.
- polymarket_volume_spike: score `2.28` - Polymarket crypto volume is unusually high.
- 4h_index_leads_crypto: score `2.1996` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-2.0994` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 1h_index_leads_crypto: score `1.2017` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0248` n `13`; crypto_alt avg `-0.6172` n `239`; crypto_major avg `-0.6253` n `8`; equity avg `-0.5487` n `164`; fx avg `-0.0204` n `6`; index avg `-0.0659` n `27`; metal avg `-0.0523` n `20`; unknown avg `0.6945` n `1263`
- 1h: commodity avg `-0.0449` n `13`; crypto_alt avg `-1.2515` n `239`; crypto_major avg `-1.3384` n `8`; equity avg `-1.1542` n `164`; fx avg `-0.0345` n `6`; index avg `-0.1367` n `27`; metal avg `-0.1207` n `20`; unknown avg `0.3272` n `1257`
- 4h: commodity avg `-0.1424` n `13`; crypto_alt avg `-1.8211` n `239`; crypto_major avg `-2.4367` n `8`; equity avg `-2.324` n `164`; fx avg `-0.0421` n `6`; index avg `-0.2371` n `27`; metal avg `-0.3373` n `20`; unknown avg `1.1095` n `1257`
- 24h: commodity avg `-0.3724` n `13`; crypto_alt avg `-0.9893` n `239`; crypto_major avg `-1.2769` n `8`; equity avg `-0.0129` n `164`; fx avg `-0.2145` n `6`; index avg `-0.0063` n `27`; metal avg `-1.2236` n `20`; unknown avg `-0.4377` n `1138`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1372`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1275`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0981`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0827`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0756`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0752`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0613`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0583`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0539`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0502`, n `668`, weak_sample_signal
