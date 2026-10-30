# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-30T00:07:30.087386+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `2.8603` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_commodity_crypto_divergence: score `-2.8571` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `-2.7883` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `-1.8899` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0087` n `13`; crypto_alt avg `-0.0951` n `238`; crypto_major avg `0.0316` n `8`; equity avg `0.1644` n `156`; fx avg `-0.0055` n `6`; index avg `-0.0276` n `27`; metal avg `-0.0298` n `20`; unknown avg `1.088` n `1238`
- 1h: commodity avg `0.0128` n `13`; crypto_alt avg `-0.5402` n `238`; crypto_major avg `-0.6845` n `8`; equity avg `0.22` n `156`; fx avg `-0.0148` n `6`; index avg `0.0142` n `27`; metal avg `-0.0588` n `20`; unknown avg `1.7172` n `1238`
- 4h: commodity avg `-0.081` n `13`; crypto_alt avg `-4.1959` n `238`; crypto_major avg `-2.9381` n `8`; equity avg `-1.0482` n `156`; fx avg `0.0233` n `6`; index avg `-0.0778` n `27`; metal avg `-0.1498` n `20`; unknown avg `139.1618` n `1168`
- 24h: commodity avg `-0.2056` n `13`; crypto_alt avg `-6.6108` n `238`; crypto_major avg `-3.0843` n `8`; equity avg `-3.5309` n `155`; fx avg `0.094` n `6`; index avg `-0.329` n `27`; metal avg `-0.6576` n `20`; unknown avg `29.4719` n `988`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.11`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.094`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0901`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0843`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0841`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0789`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0766`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0702`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0651`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0618`, n `668`, weak_sample_signal
