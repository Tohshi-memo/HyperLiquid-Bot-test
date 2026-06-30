# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-30T10:37:25.482946+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0242` n `12`; crypto_alt avg `-0.0367` n `228`; crypto_major avg `-0.1348` n `8`; equity avg `-0.0415` n `88`; fx avg `0.014` n `6`; index avg `-0.0045` n `23`; metal avg `0.0271` n `20`; unknown avg `-0.2664` n `765`
- 1h: commodity avg `0.0308` n `12`; crypto_alt avg `0.0056` n `228`; crypto_major avg `-0.0896` n `8`; equity avg `0.0861` n `88`; fx avg `0.0212` n `6`; index avg `0.0194` n `23`; metal avg `0.2074` n `20`; unknown avg `0.0244` n `765`
- 4h: commodity avg `0.2965` n `12`; crypto_alt avg `-0.6806` n `228`; crypto_major avg `-0.5204` n `8`; equity avg `-0.1372` n `88`; fx avg `0.0278` n `6`; index avg `-0.0521` n `23`; metal avg `0.0047` n `20`; unknown avg `-0.0049` n `765`
- 24h: commodity avg `0.1369` n `12`; crypto_alt avg `-0.9446` n `228`; crypto_major avg `-0.1535` n `8`; equity avg `1.2081` n `88`; fx avg `0.1433` n `6`; index avg `0.0909` n `23`; metal avg `0.3082` n `20`; unknown avg `9.1723` n `734`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1204`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0883`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0867`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0817`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.079`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.068`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0586`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0567`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0562`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0551`, n `668`, weak_sample_signal
