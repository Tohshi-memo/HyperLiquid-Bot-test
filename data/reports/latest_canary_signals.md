# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-20T07:52:24.999799+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0185` n `13`; crypto_alt avg `0.127` n `237`; crypto_major avg `0.0643` n `8`; equity avg `-0.0709` n `151`; fx avg `0.0002` n `6`; index avg `-0.006` n `26`; metal avg `-0.066` n `20`; unknown avg `0.0381` n `1198`
- 1h: commodity avg `0.1288` n `13`; crypto_alt avg `-0.1212` n `237`; crypto_major avg `-0.2092` n `8`; equity avg `-0.356` n `151`; fx avg `-0.021` n `6`; index avg `-0.077` n `26`; metal avg `-0.112` n `20`; unknown avg `0.5332` n `1196`
- 4h: commodity avg `0.0967` n `13`; crypto_alt avg `-0.6536` n `237`; crypto_major avg `-0.6099` n `8`; equity avg `-0.7215` n `151`; fx avg `-0.021` n `6`; index avg `-0.0867` n `26`; metal avg `-0.1374` n `20`; unknown avg `1.152` n `1168`
- 24h: commodity avg `0.4691` n `13`; crypto_alt avg `-0.3166` n `237`; crypto_major avg `-0.9361` n `8`; equity avg `-1.5945` n `151`; fx avg `0.0066` n `6`; index avg `-0.2281` n `26`; metal avg `-0.234` n `20`; unknown avg `4.9135` n `1013`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1831`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.139`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1159`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0937`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0932`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0887`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0838`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0704`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0704`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0684`, n `668`, weak_sample_signal
