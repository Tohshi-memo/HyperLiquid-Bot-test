# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-05T13:52:24.191367+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0129` n `12`; crypto_alt avg `-0.1467` n `232`; crypto_major avg `-0.311` n `8`; equity avg `-0.0502` n `134`; fx avg `0.0005` n `6`; index avg `-0.0021` n `26`; metal avg `-0.0048` n `20`; unknown avg `0.0711` n `752`
- 1h: commodity avg `0.0459` n `12`; crypto_alt avg `-0.339` n `232`; crypto_major avg `-0.2041` n `8`; equity avg `-0.0381` n `134`; fx avg `0.0064` n `6`; index avg `-0.0129` n `26`; metal avg `-0.0006` n `20`; unknown avg `18.2089` n `740`
- 4h: commodity avg `0.079` n `12`; crypto_alt avg `0.0121` n `232`; crypto_major avg `0.433` n `8`; equity avg `0.0249` n `134`; fx avg `0.0134` n `6`; index avg `0.0193` n `26`; metal avg `-0.0046` n `20`; unknown avg `-0.2031` n `732`
- 24h: commodity avg `0.4852` n `12`; crypto_alt avg `1.9367` n `232`; crypto_major avg `1.0102` n `8`; equity avg `0.7068` n `134`; fx avg `0.0447` n `6`; index avg `0.0287` n `26`; metal avg `0.0417` n `20`; unknown avg `0.1533` n `656`

## Correlations

- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.167`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1538`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1324`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.121`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1165`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1133`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1113`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.106`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0956`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0932`, n `668`, weak_sample_signal
