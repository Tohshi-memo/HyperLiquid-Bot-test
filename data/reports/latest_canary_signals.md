# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-03T04:22:33.407234+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0047` n `12`; crypto_alt avg `0.0899` n `230`; crypto_major avg `0.0951` n `8`; equity avg `0.0849` n `102`; fx avg `0.025` n `6`; index avg `0.035` n `25`; metal avg `0.0142` n `20`; unknown avg `-0.062` n `784`
- 1h: commodity avg `-0.0302` n `12`; crypto_alt avg `0.0484` n `230`; crypto_major avg `0.0097` n `8`; equity avg `0.1388` n `102`; fx avg `-0.0074` n `6`; index avg `0.0357` n `25`; metal avg `0.0546` n `20`; unknown avg `0.2934` n `784`
- 4h: commodity avg `-0.1341` n `12`; crypto_alt avg `-0.5073` n `230`; crypto_major avg `-0.5268` n `8`; equity avg `0.2523` n `102`; fx avg `-0.209` n `6`; index avg `0.0659` n `25`; metal avg `0.0173` n `20`; unknown avg `-0.0317` n `784`
- 24h: commodity avg `-0.1958` n `12`; crypto_alt avg `-0.6569` n `230`; crypto_major avg `-0.5082` n `8`; equity avg `0.9333` n `102`; fx avg `-0.2085` n `6`; index avg `0.0402` n `25`; metal avg `-0.0472` n `20`; unknown avg `1.2752` n `766`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1263`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1111`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0985`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0822`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0777`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0706`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0669`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0614`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0591`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.058`, n `668`, weak_sample_signal
