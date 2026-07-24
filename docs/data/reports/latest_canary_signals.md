# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-24T18:22:30.303645+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0755` n `12`; crypto_alt avg `-0.1358` n `230`; crypto_major avg `-0.1103` n `8`; equity avg `-0.3115` n `100`; fx avg `0.0015` n `6`; index avg `-0.0602` n `25`; metal avg `-0.0554` n `20`; unknown avg `-0.0376` n `773`
- 1h: commodity avg `0.0244` n `12`; crypto_alt avg `-0.0848` n `230`; crypto_major avg `0.0263` n `8`; equity avg `-0.4414` n `100`; fx avg `-0.002` n `6`; index avg `-0.0555` n `25`; metal avg `-0.0664` n `20`; unknown avg `-0.0798` n `773`
- 4h: commodity avg `-0.2372` n `12`; crypto_alt avg `0.4703` n `230`; crypto_major avg `0.5281` n `8`; equity avg `-0.3568` n `100`; fx avg `-0.0165` n `6`; index avg `0.001` n `25`; metal avg `0.0408` n `20`; unknown avg `13.3777` n `773`
- 24h: commodity avg `-0.6854` n `12`; crypto_alt avg `-0.8217` n `230`; crypto_major avg `-0.7983` n `8`; equity avg `-2.7197` n `100`; fx avg `-0.1555` n `6`; index avg `-0.3002` n `25`; metal avg `0.1027` n `20`; unknown avg `14.1309` n `756`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1484`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1466`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1226`, n `666`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1206`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1181`, n `666`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1169`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1125`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1109`, n `666`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1063`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1029`, n `666`, weak_sample_signal
