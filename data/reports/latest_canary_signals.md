# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-14T21:52:33.768204+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-3.619` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `3.5937` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-3.2801` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `-3.1526` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 1h_index_leads_crypto: score `1.7741` - Index perps are stronger than crypto majors; possible risk-on canary.
- 1h_crypto_equity_divergence: score `-1.7546` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 1h_crypto_metal_divergence: score `-1.5907` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.0072` n `13`; crypto_alt avg `-0.0517` n `239`; crypto_major avg `-0.3271` n `8`; equity avg `0.1204` n `162`; fx avg `0.0063` n `6`; index avg `0.0073` n `27`; metal avg `0.0209` n `20`; unknown avg `-0.1251` n `1262`
- 1h: commodity avg `-0.0181` n `13`; crypto_alt avg `-1.1502` n `239`; crypto_major avg `-1.7773` n `8`; equity avg `-0.0227` n `162`; fx avg `0.0142` n `6`; index avg `-0.0032` n `27`; metal avg `-0.1866` n `20`; unknown avg `0.3441` n `1242`
- 4h: commodity avg `-0.0002` n `13`; crypto_alt avg `-3.7496` n `239`; crypto_major avg `-3.6192` n `8`; equity avg `-0.4666` n `162`; fx avg `0.0116` n `6`; index avg `-0.0255` n `27`; metal avg `-0.3391` n `20`; unknown avg `-0.194` n `1214`
- 24h: commodity avg `-0.1363` n `13`; crypto_alt avg `-9.2577` n `239`; crypto_major avg `-8.8322` n `8`; equity avg `-1.8397` n `162`; fx avg `-0.0036` n `6`; index avg `-0.1689` n `27`; metal avg `-0.533` n `20`; unknown avg `0.0098` n `1098`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1416`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1238`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1145`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1135`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1117`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1031`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0989`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0943`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0922`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0843`, n `668`, weak_sample_signal
