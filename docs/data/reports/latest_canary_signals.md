# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-14T22:22:22.428174+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-3.0527` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `2.98` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-2.6999` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `-2.6191` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0782` n `13`; crypto_alt avg `0.5943` n `239`; crypto_major avg `0.7216` n `8`; equity avg `0.131` n `162`; fx avg `0.0058` n `6`; index avg `0.0143` n `27`; metal avg `0.0332` n `20`; unknown avg `1.0936` n `1260`
- 1h: commodity avg `0.0825` n `13`; crypto_alt avg `0.4184` n `239`; crypto_major avg `-0.0983` n `8`; equity avg `0.2639` n `162`; fx avg `0.0023` n `6`; index avg `0.0317` n `27`; metal avg `0.0508` n `20`; unknown avg `-0.2635` n `1254`
- 4h: commodity avg `0.0801` n `13`; crypto_alt avg `-2.9032` n `239`; crypto_major avg `-2.9726` n `8`; equity avg `-0.3535` n `162`; fx avg `0.0064` n `6`; index avg `0.0074` n `27`; metal avg `-0.2727` n `20`; unknown avg `0.3692` n `1208`
- 24h: commodity avg `0.0035` n `13`; crypto_alt avg `-8.528` n `239`; crypto_major avg `-8.2869` n `8`; equity avg `-1.7115` n `162`; fx avg `-0.0132` n `6`; index avg `-0.1337` n `27`; metal avg `-0.4927` n `20`; unknown avg `0.2171` n `1098`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1413`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1234`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1151`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1131`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1122`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1036`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0945`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0923`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0919`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0845`, n `668`, weak_sample_signal
