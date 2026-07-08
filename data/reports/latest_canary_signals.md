# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-08T10:07:31.272814+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0146` n `12`; crypto_alt avg `-0.2303` n `229`; crypto_major avg `-0.2037` n `8`; equity avg `-0.1542` n `91`; fx avg `-0.0048` n `6`; index avg `-0.0437` n `25`; metal avg `-0.0262` n `20`; unknown avg `-0.0511` n `763`
- 1h: commodity avg `-0.0263` n `12`; crypto_alt avg `-0.2413` n `229`; crypto_major avg `-0.0707` n `8`; equity avg `-0.0709` n `91`; fx avg `-0.0379` n `6`; index avg `-0.0151` n `25`; metal avg `-0.0859` n `20`; unknown avg `-0.1334` n `763`
- 4h: commodity avg `0.5435` n `12`; crypto_alt avg `-1.4268` n `229`; crypto_major avg `-1.033` n `8`; equity avg `-1.9614` n `91`; fx avg `-0.0066` n `6`; index avg `-0.4509` n `25`; metal avg `-1.1259` n `20`; unknown avg `-0.49` n `763`
- 24h: commodity avg `1.4566` n `12`; crypto_alt avg `-4.1917` n `229`; crypto_major avg `-3.5511` n `8`; equity avg `-3.4196` n `91`; fx avg `-0.1403` n `6`; index avg `-0.7786` n `25`; metal avg `-1.3165` n `20`; unknown avg `-0.8948` n `733`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1367`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1019`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1011`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1009`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0956`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0951`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0939`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0881`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0746`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0744`, n `668`, weak_sample_signal
