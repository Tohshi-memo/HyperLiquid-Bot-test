# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-10T01:17:14.783174+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0152` n `12`; crypto_alt avg `-0.2444` n `233`; crypto_major avg `-0.2402` n `8`; equity avg `-0.0706` n `134`; fx avg `0.0038` n `6`; index avg `-0.017` n `26`; metal avg `-0.0361` n `20`; unknown avg `0.1928` n `797`
- 1h: commodity avg `0.0092` n `12`; crypto_alt avg `-0.0775` n `233`; crypto_major avg `-0.02` n `8`; equity avg `-0.3845` n `134`; fx avg `-0.0037` n `6`; index avg `-0.0998` n `26`; metal avg `0.0056` n `20`; unknown avg `8.1421` n `789`
- 4h: commodity avg `-0.065` n `12`; crypto_alt avg `-1.5345` n `233`; crypto_major avg `-0.662` n `8`; equity avg `-0.4718` n `134`; fx avg `-0.0199` n `6`; index avg `-0.0677` n `26`; metal avg `-0.002` n `20`; unknown avg `-0.1963` n `729`
- 24h: commodity avg `0.0372` n `12`; crypto_alt avg `-2.9737` n `233`; crypto_major avg `-2.038` n `8`; equity avg `-1.3294` n `134`; fx avg `-0.0256` n `6`; index avg `-0.2871` n `26`; metal avg `0.426` n `20`; unknown avg `0.8529` n `665`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1346`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1201`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1094`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1062`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1052`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1005`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0981`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0968`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0857`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0857`, n `668`, weak_sample_signal
