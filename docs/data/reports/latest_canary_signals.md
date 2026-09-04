# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-04T14:52:31.671880+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.9988` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_equity_divergence: score `-2.8802` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_index_leads_crypto: score `2.7331` - Index perps are stronger than crypto majors; possible risk-on canary.
- polymarket_volume_spike: score `2.68` - Polymarket crypto volume is unusually high.
- 4h_crypto_metal_divergence: score `-2.511` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 1h_index_leads_crypto: score `1.0228` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.1377` n `12`; crypto_alt avg `-0.494` n `232`; crypto_major avg `-0.4105` n `8`; equity avg `-0.2259` n `133`; fx avg `0.0291` n `6`; index avg `-0.0359` n `26`; metal avg `-0.0874` n `20`; unknown avg `0.3482` n `793`
- 1h: commodity avg `0.4264` n `12`; crypto_alt avg `-1.227` n `232`; crypto_major avg `-1.0696` n `8`; equity avg `0.0204` n `133`; fx avg `0.0502` n `6`; index avg `-0.0468` n `26`; metal avg `-0.0526` n `20`; unknown avg `0.3446` n `787`
- 4h: commodity avg `0.2412` n `12`; crypto_alt avg `-2.3023` n `232`; crypto_major avg `-2.7576` n `8`; equity avg `0.1226` n `133`; fx avg `-0.0972` n `6`; index avg `-0.0245` n `26`; metal avg `-0.2466` n `20`; unknown avg `0.3685` n `737`
- 24h: commodity avg `-0.1357` n `12`; crypto_alt avg `-1.2501` n `232`; crypto_major avg `-1.5257` n `8`; equity avg `2.1506` n `133`; fx avg `-0.0681` n `6`; index avg `0.3221` n `26`; metal avg `-0.1655` n `20`; unknown avg `0.889` n `698`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1141`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1075`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0964`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0858`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0805`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0773`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0752`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0732`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0726`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0611`, n `668`, weak_sample_signal
