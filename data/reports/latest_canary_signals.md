# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-21T05:37:30.336041+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-4.0254` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `3.9464` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-3.8605` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `-2.7111` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0137` n `13`; crypto_alt avg `-0.2865` n `239`; crypto_major avg `-0.5242` n `8`; equity avg `-0.0468` n `166`; fx avg `0.0007` n `6`; index avg `-0.0002` n `27`; metal avg `-0.0277` n `20`; unknown avg `0.0131` n `1262`
- 1h: commodity avg `0.0207` n `13`; crypto_alt avg `0.0516` n `239`; crypto_major avg `0.1951` n `8`; equity avg `0.205` n `166`; fx avg `-0.0075` n `6`; index avg `0.0234` n `27`; metal avg `0.0196` n `20`; unknown avg `369.3838` n `1256`
- 4h: commodity avg `-0.0118` n `13`; crypto_alt avg `-3.2482` n `239`; crypto_major avg `-4.0372` n `8`; equity avg `-1.3261` n `166`; fx avg `-0.0348` n `6`; index avg `-0.0908` n `27`; metal avg `-0.1767` n `20`; unknown avg `1.1079` n `1242`
- 24h: commodity avg `0.3038` n `13`; crypto_alt avg `-6.7522` n `239`; crypto_major avg `-8.6349` n `8`; equity avg `-5.4557` n `166`; fx avg `-0.0512` n `6`; index avg `-0.5466` n `27`; metal avg `0.0252` n `20`; unknown avg `12.8054` n `1111`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1602`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1511`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1454`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1221`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0969`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0903`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0861`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0841`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0792`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0781`, n `668`, weak_sample_signal
