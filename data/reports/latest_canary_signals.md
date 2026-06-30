# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-30T04:07:26.211102+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.96` - Polymarket crypto volume is unusually high.
- 4h_index_leads_crypto: score `1.2771` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0069` n `12`; crypto_alt avg `-0.1504` n `228`; crypto_major avg `-0.2449` n `8`; equity avg `0.0946` n `88`; fx avg `-0.0022` n `6`; index avg `0.0506` n `23`; metal avg `0.0585` n `20`; unknown avg `7.1781` n `765`
- 1h: commodity avg `-0.0653` n `12`; crypto_alt avg `-0.3493` n `228`; crypto_major avg `-0.555` n `8`; equity avg `0.1773` n `88`; fx avg `-0.0005` n `6`; index avg `0.0682` n `23`; metal avg `0.0337` n `20`; unknown avg `12.7862` n `765`
- 4h: commodity avg `-0.0077` n `12`; crypto_alt avg `-0.7932` n `228`; crypto_major avg `-1.2275` n `8`; equity avg `0.1566` n `88`; fx avg `-0.0165` n `6`; index avg `0.0496` n `23`; metal avg `-0.3059` n `20`; unknown avg `12.0283` n `763`
- 24h: commodity avg `-0.2645` n `12`; crypto_alt avg `-0.3601` n `228`; crypto_major avg `0.5655` n `8`; equity avg `2.2059` n `88`; fx avg `0.1223` n `6`; index avg `0.3535` n `23`; metal avg `-0.7328` n `20`; unknown avg `12.1543` n `728`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1278`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1084`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1036`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0944`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0922`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0873`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.085`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0797`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0757`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0745`, n `668`, weak_sample_signal
