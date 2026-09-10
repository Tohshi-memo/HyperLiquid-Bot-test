# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-10T11:37:35.063917+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0267` n `12`; crypto_alt avg `0.1945` n `233`; crypto_major avg `0.0896` n `8`; equity avg `0.0793` n `134`; fx avg `0.0023` n `6`; index avg `0.0208` n `26`; metal avg `0.0629` n `20`; unknown avg `0.0869` n `797`
- 1h: commodity avg `0.0222` n `12`; crypto_alt avg `0.4032` n `233`; crypto_major avg `0.1093` n `8`; equity avg `-0.0854` n `134`; fx avg `0.018` n `6`; index avg `-0.0286` n `26`; metal avg `-0.1045` n `20`; unknown avg `0.1317` n `795`
- 4h: commodity avg `0.1114` n `12`; crypto_alt avg `0.2203` n `233`; crypto_major avg `0.1973` n `8`; equity avg `-0.3459` n `134`; fx avg `0.0609` n `6`; index avg `-0.0717` n `26`; metal avg `-0.5079` n `20`; unknown avg `0.416` n `789`
- 24h: commodity avg `-0.1253` n `12`; crypto_alt avg `-3.9409` n `233`; crypto_major avg `-2.57` n `8`; equity avg `-0.863` n `134`; fx avg `0.1069` n `6`; index avg `-0.0367` n `26`; metal avg `-0.3172` n `20`; unknown avg `-0.574` n `668`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1297`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.12`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.114`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1045`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0997`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0979`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0922`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0916`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0867`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0857`, n `668`, weak_sample_signal
