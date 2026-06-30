# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-30T06:52:34.529811+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0827` n `12`; crypto_alt avg `-0.068` n `228`; crypto_major avg `-0.0244` n `8`; equity avg `0.0415` n `88`; fx avg `0.0021` n `6`; index avg `-0.0144` n `23`; metal avg `-0.0066` n `20`; unknown avg `-0.0048` n `765`
- 1h: commodity avg `0.0662` n `12`; crypto_alt avg `0.1378` n `228`; crypto_major avg `-0.0099` n `8`; equity avg `-0.18` n `88`; fx avg `0.0393` n `6`; index avg `-0.0721` n `23`; metal avg `0.6564` n `20`; unknown avg `-0.3497` n `739`
- 4h: commodity avg `-0.0131` n `12`; crypto_alt avg `-0.1199` n `228`; crypto_major avg `-0.404` n `8`; equity avg `0.0929` n `88`; fx avg `0.0222` n `6`; index avg `0.0279` n `23`; metal avg `0.7011` n `20`; unknown avg `7.8706` n `737`
- 24h: commodity avg `-0.2112` n `12`; crypto_alt avg `-0.2362` n `228`; crypto_major avg `0.6908` n `8`; equity avg `1.6453` n `88`; fx avg `0.1513` n `6`; index avg `0.1858` n `23`; metal avg `-0.1262` n `20`; unknown avg `9.1812` n `734`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1207`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0979`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0948`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0874`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0862`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0754`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0683`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0682`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0649`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0645`, n `668`, weak_sample_signal
