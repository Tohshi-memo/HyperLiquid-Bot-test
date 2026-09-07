# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-07T13:07:27.586247+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1105` n `12`; crypto_alt avg `0.1094` n `232`; crypto_major avg `0.0311` n `8`; equity avg `0.0297` n `134`; fx avg `0.002` n `6`; index avg `0.0132` n `26`; metal avg `-0.0038` n `20`; unknown avg `0.2134` n `794`
- 1h: commodity avg `0.1099` n `12`; crypto_alt avg `0.6796` n `232`; crypto_major avg `0.3485` n `8`; equity avg `-0.0032` n `134`; fx avg `-0.0186` n `6`; index avg `0.0157` n `26`; metal avg `0.0414` n `20`; unknown avg `6614.2523` n `756`
- 4h: commodity avg `0.3234` n `12`; crypto_alt avg `1.2678` n `232`; crypto_major avg `0.665` n `8`; equity avg `-0.0969` n `134`; fx avg `0.0697` n `6`; index avg `-0.0408` n `26`; metal avg `-0.089` n `20`; unknown avg `6719.9765` n `744`
- 24h: commodity avg `0.2697` n `12`; crypto_alt avg `1.0401` n `232`; crypto_major avg `-0.4304` n `8`; equity avg `0.2197` n `134`; fx avg `-0.0936` n `6`; index avg `0.0116` n `26`; metal avg `-0.1474` n `20`; unknown avg `159.0211` n `632`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1233`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.102`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0992`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0929`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0894`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0864`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0858`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.081`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0801`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0762`, n `668`, weak_sample_signal
