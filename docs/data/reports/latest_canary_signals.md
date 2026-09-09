# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-09T11:22:30.712512+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0598` n `12`; crypto_alt avg `0.0613` n `233`; crypto_major avg `0.0296` n `8`; equity avg `0.0075` n `134`; fx avg `0.0135` n `6`; index avg `-0.0108` n `26`; metal avg `-0.0072` n `20`; unknown avg `0.0724` n `798`
- 1h: commodity avg `0.0819` n `12`; crypto_alt avg `-0.3282` n `233`; crypto_major avg `-0.2296` n `8`; equity avg `-0.0263` n `134`; fx avg `-0.0018` n `6`; index avg `-0.0303` n `26`; metal avg `0.0161` n `20`; unknown avg `11.7209` n `796`
- 4h: commodity avg `0.1347` n `12`; crypto_alt avg `-0.8963` n `233`; crypto_major avg `-0.8662` n `8`; equity avg `-0.7163` n `134`; fx avg `0.0028` n `6`; index avg `-0.1941` n `26`; metal avg `-0.09` n `20`; unknown avg `0.3622` n `790`
- 24h: commodity avg `-0.0066` n `12`; crypto_alt avg `-0.4339` n `232`; crypto_major avg `0.6668` n `8`; equity avg `0.2645` n `134`; fx avg `-0.096` n `6`; index avg `-0.1666` n `26`; metal avg `-0.0269` n `20`; unknown avg `1.1821` n `689`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `0.1183`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1066`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.094`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0903`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0861`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0805`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0799`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0774`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0755`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0748`, n `668`, weak_sample_signal
