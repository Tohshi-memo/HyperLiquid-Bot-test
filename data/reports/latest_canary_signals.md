# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-30T07:07:32.140028+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0042` n `12`; crypto_alt avg `-0.1202` n `228`; crypto_major avg `-0.0424` n `8`; equity avg `0.0698` n `88`; fx avg `0.0062` n `6`; index avg `0.0345` n `23`; metal avg `-0.0296` n `20`; unknown avg `-0.016` n `765`
- 1h: commodity avg `0.1011` n `12`; crypto_alt avg `-0.0704` n `228`; crypto_major avg `-0.0284` n `8`; equity avg `-0.0699` n `88`; fx avg `0.0365` n `6`; index avg `-0.019` n `23`; metal avg `0.5653` n `20`; unknown avg `-0.318` n `765`
- 4h: commodity avg `-0.032` n `12`; crypto_alt avg `-0.2781` n `228`; crypto_major avg `-0.4211` n `8`; equity avg `0.1757` n `88`; fx avg `0.0356` n `6`; index avg `0.0537` n `23`; metal avg `0.6641` n `20`; unknown avg `7.7178` n `737`
- 24h: commodity avg `-0.1445` n `12`; crypto_alt avg `-0.2701` n `228`; crypto_major avg `0.7899` n `8`; equity avg `1.876` n `88`; fx avg `0.1536` n `6`; index avg `0.2453` n `23`; metal avg `-0.0387` n `20`; unknown avg `9.2646` n `734`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1204`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0975`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0941`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0867`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0851`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0765`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0672`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0657`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0649`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0641`, n `668`, weak_sample_signal
