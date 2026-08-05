# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-05T13:07:35.789404+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1576` n `12`; crypto_alt avg `-0.0268` n `230`; crypto_major avg `-0.104` n `8`; equity avg `-0.1078` n `108`; fx avg `-0.0046` n `6`; index avg `0.0233` n `25`; metal avg `-0.0039` n `20`; unknown avg `-0.0286` n `782`
- 1h: commodity avg `-0.0588` n `12`; crypto_alt avg `0.1084` n `230`; crypto_major avg `0.1618` n `8`; equity avg `0.1371` n `108`; fx avg `-0.0076` n `6`; index avg `0.0545` n `25`; metal avg `-0.2158` n `20`; unknown avg `0.0183` n `782`
- 4h: commodity avg `-0.0922` n `12`; crypto_alt avg `-0.0106` n `230`; crypto_major avg `-0.1372` n `8`; equity avg `0.028` n `108`; fx avg `-0.0076` n `6`; index avg `0.0913` n `25`; metal avg `-0.0323` n `20`; unknown avg `0.65` n `781`
- 24h: commodity avg `-0.4411` n `12`; crypto_alt avg `0.6736` n `230`; crypto_major avg `0.2739` n `8`; equity avg `1.8837` n `108`; fx avg `0.0487` n `6`; index avg `0.5582` n `25`; metal avg `0.7438` n `20`; unknown avg `0.002` n `748`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1364`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1148`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1065`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1003`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0998`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0953`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0917`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.089`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0857`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0841`, n `668`, weak_sample_signal
