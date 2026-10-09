# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-09T10:07:36.088776+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0027` n `13`; crypto_alt avg `0.045` n `235`; crypto_major avg `0.0399` n `8`; equity avg `0.046` n `150`; fx avg `0.0042` n `6`; index avg `0.0044` n `26`; metal avg `-0.0014` n `20`; unknown avg `-0.0408` n `1076`
- 1h: commodity avg `-0.007` n `13`; crypto_alt avg `-0.0485` n `235`; crypto_major avg `0.0409` n `8`; equity avg `-0.0106` n `150`; fx avg `0.0075` n `6`; index avg `-0.0091` n `26`; metal avg `-0.0109` n `20`; unknown avg `0.6767` n `1076`
- 4h: commodity avg `-0.0593` n `13`; crypto_alt avg `0.0862` n `235`; crypto_major avg `0.1339` n `8`; equity avg `0.1521` n `150`; fx avg `-0.0066` n `6`; index avg `0.0368` n `26`; metal avg `-0.0212` n `20`; unknown avg `0.3992` n `1006`
- 24h: commodity avg `-0.4432` n `13`; crypto_alt avg `-1.7787` n `235`; crypto_major avg `-2.058` n `8`; equity avg `-0.4379` n `150`; fx avg `0.0837` n `6`; index avg `0.052` n `26`; metal avg `0.4331` n `20`; unknown avg `7.6367` n `949`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.1498`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.137`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.124`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1146`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1145`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.101`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0952`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0934`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0845`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0796`, n `668`, weak_sample_signal
