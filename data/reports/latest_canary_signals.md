# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-07T06:07:26.050280+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0161` n `12`; crypto_alt avg `-0.1086` n `232`; crypto_major avg `-0.0593` n `8`; equity avg `0.019` n `134`; fx avg `-0.0188` n `6`; index avg `-0.0083` n `26`; metal avg `-0.0617` n `20`; unknown avg `-0.1901` n `776`
- 1h: commodity avg `0.0847` n `12`; crypto_alt avg `-0.1193` n `232`; crypto_major avg `0.1408` n `8`; equity avg `0.0311` n `134`; fx avg `-0.0374` n `6`; index avg `0.0096` n `26`; metal avg `-0.0528` n `20`; unknown avg `-0.2053` n `776`
- 4h: commodity avg `0.1716` n `12`; crypto_alt avg `0.4334` n `232`; crypto_major avg `0.1967` n `8`; equity avg `0.2163` n `134`; fx avg `-0.0188` n `6`; index avg `-0.004` n `26`; metal avg `-0.1019` n `20`; unknown avg `-0.013` n `742`
- 24h: commodity avg `0.1512` n `12`; crypto_alt avg `0.1039` n `232`; crypto_major avg `-0.6549` n `8`; equity avg `0.4356` n `134`; fx avg `-0.019` n `6`; index avg `-0.0009` n `26`; metal avg `-0.2429` n `20`; unknown avg `377.0061` n `658`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.193`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1289`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1104`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1061`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0979`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0963`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0922`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0825`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0783`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0693`, n `668`, weak_sample_signal
