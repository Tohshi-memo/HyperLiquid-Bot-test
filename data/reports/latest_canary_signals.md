# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-10T01:22:28.710094+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1668` n `12`; crypto_alt avg `0.1173` n `228`; crypto_major avg `0.1478` n `8`; equity avg `0.116` n `74`; fx avg `-0.0054` n `6`; index avg `0.0878` n `23`; metal avg `0.463` n `18`; unknown avg `-0.2014` n `547`
- 1h: commodity avg `-0.5274` n `12`; crypto_alt avg `0.1593` n `228`; crypto_major avg `-0.1206` n `8`; equity avg `-0.0863` n `74`; fx avg `0.0271` n `6`; index avg `-0.0317` n `23`; metal avg `-0.4857` n `18`; unknown avg `-0.1695` n `547`
- 4h: commodity avg `-0.2551` n `12`; crypto_alt avg `-0.0161` n `228`; crypto_major avg `-0.6213` n `8`; equity avg `0.0495` n `74`; fx avg `-0.1162` n `6`; index avg `0.0204` n `23`; metal avg `-1.0206` n `18`; unknown avg `-0.44` n `547`
- 24h: commodity avg `-0.8145` n `12`; crypto_alt avg `0.0698` n `228`; crypto_major avg `-2.0053` n `8`; equity avg `-1.5747` n `74`; fx avg `0.0319` n `6`; index avg `-0.6727` n `23`; metal avg `-2.2838` n `18`; unknown avg `-0.3964` n `503`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0966`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0797`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0598`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0538`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0535`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0489`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0417`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0413`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.038`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0352`, n `668`, weak_sample_signal
