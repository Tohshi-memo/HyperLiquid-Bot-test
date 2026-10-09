# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-09T08:07:26.559793+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0004` n `13`; crypto_alt avg `0.0124` n `235`; crypto_major avg `0.0521` n `8`; equity avg `0.0217` n `150`; fx avg `0.0148` n `6`; index avg `-0.0007` n `26`; metal avg `0.0212` n `20`; unknown avg `1.5197` n `1006`
- 1h: commodity avg `-0.0695` n `13`; crypto_alt avg `0.1625` n `235`; crypto_major avg `0.1998` n `8`; equity avg `0.024` n `150`; fx avg `0.0499` n `6`; index avg `0.023` n `26`; metal avg `0.0459` n `20`; unknown avg `0.0802` n `1006`
- 4h: commodity avg `0.0034` n `13`; crypto_alt avg `0.64` n `235`; crypto_major avg `0.336` n `8`; equity avg `0.5398` n `150`; fx avg `0.0628` n `6`; index avg `0.0777` n `26`; metal avg `0.1643` n `20`; unknown avg `2.477` n `988`
- 24h: commodity avg `-0.2424` n `13`; crypto_alt avg `-1.0525` n `235`; crypto_major avg `-1.8963` n `8`; equity avg `-0.4468` n `150`; fx avg `0.1455` n `6`; index avg `0.0437` n `26`; metal avg `0.4825` n `20`; unknown avg `7.2165` n `949`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.1716`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.156`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1379`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1206`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1205`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1167`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1116`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1033`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1028`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0981`, n `668`, weak_sample_signal
