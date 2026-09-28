# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-28T10:37:30.129054+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0286` n `12`; crypto_alt avg `0.494` n `234`; crypto_major avg `0.3711` n `8`; equity avg `0.0204` n `141`; fx avg `0.0103` n `6`; index avg `-0.0017` n `26`; metal avg `0.0203` n `20`; unknown avg `0.0375` n `962`
- 1h: commodity avg `0.0818` n `12`; crypto_alt avg `0.564` n `234`; crypto_major avg `0.5612` n `8`; equity avg `0.0556` n `141`; fx avg `0.0143` n `6`; index avg `-0.0145` n `26`; metal avg `0.1057` n `20`; unknown avg `26.2233` n `960`
- 4h: commodity avg `0.3517` n `12`; crypto_alt avg `-0.5271` n `234`; crypto_major avg `0.2594` n `8`; equity avg `-0.9955` n `141`; fx avg `-0.0654` n `6`; index avg `-0.0514` n `26`; metal avg `-0.0767` n `20`; unknown avg `20.762` n `942`
- 24h: commodity avg `-0.0082` n `12`; crypto_alt avg `-3.9329` n `234`; crypto_major avg `-2.7919` n `8`; equity avg `-2.8595` n `141`; fx avg `0.0397` n `6`; index avg `-0.2991` n `26`; metal avg `-0.8822` n `20`; unknown avg `6.1754` n `814`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1605`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1461`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1458`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1294`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1174`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1078`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1045`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1043`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1034`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1013`, n `668`, weak_sample_signal
