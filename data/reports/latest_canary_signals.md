# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-14T14:37:31.588362+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `2.1818` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-2.1538` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_commodity_crypto_divergence: score `-2.1534` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_equity_divergence: score `-1.6968` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 1h_index_leads_crypto: score `1.4298` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0306` n `13`; crypto_alt avg `-0.0817` n `239`; crypto_major avg `-0.3072` n `8`; equity avg `-0.1078` n `162`; fx avg `0.0013` n `6`; index avg `-0.0135` n `27`; metal avg `-0.0123` n `20`; unknown avg `-0.0005` n `1262`
- 1h: commodity avg `-0.0348` n `13`; crypto_alt avg `-1.5861` n `239`; crypto_major avg `-1.4554` n `8`; equity avg `-0.3095` n `162`; fx avg `-0.0004` n `6`; index avg `-0.0256` n `27`; metal avg `-0.0476` n `20`; unknown avg `317.2981` n `1258`
- 4h: commodity avg `-0.0678` n `13`; crypto_alt avg `-2.1464` n `239`; crypto_major avg `-2.2212` n `8`; equity avg `-0.5244` n `162`; fx avg `0.0081` n `6`; index avg `-0.0394` n `27`; metal avg `-0.0674` n `20`; unknown avg `0.218` n `1250`
- 24h: commodity avg `-0.2282` n `13`; crypto_alt avg `-5.912` n `239`; crypto_major avg `-5.7989` n `8`; equity avg `-2.2659` n `162`; fx avg `-0.1252` n `6`; index avg `-0.1846` n `27`; metal avg `-0.4` n `20`; unknown avg `0.4363` n `1096`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1416`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1208`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1164`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1143`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1127`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1107`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1105`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0958`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0956`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0945`, n `668`, weak_sample_signal
