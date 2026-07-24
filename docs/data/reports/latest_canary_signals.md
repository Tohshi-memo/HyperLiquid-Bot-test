# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-24T06:52:33.267638+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0503` n `12`; crypto_alt avg `-0.0907` n `230`; crypto_major avg `-0.0721` n `8`; equity avg `-0.0962` n `100`; fx avg `-0.0067` n `6`; index avg `-0.0371` n `25`; metal avg `-0.0038` n `20`; unknown avg `0.0351` n `772`
- 1h: commodity avg `-0.1555` n `12`; crypto_alt avg `0.2389` n `230`; crypto_major avg `0.2471` n `8`; equity avg `-0.1452` n `100`; fx avg `0.0134` n `6`; index avg `-0.0611` n `25`; metal avg `0.0757` n `20`; unknown avg `0.0681` n `756`
- 4h: commodity avg `-0.2329` n `12`; crypto_alt avg `0.6369` n `230`; crypto_major avg `0.674` n `8`; equity avg `-0.0271` n `100`; fx avg `0.0346` n `6`; index avg `0.0034` n `25`; metal avg `0.1259` n `20`; unknown avg `0.2655` n `756`
- 24h: commodity avg `0.1585` n `12`; crypto_alt avg `-0.8844` n `230`; crypto_major avg `-1.4988` n `8`; equity avg `-2.1601` n `99`; fx avg `-0.0994` n `6`; index avg `-0.5906` n `25`; metal avg `-0.8973` n `20`; unknown avg `0.0078` n `756`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1773`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1646`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1485`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1101`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0984`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0959`, n `666`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.094`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0913`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0903`, n `666`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.09`, n `666`, weak_sample_signal
