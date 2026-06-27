# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-27T19:22:32.942052+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.0481` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0012` n `12`; crypto_alt avg `-0.2201` n `228`; crypto_major avg `-0.2108` n `8`; equity avg `-0.0131` n `88`; fx avg `-0.0017` n `6`; index avg `-0.006` n `23`; metal avg `-0.008` n `20`; unknown avg `0.0462` n `764`
- 1h: commodity avg `-0.0122` n `12`; crypto_alt avg `-0.0637` n `228`; crypto_major avg `-0.1566` n `8`; equity avg `0.0176` n `88`; fx avg `-0.001` n `6`; index avg `-0.0198` n `23`; metal avg `-0.0137` n `20`; unknown avg `-0.1303` n `764`
- 4h: commodity avg `-0.1589` n `12`; crypto_alt avg `-0.7003` n `228`; crypto_major avg `-1.0992` n `8`; equity avg `-0.1394` n `88`; fx avg `0.0021` n `6`; index avg `-0.0511` n `23`; metal avg `-0.0488` n `20`; unknown avg `0.2001` n `764`
- 24h: commodity avg `0.2424` n `12`; crypto_alt avg `-0.3655` n `228`; crypto_major avg `-0.4399` n `8`; equity avg `0.6564` n `88`; fx avg `0.0769` n `6`; index avg `-0.0609` n `23`; metal avg `0.1086` n `20`; unknown avg `-0.1824` n `700`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.2092`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1666`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1352`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1116`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1064`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0961`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0892`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0855`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0852`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0788`, n `668`, weak_sample_signal
