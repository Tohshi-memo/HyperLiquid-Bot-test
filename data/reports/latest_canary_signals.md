# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-29T04:22:35.386571+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.001` n `12`; crypto_alt avg `-0.2027` n `228`; crypto_major avg `-0.3128` n `8`; equity avg `-0.14` n `88`; fx avg `-0.0012` n `6`; index avg `-0.0569` n `23`; metal avg `-0.0631` n `20`; unknown avg `-0.13` n `764`
- 1h: commodity avg `0.0091` n `12`; crypto_alt avg `-0.5011` n `228`; crypto_major avg `-0.5528` n `8`; equity avg `-0.1068` n `88`; fx avg `0.0097` n `6`; index avg `-0.0298` n `23`; metal avg `-0.2516` n `20`; unknown avg `-0.3357` n `764`
- 4h: commodity avg `0.1327` n `12`; crypto_alt avg `1.1586` n `228`; crypto_major avg `0.9168` n `8`; equity avg `0.0879` n `88`; fx avg `0.0698` n `6`; index avg `-0.0076` n `23`; metal avg `0.1402` n `20`; unknown avg `0.0487` n `764`
- 24h: commodity avg `-0.2247` n `12`; crypto_alt avg `-0.027` n `228`; crypto_major avg `-0.1709` n `8`; equity avg `-0.0755` n `88`; fx avg `0.0513` n `6`; index avg `-0.0832` n `23`; metal avg `-0.2214` n `20`; unknown avg `-0.5984` n `722`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.205`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1835`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1279`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1255`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.107`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.104`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0997`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0992`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0985`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.093`, n `668`, weak_sample_signal
