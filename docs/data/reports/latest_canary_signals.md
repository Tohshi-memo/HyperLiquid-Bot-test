# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-14T15:52:25.504896+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `2.5794` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_commodity_crypto_divergence: score `-2.5734` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `-2.3923` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `-1.9822` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0082` n `13`; crypto_alt avg `0.1462` n `239`; crypto_major avg `-0.1044` n `8`; equity avg `0.0345` n `162`; fx avg `0.01` n `6`; index avg `0.0037` n `27`; metal avg `-0.1046` n `20`; unknown avg `5.7798` n `1262`
- 1h: commodity avg `-0.0219` n `13`; crypto_alt avg `-0.1454` n `239`; crypto_major avg `-0.305` n `8`; equity avg `-0.1176` n `162`; fx avg `-0.0008` n `6`; index avg `-0.0089` n `27`; metal avg `-0.1649` n `20`; unknown avg `4.7146` n `1256`
- 4h: commodity avg `-0.0603` n `13`; crypto_alt avg `-2.4849` n `239`; crypto_major avg `-2.6337` n `8`; equity avg `-0.6515` n `162`; fx avg `0.0145` n `6`; index avg `-0.0543` n `27`; metal avg `-0.2414` n `20`; unknown avg `-0.0023` n `1250`
- 24h: commodity avg `-0.0999` n `13`; crypto_alt avg `-5.3836` n `239`; crypto_major avg `-5.2465` n `8`; equity avg `-0.7023` n `162`; fx avg `-0.0761` n `6`; index avg `-0.0271` n `27`; metal avg `-0.3971` n `20`; unknown avg `1.3952` n `1096`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1407`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1216`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1155`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1146`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1125`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1123`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.109`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1066`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0994`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0952`, n `668`, weak_sample_signal
