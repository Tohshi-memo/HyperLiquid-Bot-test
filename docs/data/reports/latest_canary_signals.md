# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-30T13:22:31.357762+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.1748` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.1235` n `12`; crypto_alt avg `0.1772` n `228`; crypto_major avg `0.139` n `8`; equity avg `0.0483` n `88`; fx avg `0.0074` n `6`; index avg `0.0095` n `23`; metal avg `0.0589` n `20`; unknown avg `-0.0439` n `765`
- 1h: commodity avg `-0.1132` n `12`; crypto_alt avg `0.0124` n `228`; crypto_major avg `-0.2431` n `8`; equity avg `-0.2676` n `88`; fx avg `0.0084` n `6`; index avg `-0.015` n `23`; metal avg `-0.0054` n `20`; unknown avg `-0.2457` n `765`
- 4h: commodity avg `0.1925` n `12`; crypto_alt avg `-1.2445` n `228`; crypto_major avg `-1.1498` n `8`; equity avg `-0.4125` n `88`; fx avg `0.004` n `6`; index avg `0.025` n `23`; metal avg `0.0369` n `20`; unknown avg `-0.191` n `765`
- 24h: commodity avg `0.387` n `12`; crypto_alt avg `-2.4089` n `228`; crypto_major avg `-1.6355` n `8`; equity avg `0.7776` n `88`; fx avg `0.0998` n `6`; index avg `0.1636` n `23`; metal avg `0.0576` n `20`; unknown avg `8.6738` n `734`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1227`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0926`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0897`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0868`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0855`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0675`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0569`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0512`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0504`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0471`, n `668`, weak_sample_signal
