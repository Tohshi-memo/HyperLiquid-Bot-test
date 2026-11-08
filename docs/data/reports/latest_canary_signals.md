# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-08T23:52:26.435005+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.8348` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `-2.7653` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `2.5919` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0046` n `13`; crypto_alt avg `-0.5993` n `239`; crypto_major avg `-0.7302` n `8`; equity avg `-0.3973` n `158`; fx avg `-0.0101` n `6`; index avg `-0.0637` n `27`; metal avg `-0.0557` n `20`; unknown avg `-0.4326` n `1260`
- 1h: commodity avg `-0.1063` n `13`; crypto_alt avg `0.0739` n `239`; crypto_major avg `-0.0269` n `8`; equity avg `-0.0621` n `158`; fx avg `-0.0107` n `6`; index avg `-0.0079` n `27`; metal avg `0.0912` n `20`; unknown avg `0.6582` n `1244`
- 4h: commodity avg `0.0565` n `13`; crypto_alt avg `-2.2645` n `239`; crypto_major avg `-2.7783` n `8`; equity avg `-1.3968` n `158`; fx avg `-0.0365` n `6`; index avg `-0.1864` n `27`; metal avg `-0.013` n `20`; unknown avg `3.3633` n `1176`
- 24h: commodity avg `-0.028` n `13`; crypto_alt avg `-3.6153` n `239`; crypto_major avg `-3.09` n `8`; equity avg `-0.9464` n `158`; fx avg `0.0236` n `6`; index avg `-0.1694` n `27`; metal avg `-0.0329` n `20`; unknown avg `0.0546` n `1000`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2005`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1646`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1597`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1203`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1166`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1134`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1126`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1029`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0961`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0936`, n `668`, weak_sample_signal
