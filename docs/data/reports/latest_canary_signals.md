# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-23T17:19:51.557548+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.677` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `-2.3642` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `2.3559` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_equity_divergence: score `-1.5612` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0372` n `12`; crypto_alt avg `0.5154` n `234`; crypto_major avg `0.421` n `8`; equity avg `0.1737` n `141`; fx avg `0.0123` n `6`; index avg `0.0267` n `26`; metal avg `-0.0176` n `20`; unknown avg `0.8553` n `939`
- 1h: commodity avg `-0.1539` n `12`; crypto_alt avg `-0.1101` n `234`; crypto_major avg `-0.2854` n `8`; equity avg `-0.1755` n `141`; fx avg `-0.0054` n `6`; index avg `-0.0431` n `26`; metal avg `-0.0729` n `20`; unknown avg `-0.1733` n `937`
- 4h: commodity avg `0.0866` n `12`; crypto_alt avg `-3.4971` n `234`; crypto_major avg `-2.5904` n `8`; equity avg `-1.0292` n `141`; fx avg `-0.0175` n `6`; index avg `-0.2345` n `26`; metal avg `-0.2262` n `20`; unknown avg `511.3079` n `891`
- 24h: commodity avg `0.2126` n `12`; crypto_alt avg `-2.5616` n `234`; crypto_major avg `-3.559` n `8`; equity avg `-1.1968` n `140`; fx avg `0.0064` n `6`; index avg `-0.3169` n `26`; metal avg `-0.6491` n `20`; unknown avg `12.1253` n `878`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.2606`, n `668`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.2044`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1573`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.136`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1333`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1307`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1273`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1152`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1149`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.095`, n `668`, weak_sample_signal
