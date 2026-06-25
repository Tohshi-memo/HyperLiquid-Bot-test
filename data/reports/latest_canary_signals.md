# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-25T17:52:41.814678+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0513` n `12`; crypto_alt avg `-0.1729` n `228`; crypto_major avg `-0.2808` n `8`; equity avg `-0.1278` n `86`; fx avg `0.0031` n `6`; index avg `-0.01` n `23`; metal avg `-0.0458` n `20`; unknown avg `-0.1426` n `765`
- 1h: commodity avg `0.0694` n `12`; crypto_alt avg `0.7` n `228`; crypto_major avg `0.98` n `8`; equity avg `-0.0312` n `86`; fx avg `0.0028` n `6`; index avg `0.0094` n `23`; metal avg `-0.0416` n `20`; unknown avg `0.3009` n `765`
- 4h: commodity avg `0.2852` n `12`; crypto_alt avg `1.3547` n `228`; crypto_major avg `1.2759` n `8`; equity avg `0.2663` n `86`; fx avg `0.0573` n `6`; index avg `0.072` n `23`; metal avg `0.3733` n `20`; unknown avg `1.2135` n `765`
- 24h: commodity avg `0.3678` n `12`; crypto_alt avg `1.5645` n `228`; crypto_major avg `1.365` n `8`; equity avg `0.3348` n `86`; fx avg `0.0709` n `6`; index avg `0.4837` n `23`; metal avg `0.7122` n `20`; unknown avg `0.5451` n `700`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1626`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1118`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1031`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0861`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0842`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0793`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0757`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0697`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0659`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0611`, n `668`, weak_sample_signal
