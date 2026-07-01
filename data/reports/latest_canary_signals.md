# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-01T06:07:28.899126+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.027` n `12`; crypto_alt avg `-0.1843` n `228`; crypto_major avg `-0.2161` n `8`; equity avg `-0.0767` n `88`; fx avg `0.0241` n `6`; index avg `-0.0154` n `23`; metal avg `-0.1174` n `20`; unknown avg `0.1248` n `745`
- 1h: commodity avg `-0.1042` n `12`; crypto_alt avg `-0.5795` n `228`; crypto_major avg `-0.5855` n `8`; equity avg `-0.1846` n `88`; fx avg `-0.0043` n `6`; index avg `-0.0627` n `23`; metal avg `-0.0924` n `20`; unknown avg `-0.3815` n `745`
- 4h: commodity avg `-0.0447` n `12`; crypto_alt avg `1.1313` n `228`; crypto_major avg `0.6903` n `8`; equity avg `0.4088` n `88`; fx avg `-0.0539` n `6`; index avg `0.0897` n `23`; metal avg `-0.0749` n `20`; unknown avg `0.3771` n `745`
- 24h: commodity avg `0.0606` n `12`; crypto_alt avg `-0.4644` n `228`; crypto_major avg `-0.2356` n `8`; equity avg `0.3617` n `88`; fx avg `0.1204` n `6`; index avg `-0.0603` n `23`; metal avg `-0.3247` n `20`; unknown avg `-0.4811` n `745`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1232`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1128`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1009`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0879`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0878`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0791`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.078`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0757`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0688`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0631`, n `668`, weak_sample_signal
