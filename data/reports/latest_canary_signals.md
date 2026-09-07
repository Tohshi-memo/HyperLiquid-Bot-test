# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-07T23:52:24.536895+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0249` n `12`; crypto_alt avg `0.2666` n `232`; crypto_major avg `0.1771` n `8`; equity avg `0.0583` n `134`; fx avg `-0.0137` n `6`; index avg `0.0153` n `26`; metal avg `0.0317` n `20`; unknown avg `0.4279` n `797`
- 1h: commodity avg `-0.0179` n `12`; crypto_alt avg `0.63` n `232`; crypto_major avg `0.3564` n `8`; equity avg `0.087` n `134`; fx avg `-0.0323` n `6`; index avg `0.0033` n `26`; metal avg `0.1087` n `20`; unknown avg `0.8952` n `795`
- 4h: commodity avg `0.0042` n `12`; crypto_alt avg `-0.142` n `232`; crypto_major avg `-0.2008` n `8`; equity avg `-0.087` n `134`; fx avg `-0.0464` n `6`; index avg `-0.0376` n `26`; metal avg `0.0933` n `20`; unknown avg `7.5297` n `752`
- 24h: commodity avg `0.1981` n `12`; crypto_alt avg `-0.375` n `232`; crypto_major avg `-1.4888` n `8`; equity avg `0.4475` n `134`; fx avg `-0.222` n `6`; index avg `0.062` n `26`; metal avg `0.1756` n `20`; unknown avg `7769.1065` n `644`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1295`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0952`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0941`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0939`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0939`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0928`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0883`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.088`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0815`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0812`, n `668`, weak_sample_signal
