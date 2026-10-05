# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-05T03:22:30.677553+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.76` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0036` n `13`; crypto_alt avg `-0.3326` n `235`; crypto_major avg `-0.2706` n `8`; equity avg `0.0733` n `144`; fx avg `0.0188` n `6`; index avg `0.0173` n `26`; metal avg `0.0333` n `20`; unknown avg `0.2182` n `1066`
- 1h: commodity avg `-0.0133` n `13`; crypto_alt avg `-0.5177` n `235`; crypto_major avg `-0.568` n `8`; equity avg `-0.1493` n `144`; fx avg `-0.052` n `6`; index avg `-0.0476` n `26`; metal avg `-0.1175` n `20`; unknown avg `0.4806` n `1064`
- 4h: commodity avg `-0.1349` n `13`; crypto_alt avg `-0.0387` n `235`; crypto_major avg `-0.2928` n `8`; equity avg `0.047` n `144`; fx avg `-0.1012` n `6`; index avg `-0.0221` n `26`; metal avg `0.0057` n `20`; unknown avg `4.8672` n `1026`
- 24h: commodity avg `-0.3173` n `13`; crypto_alt avg `0.9629` n `235`; crypto_major avg `1.3382` n `8`; equity avg `0.42` n `144`; fx avg `-0.0999` n `6`; index avg `-0.0107` n `26`; metal avg `0.0708` n `20`; unknown avg `0.8638` n `938`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1826`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1615`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1496`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1454`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1332`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1111`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0921`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0897`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0859`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0792`, n `668`, weak_sample_signal
