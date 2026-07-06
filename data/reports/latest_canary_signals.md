# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-06T12:07:29.067188+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.0121` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `1.7747` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-1.6506` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 1h_index_leads_crypto: score `1.4555` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.071` n `12`; crypto_alt avg `-1.7091` n `229`; crypto_major avg `-1.5546` n `8`; equity avg `-0.1324` n `88`; fx avg `-0.002` n `6`; index avg `0.0109` n `25`; metal avg `0.0283` n `20`; unknown avg `-0.058` n `765`
- 1h: commodity avg `0.1324` n `12`; crypto_alt avg `-1.7108` n `229`; crypto_major avg `-1.4199` n `8`; equity avg `0.0043` n `88`; fx avg `0.0114` n `6`; index avg `0.0356` n `25`; metal avg `0.0238` n `20`; unknown avg `-0.1819` n `765`
- 4h: commodity avg `0.2285` n `12`; crypto_alt avg `-1.7064` n `229`; crypto_major avg `-1.7836` n `8`; equity avg `-0.3082` n `88`; fx avg `0.0054` n `6`; index avg `-0.0089` n `25`; metal avg `-0.133` n `20`; unknown avg `-0.1456` n `765`
- 24h: commodity avg `-0.0329` n `12`; crypto_alt avg `-1.2069` n `229`; crypto_major avg `-0.538` n `8`; equity avg `-0.7855` n `88`; fx avg `0.0796` n `6`; index avg `0.0053` n `25`; metal avg `-0.1588` n `20`; unknown avg `0.683` n `661`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1077`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0913`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0899`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0869`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0796`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0694`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0683`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0655`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0635`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0562`, n `668`, weak_sample_signal
