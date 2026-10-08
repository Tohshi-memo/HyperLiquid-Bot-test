# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-08T16:07:46.759879+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-3.0087` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `2.9649` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-2.7808` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 1h_commodity_crypto_divergence: score `-2.7001` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 1h_index_leads_crypto: score `2.6509` - Index perps are stronger than crypto majors; possible risk-on canary.
- 1h_crypto_metal_divergence: score `-2.5798` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 1h_crypto_equity_divergence: score `-2.3` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_crypto_equity_divergence: score `-2.2507` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0273` n `13`; crypto_alt avg `-0.9633` n `235`; crypto_major avg `-0.5295` n `8`; equity avg `-0.0912` n `150`; fx avg `-0.0105` n `6`; index avg `-0.0104` n `26`; metal avg `-0.0331` n `20`; unknown avg `-0.3649` n `1069`
- 1h: commodity avg `-0.0017` n `13`; crypto_alt avg `-3.8459` n `235`; crypto_major avg `-2.7018` n `8`; equity avg `-0.4018` n `150`; fx avg `-0.0243` n `6`; index avg `-0.0509` n `26`; metal avg `-0.122` n `20`; unknown avg `0.4768` n `1069`
- 4h: commodity avg `-0.0312` n `13`; crypto_alt avg `-4.1176` n `235`; crypto_major avg `-3.0399` n `8`; equity avg `-0.7892` n `150`; fx avg `0.0071` n `6`; index avg `-0.075` n `26`; metal avg `-0.2591` n `20`; unknown avg `0.5661` n `1021`
- 24h: commodity avg `1.0115` n `13`; crypto_alt avg `-4.3583` n `235`; crypto_major avg `-5.1333` n `8`; equity avg `-2.2308` n `150`; fx avg `0.0545` n `6`; index avg `-0.285` n `26`; metal avg `-0.299` n `20`; unknown avg `22.525` n `990`

## Correlations

- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1745`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1595`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1536`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1529`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1465`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1453`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1391`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1363`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.136`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1344`, n `668`, weak_sample_signal
