# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-16T22:37:33.747765+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0013` n `12`; crypto_alt avg `0.0603` n `234`; crypto_major avg `0.0342` n `8`; equity avg `0.1373` n `137`; fx avg `-0.0008` n `6`; index avg `0.0388` n `27`; metal avg `0.0606` n `20`; unknown avg `0.8647` n `887`
- 1h: commodity avg `-0.0296` n `12`; crypto_alt avg `-0.3276` n `234`; crypto_major avg `-0.3389` n `8`; equity avg `0.2048` n `137`; fx avg `0.0127` n `6`; index avg `0.0615` n `27`; metal avg `0.0279` n `20`; unknown avg `0.76` n `829`
- 4h: commodity avg `-0.0254` n `12`; crypto_alt avg `1.2221` n `234`; crypto_major avg `0.5554` n `8`; equity avg `0.4347` n `137`; fx avg `0.0558` n `6`; index avg `0.0293` n `27`; metal avg `-0.035` n `20`; unknown avg `-0.2344` n `753`
- 24h: commodity avg `-0.5891` n `12`; crypto_alt avg `0.1764` n `234`; crypto_major avg `0.4135` n `8`; equity avg `1.1952` n `137`; fx avg `0.0712` n `6`; index avg `0.0833` n `27`; metal avg `-0.2914` n `20`; unknown avg `-0.5953` n `723`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1176`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1156`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0988`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0973`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0973`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0915`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.085`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0794`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0789`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.066`, n `668`, weak_sample_signal
