# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-08T01:52:25.177663+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0101` n `12`; crypto_alt avg `-0.0679` n `232`; crypto_major avg `-0.0277` n `8`; equity avg `0.0496` n `134`; fx avg `0.007` n `6`; index avg `0.0357` n `26`; metal avg `0.0335` n `20`; unknown avg `1.135` n `797`
- 1h: commodity avg `-0.0461` n `12`; crypto_alt avg `0.2466` n `232`; crypto_major avg `0.1209` n `8`; equity avg `0.0299` n `134`; fx avg `-0.0453` n `6`; index avg `0.0347` n `26`; metal avg `0.141` n `20`; unknown avg `0.9841` n `795`
- 4h: commodity avg `-0.078` n `12`; crypto_alt avg `0.66` n `232`; crypto_major avg `0.3448` n `8`; equity avg `0.2875` n `134`; fx avg `-0.1533` n `6`; index avg `0.0814` n `26`; metal avg `0.2272` n `20`; unknown avg `13.1535` n `788`
- 24h: commodity avg `0.1386` n `12`; crypto_alt avg `1.3163` n `232`; crypto_major avg `-0.4346` n `8`; equity avg `0.7324` n `134`; fx avg `-0.2465` n `6`; index avg `0.1612` n `26`; metal avg `0.309` n `20`; unknown avg `7765.1243` n `644`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1193`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0942`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0891`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0884`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.083`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0811`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0804`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0804`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0798`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0779`, n `668`, weak_sample_signal
