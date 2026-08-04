# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-04T00:52:27.078929+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.024` n `12`; crypto_alt avg `0.0155` n `230`; crypto_major avg `0.0498` n `8`; equity avg `0.097` n `107`; fx avg `-0.04` n `6`; index avg `-0.0143` n `25`; metal avg `-0.0292` n `20`; unknown avg `-0.0384` n `780`
- 1h: commodity avg `0.1015` n `12`; crypto_alt avg `-0.1826` n `230`; crypto_major avg `-0.1996` n `8`; equity avg `-0.8091` n `107`; fx avg `-0.0781` n `6`; index avg `-0.1751` n `25`; metal avg `-0.0033` n `20`; unknown avg `0.1288` n `780`
- 4h: commodity avg `0.1546` n `12`; crypto_alt avg `-0.384` n `230`; crypto_major avg `-0.6038` n `8`; equity avg `-0.3444` n `107`; fx avg `-0.0279` n `6`; index avg `-0.1003` n `25`; metal avg `-0.0154` n `20`; unknown avg `0.2145` n `780`
- 24h: commodity avg `0.0844` n `12`; crypto_alt avg `0.3241` n `230`; crypto_major avg `0.0954` n `8`; equity avg `1.2554` n `107`; fx avg `-0.0338` n `6`; index avg `0.11` n `25`; metal avg `-0.1503` n `20`; unknown avg `0.0967` n `763`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1423`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1091`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0989`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0967`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0906`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0864`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0862`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0836`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0819`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0814`, n `668`, weak_sample_signal
