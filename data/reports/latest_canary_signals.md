# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-20T16:52:26.744276+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-3.2559` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `3.0197` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-2.9678` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0163` n `13`; crypto_alt avg `-0.1968` n `239`; crypto_major avg `-0.1082` n `8`; equity avg `-0.2935` n `166`; fx avg `0.0124` n `6`; index avg `-0.035` n `27`; metal avg `-0.0612` n `20`; unknown avg `1.861` n `1261`
- 1h: commodity avg `0.1085` n `13`; crypto_alt avg `0.4213` n `239`; crypto_major avg `0.3715` n `8`; equity avg `-1.1085` n `166`; fx avg `-0.0008` n `6`; index avg `-0.1494` n `27`; metal avg `-0.1209` n `20`; unknown avg `22.263` n `1249`
- 4h: commodity avg `-0.0377` n `13`; crypto_alt avg `-3.1305` n `239`; crypto_major avg `-3.2936` n `8`; equity avg `-2.9252` n `166`; fx avg `0.0068` n `6`; index avg `-0.2739` n `27`; metal avg `-0.3258` n `20`; unknown avg `1.3338` n `1247`
- 24h: commodity avg `-0.3323` n `13`; crypto_alt avg `-5.6397` n `239`; crypto_major avg `-5.7574` n `8`; equity avg `-9.0349` n `166`; fx avg `0.001` n `6`; index avg `-0.7785` n `27`; metal avg `-1.2483` n `20`; unknown avg `40.4673` n `1153`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1679`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1532`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1512`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1213`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0937`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0899`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0829`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0792`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0792`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0783`, n `668`, weak_sample_signal
