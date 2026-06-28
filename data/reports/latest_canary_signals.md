# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-28T22:52:25.356505+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.1533` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0306` n `12`; crypto_alt avg `-0.2038` n `228`; crypto_major avg `-0.2216` n `8`; equity avg `-0.0514` n `88`; fx avg `0.0019` n `6`; index avg `-0.006` n `23`; metal avg `0.0047` n `20`; unknown avg `-0.0131` n `764`
- 1h: commodity avg `-0.167` n `12`; crypto_alt avg `-0.0888` n `228`; crypto_major avg `-0.3452` n `8`; equity avg `0.0956` n `88`; fx avg `0.0056` n `6`; index avg `0.0543` n `23`; metal avg `-0.1542` n `20`; unknown avg `0.0467` n `764`
- 4h: commodity avg `-0.3329` n `12`; crypto_alt avg `-0.9317` n `228`; crypto_major avg `-1.0226` n `8`; equity avg `0.2078` n `88`; fx avg `-0.0618` n `6`; index avg `0.1307` n `23`; metal avg `-0.1623` n `20`; unknown avg `0.2517` n `764`
- 24h: commodity avg `-0.1218` n `12`; crypto_alt avg `-1.0641` n `228`; crypto_major avg `-1.6925` n `8`; equity avg `0.2917` n `88`; fx avg `-0.1015` n `6`; index avg `0.1312` n `23`; metal avg `-0.162` n `20`; unknown avg `15.1038` n `690`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1881`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1774`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1232`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1177`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1112`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.105`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1018`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1016`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0875`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0867`, n `668`, weak_sample_signal
