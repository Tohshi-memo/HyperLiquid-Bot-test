# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-26T09:07:18.808518+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.109` n `12`; crypto_alt avg `-0.057` n `228`; crypto_major avg `-0.0583` n `8`; equity avg `0.0587` n `67`; fx avg `-0.0092` n `6`; index avg `0.016` n `23`; metal avg `-0.0498` n `18`; unknown avg `-0.2872` n `417`
- 1h: commodity avg `0.2627` n `12`; crypto_alt avg `0.0055` n `228`; crypto_major avg `-0.0801` n `8`; equity avg `0.2741` n `67`; fx avg `0.0009` n `6`; index avg `0.0602` n `23`; metal avg `-0.1944` n `18`; unknown avg `-0.3764` n `417`
- 4h: commodity avg `0.5566` n `12`; crypto_alt avg `0.1162` n `228`; crypto_major avg `-0.1221` n `8`; equity avg `0.2091` n `67`; fx avg `-0.0228` n `6`; index avg `-0.0022` n `23`; metal avg `-0.1849` n `18`; unknown avg `-0.009` n `397`
- 24h: commodity avg `0.9668` n `12`; crypto_alt avg `-0.9116` n `228`; crypto_major avg `-1.7848` n `8`; equity avg `-0.4853` n `67`; fx avg `-0.1008` n `6`; index avg `-0.0869` n `23`; metal avg `-0.669` n `18`; unknown avg `-0.2438` n `387`

## Correlations

- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1756`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1747`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1736`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1503`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1421`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.133`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1302`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1244`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1232`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1166`, n `668`, weak_sample_signal
