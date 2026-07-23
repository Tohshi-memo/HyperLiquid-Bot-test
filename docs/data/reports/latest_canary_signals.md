# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-23T17:51:45.343920+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0902` n `12`; crypto_alt avg `-0.0421` n `230`; crypto_major avg `-0.087` n `8`; equity avg `-0.0316` n `100`; fx avg `0.0019` n `6`; index avg `0.0137` n `25`; metal avg `-0.0189` n `20`; unknown avg `-0.0639` n `772`
- 1h: commodity avg `0.146` n `12`; crypto_alt avg `-0.1931` n `230`; crypto_major avg `-0.1524` n `8`; equity avg `-0.0721` n `100`; fx avg `0.001` n `6`; index avg `-0.0054` n `25`; metal avg `-0.0569` n `20`; unknown avg `-0.2559` n `772`
- 4h: commodity avg `0.2111` n `12`; crypto_alt avg `-0.4481` n `230`; crypto_major avg `-0.7237` n `8`; equity avg `-0.359` n `100`; fx avg `-0.0143` n `6`; index avg `-0.0997` n `25`; metal avg `-0.1446` n `20`; unknown avg `-0.4785` n `772`
- 24h: commodity avg `1.0858` n `12`; crypto_alt avg `-1.6076` n `230`; crypto_major avg `-2.3296` n `8`; equity avg `-1.1633` n `99`; fx avg `-0.0826` n `6`; index avg `-0.3516` n `25`; metal avg `-0.8548` n `20`; unknown avg `-0.5086` n `740`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1558`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1417`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1399`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1324`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1113`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0949`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0949`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0875`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0857`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0724`, n `666`, weak_sample_signal
