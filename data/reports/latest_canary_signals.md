# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-27T22:07:26.462310+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.3834` n `12`; crypto_alt avg `-0.653` n `234`; crypto_major avg `-0.4804` n `8`; equity avg `-0.2016` n `141`; fx avg `0.0108` n `6`; index avg `-0.0624` n `26`; metal avg `-0.0947` n `20`; unknown avg `1.1521` n `940`
- 1h: commodity avg `-0.3382` n `12`; crypto_alt avg `-0.4063` n `234`; crypto_major avg `-0.4648` n `8`; equity avg `-0.2292` n `141`; fx avg `0.0347` n `6`; index avg `-0.0507` n `26`; metal avg `-0.1012` n `20`; unknown avg `3.6513` n `908`
- 4h: commodity avg `-0.3432` n `12`; crypto_alt avg `-0.279` n `234`; crypto_major avg `-0.3837` n `8`; equity avg `-0.1847` n `141`; fx avg `-0.0181` n `6`; index avg `-0.0497` n `26`; metal avg `-0.1013` n `20`; unknown avg `2.0586` n `874`
- 24h: commodity avg `-0.4927` n `12`; crypto_alt avg `0.2668` n `234`; crypto_major avg `-0.2238` n `8`; equity avg `0.1418` n `141`; fx avg `-0.025` n `6`; index avg `-0.0072` n `26`; metal avg `-0.1179` n `20`; unknown avg `7.838` n `841`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1569`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1532`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1275`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1274`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1266`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1234`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1232`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1026`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.102`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0954`, n `668`, weak_sample_signal
