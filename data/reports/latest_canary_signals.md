# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-02T17:07:23.373016+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0469` n `12`; crypto_alt avg `-0.0291` n `230`; crypto_major avg `-0.0615` n `8`; equity avg `0.1042` n `102`; fx avg `0.0063` n `6`; index avg `0.0126` n `25`; metal avg `0.0006` n `20`; unknown avg `1.1518` n `782`
- 1h: commodity avg `-0.0762` n `12`; crypto_alt avg `0.0814` n `230`; crypto_major avg `0.3404` n `8`; equity avg `0.2632` n `102`; fx avg `0.0122` n `6`; index avg `0.0413` n `25`; metal avg `0.0386` n `20`; unknown avg `1.656` n `782`
- 4h: commodity avg `-0.1306` n `12`; crypto_alt avg `0.0232` n `230`; crypto_major avg `0.454` n `8`; equity avg `0.3361` n `102`; fx avg `-0.0368` n `6`; index avg `0.0662` n `25`; metal avg `0.063` n `20`; unknown avg `1.2522` n `782`
- 24h: commodity avg `-1.2427` n `12`; crypto_alt avg `0.2925` n `230`; crypto_major avg `0.4326` n `8`; equity avg `1.2667` n `102`; fx avg `-0.1407` n `6`; index avg `0.2786` n `25`; metal avg `0.2994` n `20`; unknown avg `1.4376` n `766`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1259`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1196`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1119`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0901`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0826`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0805`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0779`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0729`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0727`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0706`, n `668`, weak_sample_signal
