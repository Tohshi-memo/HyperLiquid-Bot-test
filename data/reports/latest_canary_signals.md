# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-07T20:22:26.771522+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0109` n `12`; crypto_alt avg `0.1225` n `232`; crypto_major avg `-0.0187` n `8`; equity avg `-0.029` n `134`; fx avg `-0.0011` n `6`; index avg `0.0033` n `26`; metal avg `0.0128` n `20`; unknown avg `-0.3871` n `780`
- 1h: commodity avg `0.0163` n `12`; crypto_alt avg `0.1557` n `232`; crypto_major avg `0.0023` n `8`; equity avg `0.0227` n `134`; fx avg `0.0014` n `6`; index avg `0.0065` n `26`; metal avg `0.0136` n `20`; unknown avg `-0.2717` n `762`
- 4h: commodity avg `0.0259` n `12`; crypto_alt avg `0.5972` n `232`; crypto_major avg `0.3958` n `8`; equity avg `0.2542` n `134`; fx avg `-0.0169` n `6`; index avg `0.0479` n `26`; metal avg `0.0055` n `20`; unknown avg `-0.4199` n `738`
- 24h: commodity avg `0.1951` n `12`; crypto_alt avg `0.2363` n `232`; crypto_major avg `-0.9027` n `8`; equity avg `0.4148` n `134`; fx avg `-0.1276` n `6`; index avg `0.0861` n `26`; metal avg `0.0053` n `20`; unknown avg `7956.4672` n `641`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1254`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0943`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0928`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0917`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0881`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0878`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0867`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.085`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0831`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0806`, n `668`, weak_sample_signal
