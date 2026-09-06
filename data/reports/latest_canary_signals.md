# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-06T04:22:26.681083+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0117` n `12`; crypto_alt avg `-0.4452` n `232`; crypto_major avg `-0.1246` n `8`; equity avg `-0.0131` n `134`; fx avg `0.0101` n `6`; index avg `0.0009` n `26`; metal avg `-0.0061` n `20`; unknown avg `0.3907` n `792`
- 1h: commodity avg `0.0084` n `12`; crypto_alt avg `-0.2549` n `232`; crypto_major avg `0.0901` n `8`; equity avg `-0.0132` n `134`; fx avg `0.0033` n `6`; index avg `0.0029` n `26`; metal avg `0.0047` n `20`; unknown avg `0.3405` n `758`
- 4h: commodity avg `0.0302` n `12`; crypto_alt avg `0.1913` n `232`; crypto_major avg `0.5268` n `8`; equity avg `0.076` n `134`; fx avg `0.0076` n `6`; index avg `0.0124` n `26`; metal avg `-0.0091` n `20`; unknown avg `3.3099` n `752`
- 24h: commodity avg `0.1159` n `12`; crypto_alt avg `2.7301` n `232`; crypto_major avg `2.8984` n `8`; equity avg `0.5047` n `134`; fx avg `-0.0624` n `6`; index avg `0.1279` n `26`; metal avg `0.0279` n `20`; unknown avg `1.0209` n `680`

## Correlations

- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1583`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1511`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.133`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1188`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1081`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0968`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0954`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0935`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0892`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0821`, n `668`, weak_sample_signal
