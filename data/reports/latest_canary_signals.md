# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-16T00:37:32.364379+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0286` n `12`; crypto_alt avg `0.0936` n `228`; crypto_major avg `0.0065` n `8`; equity avg `0.0298` n `77`; fx avg `-0.0305` n `6`; index avg `0.0068` n `23`; metal avg `0.0866` n `18`; unknown avg `0.5734` n `687`
- 1h: commodity avg `-0.0517` n `12`; crypto_alt avg `0.6902` n `228`; crypto_major avg `0.3773` n `8`; equity avg `-0.1389` n `77`; fx avg `0.0053` n `6`; index avg `0.0456` n `23`; metal avg `-0.1805` n `18`; unknown avg `1.2997` n `687`
- 4h: commodity avg `-0.014` n `12`; crypto_alt avg `-0.2918` n `228`; crypto_major avg `-0.9904` n `8`; equity avg `-0.343` n `77`; fx avg `-0.0123` n `6`; index avg `-0.0712` n `23`; metal avg `-0.1373` n `18`; unknown avg `0.2504` n `679`
- 24h: commodity avg `0.6715` n `12`; crypto_alt avg `1.3929` n `228`; crypto_major avg `2.2425` n `8`; equity avg `1.1812` n `76`; fx avg `0.0147` n `6`; index avg `0.5579` n `23`; metal avg `-0.2928` n `18`; unknown avg `1.7536` n `519`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1003`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0826`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0731`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.0711`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.065`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.061`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0569`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0566`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0566`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0439`, n `668`, weak_sample_signal
