# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-01T02:07:27.784848+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0076` n `12`; crypto_alt avg `-0.2801` n `232`; crypto_major avg `-0.1382` n `8`; equity avg `-0.0104` n `130`; fx avg `-0.0136` n `6`; index avg `-0.0149` n `26`; metal avg `0.03` n `20`; unknown avg `0.1416` n `790`
- 1h: commodity avg `-0.0471` n `12`; crypto_alt avg `-0.2115` n `232`; crypto_major avg `-0.2835` n `8`; equity avg `-0.0564` n `130`; fx avg `-0.0033` n `6`; index avg `-0.0218` n `26`; metal avg `-0.0586` n `20`; unknown avg `0.8816` n `790`
- 4h: commodity avg `0.0438` n `12`; crypto_alt avg `0.1815` n `232`; crypto_major avg `-0.5812` n `8`; equity avg `0.024` n `130`; fx avg `0.0148` n `6`; index avg `0.0389` n `26`; metal avg `0.0243` n `20`; unknown avg `1.513` n `790`
- 24h: commodity avg `0.2768` n `12`; crypto_alt avg `2.0368` n `231`; crypto_major avg `1.5672` n `8`; equity avg `1.3134` n `130`; fx avg `-0.0352` n `6`; index avg `0.1757` n `26`; metal avg `0.019` n `20`; unknown avg `0.2622` n `751`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.1009`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0989`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0963`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0957`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0872`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0578`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0567`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0542`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0524`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0479`, n `668`, weak_sample_signal
