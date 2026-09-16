# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-16T15:37:31.436306+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.53` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0957` n `12`; crypto_alt avg `-0.1175` n `234`; crypto_major avg `-0.0712` n `8`; equity avg `-0.082` n `137`; fx avg `0.0016` n `6`; index avg `-0.0262` n `27`; metal avg `-0.0275` n `20`; unknown avg `0.6877` n `917`
- 1h: commodity avg `-0.1806` n `12`; crypto_alt avg `-0.0791` n `234`; crypto_major avg `0.0407` n `8`; equity avg `0.186` n `137`; fx avg `-0.0395` n `6`; index avg `0.0496` n `27`; metal avg `0.0558` n `20`; unknown avg `1.8928` n `915`
- 4h: commodity avg `-0.2796` n `12`; crypto_alt avg `-1.0956` n `234`; crypto_major avg `-0.7857` n `8`; equity avg `0.4152` n `137`; fx avg `0.0132` n `6`; index avg `0.0611` n `27`; metal avg `-0.0461` n `20`; unknown avg `2.1451` n `897`
- 24h: commodity avg `-0.4566` n `12`; crypto_alt avg `-2.8828` n `234`; crypto_major avg `-1.9844` n `8`; equity avg `1.1585` n `137`; fx avg `0.01` n `6`; index avg `0.2558` n `27`; metal avg `0.4651` n `20`; unknown avg `1.3795` n `806`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.1429`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1313`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1301`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1299`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1273`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1206`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1117`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.105`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1024`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1018`, n `668`, weak_sample_signal
