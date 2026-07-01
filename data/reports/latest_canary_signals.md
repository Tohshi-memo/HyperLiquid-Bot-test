# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-01T20:07:33.643444+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0052` n `12`; crypto_alt avg `0.0246` n `228`; crypto_major avg `-0.029` n `8`; equity avg `-0.3359` n `88`; fx avg `0.0067` n `6`; index avg `-0.0596` n `25`; metal avg `-0.0689` n `20`; unknown avg `0.1864` n `763`
- 1h: commodity avg `-0.0532` n `12`; crypto_alt avg `-0.3786` n `228`; crypto_major avg `-0.5336` n `8`; equity avg `-0.5606` n `88`; fx avg `0.01` n `6`; index avg `-0.1088` n `25`; metal avg `-0.2888` n `20`; unknown avg `0.7688` n `763`
- 4h: commodity avg `-0.0491` n `12`; crypto_alt avg `-1.0198` n `228`; crypto_major avg `-0.6694` n `8`; equity avg `-1.2244` n `88`; fx avg `0.01` n `6`; index avg `-0.2085` n `25`; metal avg `-0.5007` n `20`; unknown avg `0.0364` n `761`
- 24h: commodity avg `-0.6353` n `12`; crypto_alt avg `1.139` n `228`; crypto_major avg `0.9375` n `8`; equity avg `-1.7673` n `88`; fx avg `-0.0154` n `6`; index avg `-0.5814` n `25`; metal avg `-0.0055` n `20`; unknown avg `0.0265` n `739`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1226`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1136`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0974`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.097`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0866`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.079`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.078`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0731`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0686`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0646`, n `668`, weak_sample_signal
