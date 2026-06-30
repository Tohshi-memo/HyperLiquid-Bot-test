# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-30T03:22:28.407370+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.14` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0019` n `12`; crypto_alt avg `-0.0037` n `228`; crypto_major avg `0.0501` n `8`; equity avg `0.0333` n `88`; fx avg `-0.0005` n `6`; index avg `-0.0008` n `23`; metal avg `0.0596` n `20`; unknown avg `2.2932` n `765`
- 1h: commodity avg `0.0481` n `12`; crypto_alt avg `0.3585` n `228`; crypto_major avg `0.2693` n `8`; equity avg `0.1808` n `88`; fx avg `-0.015` n `6`; index avg `0.0472` n `23`; metal avg `0.1922` n `20`; unknown avg `2.2541` n `765`
- 4h: commodity avg `0.0746` n `12`; crypto_alt avg `-0.316` n `228`; crypto_major avg `-0.6794` n `8`; equity avg `0.0341` n `88`; fx avg `0.018` n `6`; index avg `0.0042` n `23`; metal avg `-0.4424` n `20`; unknown avg `2.26` n `763`
- 24h: commodity avg `-0.1868` n `12`; crypto_alt avg `-0.3108` n `228`; crypto_major avg `0.9347` n `8`; equity avg `2.0909` n `88`; fx avg `0.1331` n `6`; index avg `0.3112` n `23`; metal avg `-0.8928` n `20`; unknown avg `4.2869` n `728`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1282`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1097`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1075`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0959`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0944`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0913`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.085`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0828`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.082`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0787`, n `668`, weak_sample_signal
