# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-20T16:07:47.068383+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.7455` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `2.5815` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-2.5544` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 1h_commodity_crypto_divergence: score `-2.5372` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 1h_crypto_metal_divergence: score `-2.2177` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 1h_index_leads_crypto: score `2.18` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.038` n `13`; crypto_alt avg `0.3897` n `239`; crypto_major avg `0.4383` n `8`; equity avg `-0.0272` n `166`; fx avg `-0.014` n `6`; index avg `-0.0307` n `27`; metal avg `-0.0214` n `20`; unknown avg `0.8251` n `1245`
- 1h: commodity avg `0.0615` n `13`; crypto_alt avg `-2.5833` n `239`; crypto_major avg `-2.4757` n `8`; equity avg `-2.7419` n `166`; fx avg `0.0172` n `6`; index avg `-0.2957` n `27`; metal avg `-0.258` n `20`; unknown avg `160.7075` n `1243`
- 4h: commodity avg `-0.0003` n `13`; crypto_alt avg `-2.8098` n `239`; crypto_major avg `-2.7458` n `8`; equity avg `-1.7863` n `166`; fx avg `0.036` n `6`; index avg `-0.1643` n `27`; metal avg `-0.1914` n `20`; unknown avg `2.7142` n `1245`
- 24h: commodity avg `-0.4015` n `13`; crypto_alt avg `-5.9485` n `239`; crypto_major avg `-5.8541` n `8`; equity avg `-8.5727` n `166`; fx avg `-0.0331` n `6`; index avg `-0.7548` n `27`; metal avg `-1.0844` n `20`; unknown avg `48.5988` n `1150`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1673`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1536`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1502`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1213`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0971`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0937`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0841`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0809`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0771`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0747`, n `668`, weak_sample_signal
