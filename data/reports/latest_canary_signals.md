# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-02T21:07:29.715355+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.81` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0056` n `12`; crypto_alt avg `0.0503` n `229`; crypto_major avg `0.0066` n `8`; equity avg `-0.0521` n `88`; fx avg `-0.0544` n `6`; index avg `0.0139` n `25`; metal avg `0.0414` n `20`; unknown avg `-0.2617` n `765`
- 1h: commodity avg `-0.0096` n `12`; crypto_alt avg `-0.0103` n `229`; crypto_major avg `-0.0324` n `8`; equity avg `-0.0754` n `88`; fx avg `-0.0427` n `6`; index avg `0.0109` n `25`; metal avg `0.0445` n `20`; unknown avg `-0.4054` n `765`
- 4h: commodity avg `0.1012` n `12`; crypto_alt avg `0.0282` n `229`; crypto_major avg `-0.1568` n `8`; equity avg `0.2952` n `88`; fx avg `-0.0128` n `6`; index avg `0.1003` n `25`; metal avg `0.0399` n `20`; unknown avg `0.3553` n `763`
- 24h: commodity avg `0.0785` n `12`; crypto_alt avg `1.9548` n `228`; crypto_major avg `2.7929` n `8`; equity avg `-2.2816` n `88`; fx avg `-0.142` n `6`; index avg `-0.4425` n `25`; metal avg `1.0209` n `20`; unknown avg `1.3607` n `739`

## Correlations

- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0904`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0884`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0838`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0773`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0703`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.067`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0653`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.064`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0633`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0621`, n `668`, weak_sample_signal
