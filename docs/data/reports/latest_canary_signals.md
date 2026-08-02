# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-02T06:22:25.880759+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0474` n `12`; crypto_alt avg `-0.0511` n `230`; crypto_major avg `-0.0824` n `8`; equity avg `-0.0208` n `102`; fx avg `-0.0009` n `6`; index avg `0.012` n `25`; metal avg `0.0058` n `20`; unknown avg `0.0658` n `782`
- 1h: commodity avg `-0.056` n `12`; crypto_alt avg `0.0416` n `230`; crypto_major avg `-0.1348` n `8`; equity avg `0.033` n `102`; fx avg `0.0016` n `6`; index avg `0.0185` n `25`; metal avg `0.0056` n `20`; unknown avg `0.0611` n `766`
- 4h: commodity avg `-0.2571` n `12`; crypto_alt avg `0.1981` n `230`; crypto_major avg `0.1663` n `8`; equity avg `-0.0743` n `102`; fx avg `-0.0538` n `6`; index avg `0.0835` n `25`; metal avg `0.1135` n `20`; unknown avg `0.3837` n `766`
- 24h: commodity avg `-1.0953` n `12`; crypto_alt avg `0.235` n `230`; crypto_major avg `0.334` n `8`; equity avg `0.7819` n `102`; fx avg `-0.1165` n `6`; index avg `0.2618` n `25`; metal avg `0.2581` n `20`; unknown avg `0.3638` n `765`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1337`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1234`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1011`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0926`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.091`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0765`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0714`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0707`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0689`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0685`, n `668`, weak_sample_signal
