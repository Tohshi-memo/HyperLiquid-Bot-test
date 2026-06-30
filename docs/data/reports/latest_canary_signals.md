# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-30T15:09:33.830810+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.5322` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0105` n `12`; crypto_alt avg `-0.2692` n `228`; crypto_major avg `-0.2021` n `8`; equity avg `-0.0293` n `88`; fx avg `0.0305` n `6`; index avg `0.0266` n `23`; metal avg `-0.1024` n `20`; unknown avg `-0.1765` n `765`
- 1h: commodity avg `-0.0492` n `12`; crypto_alt avg `-0.5101` n `228`; crypto_major avg `-0.8613` n `8`; equity avg `-0.0576` n `88`; fx avg `0.0848` n `6`; index avg `0.0338` n `23`; metal avg `0.1062` n `20`; unknown avg `-0.3593` n `765`
- 4h: commodity avg `0.1381` n `12`; crypto_alt avg `-0.9691` n `228`; crypto_major avg `-1.372` n `8`; equity avg `-0.0745` n `88`; fx avg `0.0837` n `6`; index avg `0.1602` n `23`; metal avg `-0.0576` n `20`; unknown avg `-0.1753` n `765`
- 24h: commodity avg `0.3475` n `12`; crypto_alt avg `-1.0971` n `228`; crypto_major avg `-0.5044` n `8`; equity avg `2.1935` n `88`; fx avg `0.1518` n `6`; index avg `0.4642` n `23`; metal avg `0.4178` n `20`; unknown avg `8.6736` n `735`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1223`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0987`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.089`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0858`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.085`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0803`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0742`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0657`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0605`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0594`, n `668`, weak_sample_signal
