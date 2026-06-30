# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-30T15:07:30.062039+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.5541` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.016` n `12`; crypto_alt avg `-0.2516` n `228`; crypto_major avg `-0.2325` n `8`; equity avg `-0.0628` n `88`; fx avg `0.0294` n `6`; index avg `0.0187` n `23`; metal avg `-0.0783` n `20`; unknown avg `-0.143` n `765`
- 1h: commodity avg `-0.0548` n `12`; crypto_alt avg `-0.4923` n `228`; crypto_major avg `-0.8915` n `8`; equity avg `-0.0908` n `88`; fx avg `0.0837` n `6`; index avg `0.0259` n `23`; metal avg `0.1305` n `20`; unknown avg `-0.3251` n `765`
- 4h: commodity avg `0.1323` n `12`; crypto_alt avg `-0.951` n `228`; crypto_major avg `-1.4019` n `8`; equity avg `-0.1072` n `88`; fx avg `0.0827` n `6`; index avg `0.1522` n `23`; metal avg `-0.0333` n `20`; unknown avg `-0.1379` n `765`
- 24h: commodity avg `0.3417` n `12`; crypto_alt avg `-1.0793` n `228`; crypto_major avg `-0.5347` n `8`; equity avg `2.1595` n `88`; fx avg `0.1507` n `6`; index avg `0.4559` n `23`; metal avg `0.4423` n `20`; unknown avg `8.7126` n `735`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1224`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0985`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0891`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0858`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.085`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.08`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0748`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0656`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0609`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0598`, n `668`, weak_sample_signal
