# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-30T12:37:26.758489+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.1309` - Index perps are stronger than crypto majors; possible risk-on canary.
- 1h_index_leads_crypto: score `1.0713` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0388` n `12`; crypto_alt avg `-0.0879` n `228`; crypto_major avg `-0.2822` n `8`; equity avg `-0.1628` n `88`; fx avg `-0.0192` n `6`; index avg `-0.022` n `23`; metal avg `-0.1102` n `20`; unknown avg `-0.2176` n `765`
- 1h: commodity avg `0.2581` n `12`; crypto_alt avg `-0.8564` n `228`; crypto_major avg `-1.0899` n `8`; equity avg `-0.4513` n `88`; fx avg `-0.0174` n `6`; index avg `-0.0186` n `23`; metal avg `-0.2547` n `20`; unknown avg `-0.2602` n `765`
- 4h: commodity avg `0.3218` n `12`; crypto_alt avg `-1.275` n `228`; crypto_major avg `-1.1103` n `8`; equity avg `-0.3331` n `88`; fx avg `-0.0401` n `6`; index avg `0.0206` n `23`; metal avg `-0.0444` n `20`; unknown avg `-0.2152` n `765`
- 24h: commodity avg `0.5239` n `12`; crypto_alt avg `-2.7573` n `228`; crypto_major avg `-1.7414` n `8`; equity avg `0.8259` n `88`; fx avg `0.0643` n `6`; index avg `0.1426` n `23`; metal avg `-0.0738` n `20`; unknown avg `8.7378` n `734`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1217`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0911`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0892`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0835`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.079`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0558`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0524`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0522`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0504`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0472`, n `668`, weak_sample_signal
