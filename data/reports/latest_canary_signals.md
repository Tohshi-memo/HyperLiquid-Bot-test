# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-07T15:07:25.717776+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0569` n `12`; crypto_alt avg `-0.2439` n `232`; crypto_major avg `-0.2697` n `8`; equity avg `-0.0556` n `134`; fx avg `0.0125` n `6`; index avg `-0.0135` n `26`; metal avg `-0.0259` n `20`; unknown avg `0.3221` n `794`
- 1h: commodity avg `0.051` n `12`; crypto_alt avg `-0.1875` n `232`; crypto_major avg `-0.3398` n `8`; equity avg `0.0028` n `134`; fx avg `-0.0296` n `6`; index avg `-0.0138` n `26`; metal avg `0.0596` n `20`; unknown avg `-0.2557` n `794`
- 4h: commodity avg `0.1101` n `12`; crypto_alt avg `0.3414` n `232`; crypto_major avg `-0.3446` n `8`; equity avg `-0.009` n `134`; fx avg `-0.0267` n `6`; index avg `0.0204` n `26`; metal avg `0.1397` n `20`; unknown avg `6683.7767` n `748`
- 24h: commodity avg `0.2504` n `12`; crypto_alt avg `1.3975` n `232`; crypto_major avg `-0.4778` n `8`; equity avg `0.5361` n `134`; fx avg `-0.1016` n `6`; index avg `0.0681` n `26`; metal avg `0.0125` n `20`; unknown avg `-0.0819` n `680`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1234`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0975`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0919`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0909`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0905`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0899`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0889`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.087`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0853`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0844`, n `668`, weak_sample_signal
