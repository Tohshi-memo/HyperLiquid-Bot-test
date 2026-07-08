# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-08T06:37:28.271973+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0149` n `12`; crypto_alt avg `-0.1123` n `229`; crypto_major avg `-0.0272` n `8`; equity avg `-0.1182` n `91`; fx avg `-0.0288` n `6`; index avg `-0.0342` n `25`; metal avg `-0.0081` n `20`; unknown avg `-0.0188` n `763`
- 1h: commodity avg `0.0295` n `12`; crypto_alt avg `-0.4271` n `229`; crypto_major avg `-0.4129` n `8`; equity avg `-0.0393` n `91`; fx avg `-0.0455` n `6`; index avg `-0.0255` n `25`; metal avg `-0.0031` n `20`; unknown avg `-0.2127` n `743`
- 4h: commodity avg `0.1303` n `12`; crypto_alt avg `-0.0445` n `229`; crypto_major avg `-0.2839` n `8`; equity avg `-0.3024` n `91`; fx avg `-0.1247` n `6`; index avg `-0.1967` n `25`; metal avg `0.2169` n `20`; unknown avg `-0.2213` n `743`
- 24h: commodity avg `0.861` n `12`; crypto_alt avg `-3.0677` n `229`; crypto_major avg `-2.6484` n `8`; equity avg `-1.749` n `91`; fx avg `-0.3029` n `6`; index avg `-0.3848` n `25`; metal avg `0.0936` n `20`; unknown avg `-0.6375` n `729`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1341`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0948`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0929`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0835`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0811`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0696`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0693`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0689`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0684`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0643`, n `668`, weak_sample_signal
