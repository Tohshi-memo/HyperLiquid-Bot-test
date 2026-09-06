# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-06T19:07:26.348864+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0014` n `12`; crypto_alt avg `-0.0568` n `232`; crypto_major avg `-0.0509` n `8`; equity avg `0.0309` n `134`; fx avg `0.0109` n `6`; index avg `0.0036` n `26`; metal avg `0.0114` n `20`; unknown avg `148.4459` n `775`
- 1h: commodity avg `-0.0075` n `12`; crypto_alt avg `-0.0671` n `232`; crypto_major avg `-0.0751` n `8`; equity avg `0.0683` n `134`; fx avg `0.0084` n `6`; index avg `0.0089` n `26`; metal avg `0.0045` n `20`; unknown avg `0.5099` n `769`
- 4h: commodity avg `-0.0172` n `12`; crypto_alt avg `0.694` n `232`; crypto_major avg `0.2454` n `8`; equity avg `0.2636` n `134`; fx avg `-0.0015` n `6`; index avg `0.0446` n `26`; metal avg `0.0162` n `20`; unknown avg `0.5323` n `754`
- 24h: commodity avg `0.056` n `12`; crypto_alt avg `1.1061` n `232`; crypto_major avg `-0.2596` n `8`; equity avg `0.3456` n `134`; fx avg `-0.0119` n `6`; index avg `0.0005` n `26`; metal avg `-0.0264` n `20`; unknown avg `72.6317` n `676`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1596`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1321`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1233`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1154`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1142`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1094`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1045`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0994`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.098`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0966`, n `668`, weak_sample_signal
