# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-26T01:54:48.130997+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0414` n `12`; crypto_alt avg `-0.0492` n `231`; crypto_major avg `-0.1559` n `8`; equity avg `-0.0504` n `122`; fx avg `-0.0312` n `6`; index avg `0.0029` n `25`; metal avg `0.0943` n `20`; unknown avg `-0.0899` n `796`
- 1h: commodity avg `-0.0015` n `12`; crypto_alt avg `0.245` n `231`; crypto_major avg `0.2459` n `8`; equity avg `-0.0769` n `122`; fx avg `-0.0353` n `6`; index avg `0.0136` n `25`; metal avg `0.1526` n `20`; unknown avg `0.1124` n `796`
- 4h: commodity avg `-0.0584` n `12`; crypto_alt avg `0.8581` n `231`; crypto_major avg `0.4389` n `8`; equity avg `-0.638` n `122`; fx avg `-0.027` n `6`; index avg `-0.1268` n `25`; metal avg `0.0944` n `20`; unknown avg `0.0438` n `795`
- 24h: commodity avg `-0.8238` n `12`; crypto_alt avg `-2.0591` n `231`; crypto_major avg `-1.8334` n `8`; equity avg `1.1886` n `122`; fx avg `0.0007` n `6`; index avg `0.1262` n `25`; metal avg `-0.0337` n `20`; unknown avg `-0.3273` n `778`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1806`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1397`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.128`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1211`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1061`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0975`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0852`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0813`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0803`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0798`, n `668`, weak_sample_signal
