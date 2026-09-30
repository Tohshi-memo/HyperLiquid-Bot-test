# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-30T16:52:41.526706+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0372` n `12`; crypto_alt avg `0.3262` n `234`; crypto_major avg `0.34` n `8`; equity avg `0.0485` n `142`; fx avg `-0.0034` n `6`; index avg `0.0015` n `26`; metal avg `0.0009` n `20`; unknown avg `0.3248` n `969`
- 1h: commodity avg `-0.1018` n `12`; crypto_alt avg `0.5916` n `234`; crypto_major avg `0.567` n `8`; equity avg `0.0255` n `142`; fx avg `-0.0052` n `6`; index avg `-0.0217` n `26`; metal avg `0.018` n `20`; unknown avg `2.4103` n `961`
- 4h: commodity avg `0.1623` n `12`; crypto_alt avg `-0.616` n `234`; crypto_major avg `-0.793` n `8`; equity avg `-0.4598` n `142`; fx avg `0.0212` n `6`; index avg `-0.0203` n `26`; metal avg `-0.3063` n `20`; unknown avg `5.9882` n `875`
- 24h: commodity avg `0.1577` n `12`; crypto_alt avg `2.105` n `234`; crypto_major avg `1.9383` n `8`; equity avg `0.0966` n `142`; fx avg `0.0807` n `6`; index avg `0.1747` n `26`; metal avg `0.0277` n `20`; unknown avg `4.1715` n `820`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.1338`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1301`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1247`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1113`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1108`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.109`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0973`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0946`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0911`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0885`, n `668`, weak_sample_signal
