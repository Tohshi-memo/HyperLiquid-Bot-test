# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-30T00:37:35.772580+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.0435` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0439` n `12`; crypto_alt avg `-0.6098` n `228`; crypto_major avg `-0.6407` n `8`; equity avg `-0.3615` n `88`; fx avg `0.0052` n `6`; index avg `-0.1042` n `23`; metal avg `-0.1306` n `20`; unknown avg `0.1385` n `765`
- 1h: commodity avg `-0.0014` n `12`; crypto_alt avg `-0.7061` n `228`; crypto_major avg `-0.8643` n `8`; equity avg `-0.6114` n `88`; fx avg `0.0577` n `6`; index avg `-0.1541` n `23`; metal avg `-0.272` n `20`; unknown avg `0.2422` n `765`
- 4h: commodity avg `-0.0715` n `12`; crypto_alt avg `-1.1371` n `228`; crypto_major avg `-1.1852` n `8`; equity avg `-0.4034` n `88`; fx avg `0.0746` n `6`; index avg `-0.1417` n `23`; metal avg `-0.1712` n `20`; unknown avg `1.1691` n `763`
- 24h: commodity avg `-0.2266` n `12`; crypto_alt avg `1.3772` n `228`; crypto_major avg `2.6237` n `8`; equity avg `2.0651` n `88`; fx avg `0.2233` n `6`; index avg `0.2626` n `23`; metal avg `-0.3597` n `20`; unknown avg `1.6766` n `730`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1545`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1264`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1083`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1077`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.107`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1033`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0959`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0957`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0906`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0894`, n `668`, weak_sample_signal
