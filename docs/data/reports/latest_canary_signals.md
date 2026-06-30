# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-30T23:22:26.837035+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.024` n `12`; crypto_alt avg `-0.0225` n `228`; crypto_major avg `-0.0023` n `8`; equity avg `0.054` n `88`; fx avg `-0.012` n `6`; index avg `0.0017` n `23`; metal avg `-0.0891` n `20`; unknown avg `-0.4306` n `765`
- 1h: commodity avg `0.0378` n `12`; crypto_alt avg `-0.2664` n `228`; crypto_major avg `-0.199` n `8`; equity avg `0.0608` n `88`; fx avg `-0.0128` n `6`; index avg `-0.0077` n `23`; metal avg `-0.0683` n `20`; unknown avg `-0.5712` n `765`
- 4h: commodity avg `0.0115` n `12`; crypto_alt avg `-0.3397` n `228`; crypto_major avg `-0.1715` n `8`; equity avg `0.2891` n `88`; fx avg `-0.0096` n `6`; index avg `-0.0464` n `23`; metal avg `-0.2491` n `20`; unknown avg `1.0247` n `763`
- 24h: commodity avg `0.1762` n `12`; crypto_alt avg `-2.0933` n `228`; crypto_major avg `-2.1755` n `8`; equity avg `1.2643` n `88`; fx avg `0.0913` n `6`; index avg `0.2456` n `23`; metal avg `-0.1568` n `20`; unknown avg `7.358` n `735`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1133`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.099`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0923`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0846`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0766`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0738`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0709`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0706`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0541`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0502`, n `668`, weak_sample_signal
