# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-26T22:52:25.407610+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0765` n `12`; crypto_alt avg `-0.0113` n `230`; crypto_major avg `0.0339` n `8`; equity avg `-0.016` n `100`; fx avg `-0.0005` n `6`; index avg `-0.0105` n `25`; metal avg `0.0028` n `20`; unknown avg `-0.0636` n `775`
- 1h: commodity avg `-0.2573` n `12`; crypto_alt avg `0.6347` n `230`; crypto_major avg `0.764` n `8`; equity avg `0.4111` n `100`; fx avg `0.0026` n `6`; index avg `0.1199` n `25`; metal avg `0.1679` n `20`; unknown avg `0.0189` n `775`
- 4h: commodity avg `-0.2703` n `12`; crypto_alt avg `0.8035` n `230`; crypto_major avg `0.9334` n `8`; equity avg `0.4117` n `100`; fx avg `0.0186` n `6`; index avg `0.0907` n `25`; metal avg `0.219` n `20`; unknown avg `-0.1324` n `775`
- 24h: commodity avg `-0.5405` n `12`; crypto_alt avg `1.5857` n `230`; crypto_major avg `1.874` n `8`; equity avg `1.0722` n `100`; fx avg `0.0511` n `6`; index avg `0.2042` n `25`; metal avg `0.4215` n `20`; unknown avg `0.0963` n `758`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1734`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1567`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1521`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1355`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1234`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1228`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1151`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1124`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.11`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.1098`, n `668`, weak_sample_signal
