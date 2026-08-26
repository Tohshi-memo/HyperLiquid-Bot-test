# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-26T14:52:37.534959+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.1933` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `1.845` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-1.6532` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.0238` n `12`; crypto_alt avg `-0.5277` n `231`; crypto_major avg `-0.3268` n `8`; equity avg `-0.0154` n `122`; fx avg `-0.0104` n `6`; index avg `0.019` n `25`; metal avg `-0.0287` n `20`; unknown avg `-0.1003` n `797`
- 1h: commodity avg `0.0831` n `12`; crypto_alt avg `-0.4193` n `231`; crypto_major avg `-0.4312` n `8`; equity avg `-0.3828` n `122`; fx avg `-0.0193` n `6`; index avg `-0.0441` n `25`; metal avg `-0.1086` n `20`; unknown avg `-0.1131` n `797`
- 4h: commodity avg `0.3533` n `12`; crypto_alt avg `-1.6541` n `231`; crypto_major avg `-1.84` n `8`; equity avg `-0.3421` n `122`; fx avg `-0.0135` n `6`; index avg `0.005` n `25`; metal avg `-0.1868` n `20`; unknown avg `-0.2195` n `797`
- 24h: commodity avg `0.2128` n `12`; crypto_alt avg `-2.3353` n `231`; crypto_major avg `-2.2` n `8`; equity avg `-0.2808` n `122`; fx avg `-0.0609` n `6`; index avg `0.0503` n `25`; metal avg `-0.0948` n `20`; unknown avg `0.3671` n `779`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1625`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1274`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1081`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1071`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1014`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1007`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.094`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0863`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0854`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0755`, n `668`, weak_sample_signal
