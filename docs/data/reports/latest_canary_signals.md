# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-24T08:07:24.782334+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0478` n `12`; crypto_alt avg `-0.0138` n `230`; crypto_major avg `0.0097` n `8`; equity avg `-0.1449` n `100`; fx avg `-0.0093` n `6`; index avg `-0.0228` n `25`; metal avg `-0.0319` n `20`; unknown avg `0.0098` n `772`
- 1h: commodity avg `-0.0031` n `12`; crypto_alt avg `-0.0246` n `230`; crypto_major avg `0.0121` n `8`; equity avg `0.1342` n `100`; fx avg `-0.0133` n `6`; index avg `0.0239` n `25`; metal avg `0.0312` n `20`; unknown avg `0.0164` n `772`
- 4h: commodity avg `-0.2684` n `12`; crypto_alt avg `0.2859` n `230`; crypto_major avg `0.3664` n `8`; equity avg `0.4595` n `100`; fx avg `0.0392` n `6`; index avg `0.0758` n `25`; metal avg `0.1675` n `20`; unknown avg `0.0928` n `756`
- 24h: commodity avg `0.0726` n `12`; crypto_alt avg `-0.6721` n `230`; crypto_major avg `-0.9998` n `8`; equity avg `-1.6697` n `99`; fx avg `-0.1128` n `6`; index avg `-0.468` n `25`; metal avg `-0.543` n `20`; unknown avg `0.1072` n `756`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1552`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1474`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1265`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0976`, n `666`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0926`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0876`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0859`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0837`, n `666`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.081`, n `666`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0797`, n `666`, weak_sample_signal
