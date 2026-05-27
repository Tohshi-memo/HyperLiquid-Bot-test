# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-27T03:07:20.093797+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1251` n `12`; crypto_alt avg `0.241` n `228`; crypto_major avg `0.364` n `8`; equity avg `0.0211` n `67`; fx avg `0.006` n `6`; index avg `-0.0174` n `23`; metal avg `0.1008` n `18`; unknown avg `0.7914` n `418`
- 1h: commodity avg `-0.1848` n `12`; crypto_alt avg `0.1044` n `228`; crypto_major avg `0.4612` n `8`; equity avg `0.0285` n `67`; fx avg `-0.0388` n `6`; index avg `0.0494` n `23`; metal avg `0.2181` n `18`; unknown avg `0.559` n `418`
- 4h: commodity avg `-0.5793` n `12`; crypto_alt avg `-0.2031` n `228`; crypto_major avg `0.4281` n `8`; equity avg `0.2207` n `67`; fx avg `-0.0554` n `6`; index avg `0.1919` n `23`; metal avg `-0.1083` n `18`; unknown avg `0.5271` n `418`
- 24h: commodity avg `-0.178` n `12`; crypto_alt avg `-0.024` n `228`; crypto_major avg `0.3906` n `8`; equity avg `0.8785` n `67`; fx avg `-0.0763` n `6`; index avg `1.0443` n `23`; metal avg `0.0728` n `18`; unknown avg `1.668` n `397`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1861`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1855`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1723`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1706`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1684`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1681`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1598`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1448`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1408`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1395`, n `668`, weak_sample_signal
