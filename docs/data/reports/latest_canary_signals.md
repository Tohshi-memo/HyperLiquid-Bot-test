# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-02T14:07:25.638922+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `4.36` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.027` n `12`; crypto_alt avg `-0.1326` n `228`; crypto_major avg `-0.1466` n `8`; equity avg `0.1054` n `69`; fx avg `0.0002` n `6`; index avg `0.0714` n `23`; metal avg `-0.0987` n `18`; unknown avg `-0.0219` n `422`
- 1h: commodity avg `0.4294` n `12`; crypto_alt avg `-0.2292` n `228`; crypto_major avg `-0.2632` n `8`; equity avg `-0.0144` n `69`; fx avg `-0.0343` n `6`; index avg `0.2193` n `23`; metal avg `-0.4545` n `18`; unknown avg `-0.0935` n `422`
- 4h: commodity avg `0.2135` n `12`; crypto_alt avg `0.7375` n `228`; crypto_major avg `-0.0075` n `8`; equity avg `-0.1372` n `69`; fx avg `-0.0176` n `6`; index avg `0.2435` n `23`; metal avg `-0.4712` n `18`; unknown avg `0.3634` n `422`
- 24h: commodity avg `-1.0238` n `12`; crypto_alt avg `1.0271` n `228`; crypto_major avg `-0.9007` n `8`; equity avg `1.0561` n `69`; fx avg `0.1942` n `6`; index avg `0.5775` n `23`; metal avg `1.3561` n `18`; unknown avg `0.3311` n `412`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1347`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1193`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1096`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0737`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0726`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0699`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0699`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0679`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0631`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0601`, n `668`, weak_sample_signal
