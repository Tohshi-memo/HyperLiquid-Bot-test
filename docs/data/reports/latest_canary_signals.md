# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-01T23:22:25.765012+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 1h_index_leads_crypto: score `1.2186` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0005` n `12`; crypto_alt avg `-0.0858` n `228`; crypto_major avg `-0.0643` n `8`; equity avg `-0.1502` n `88`; fx avg `0.0018` n `6`; index avg `-0.0259` n `25`; metal avg `-0.0431` n `20`; unknown avg `0.0719` n `763`
- 1h: commodity avg `0.0013` n `12`; crypto_alt avg `-1.0396` n `228`; crypto_major avg `-1.2711` n `8`; equity avg `-0.284` n `88`; fx avg `0.0019` n `6`; index avg `-0.0525` n `25`; metal avg `-0.0307` n `20`; unknown avg `201.177` n `763`
- 4h: commodity avg `-0.0738` n `12`; crypto_alt avg `0.1019` n `228`; crypto_major avg `-0.4357` n `8`; equity avg `-0.6119` n `88`; fx avg `0.0438` n `6`; index avg `-0.1081` n `25`; metal avg `-0.2156` n `20`; unknown avg `202.9686` n `763`
- 24h: commodity avg `-0.6306` n `12`; crypto_alt avg `2.0319` n `228`; crypto_major avg `1.5926` n `8`; equity avg `-1.8399` n `88`; fx avg `0.058` n `6`; index avg `-0.5395` n `25`; metal avg `0.2301` n `20`; unknown avg `209.4121` n `739`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1235`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1188`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.101`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0961`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0926`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0837`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0831`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0831`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0794`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0696`, n `668`, weak_sample_signal
