# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-07T09:08:02.928053+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0321` n `12`; crypto_alt avg `0.0792` n `232`; crypto_major avg `0.0384` n `8`; equity avg `0.0312` n `134`; fx avg `-0.0157` n `6`; index avg `0.0033` n `26`; metal avg `-0.0058` n `20`; unknown avg `1.3529` n `794`
- 1h: commodity avg `0.0408` n `12`; crypto_alt avg `0.4948` n `232`; crypto_major avg `0.1342` n `8`; equity avg `0.0813` n `134`; fx avg `-0.1007` n `6`; index avg `-0.0006` n `26`; metal avg `-0.02` n `20`; unknown avg `2.3886` n `788`
- 4h: commodity avg `-0.1374` n `12`; crypto_alt avg `-0.1334` n `232`; crypto_major avg `-0.2272` n `8`; equity avg `0.0587` n `134`; fx avg `-0.1613` n `6`; index avg `0.0563` n `26`; metal avg `0.1159` n `20`; unknown avg `2.0681` n `758`
- 24h: commodity avg `-0.0716` n `12`; crypto_alt avg `0.3231` n `232`; crypto_major avg `-0.6425` n `8`; equity avg `0.4661` n `134`; fx avg `-0.1403` n `6`; index avg `0.0594` n `26`; metal avg `-0.0606` n `20`; unknown avg `76.6054` n `648`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1945`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1234`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1058`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1037`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1015`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0986`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.092`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.088`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0819`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0735`, n `668`, weak_sample_signal
