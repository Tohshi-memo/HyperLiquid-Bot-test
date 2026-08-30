# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-30T08:52:29.546563+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0049` n `12`; crypto_alt avg `-0.0094` n `231`; crypto_major avg `-0.0816` n `8`; equity avg `-0.0135` n `128`; fx avg `-0.0011` n `6`; index avg `0.0027` n `26`; metal avg `-0.0017` n `20`; unknown avg `-0.0654` n `793`
- 1h: commodity avg `0.0187` n `12`; crypto_alt avg `0.0246` n `231`; crypto_major avg `-0.0397` n `8`; equity avg `0.0078` n `128`; fx avg `-0.0002` n `6`; index avg `0.0004` n `26`; metal avg `-0.0017` n `20`; unknown avg `-0.1173` n `793`
- 4h: commodity avg `0.0018` n `12`; crypto_alt avg `0.3522` n `231`; crypto_major avg `0.1269` n `8`; equity avg `0.0216` n `128`; fx avg `0.0045` n `6`; index avg `0.0045` n `26`; metal avg `0.0153` n `20`; unknown avg `-0.0348` n `759`
- 24h: commodity avg `0.0123` n `12`; crypto_alt avg `1.0248` n `231`; crypto_major avg `0.8892` n `8`; equity avg `0.2931` n `128`; fx avg `-0.0044` n `6`; index avg `0.0552` n `26`; metal avg `0.0855` n `20`; unknown avg `0.7489` n `714`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1548`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1278`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1214`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1154`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1068`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0977`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0968`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0943`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0816`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0783`, n `668`, weak_sample_signal
