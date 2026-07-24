# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-24T07:37:27.465774+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0228` n `12`; crypto_alt avg `-0.2219` n `230`; crypto_major avg `-0.3319` n `8`; equity avg `0.01` n `100`; fx avg `0.0` n `6`; index avg `-0.0054` n `25`; metal avg `0.0191` n `20`; unknown avg `0.0273` n `772`
- 1h: commodity avg `-0.1213` n `12`; crypto_alt avg `0.0066` n `230`; crypto_major avg `0.1264` n `8`; equity avg `0.4297` n `100`; fx avg `0.0068` n `6`; index avg `0.0811` n `25`; metal avg `0.171` n `20`; unknown avg `0.0464` n `772`
- 4h: commodity avg `-0.3692` n `12`; crypto_alt avg `0.322` n `230`; crypto_major avg `0.3673` n `8`; equity avg `0.5982` n `100`; fx avg `0.0362` n `6`; index avg `0.1037` n `25`; metal avg `0.2192` n `20`; unknown avg `0.2084` n `756`
- 24h: commodity avg `-0.0271` n `12`; crypto_alt avg `-0.5436` n `230`; crypto_major avg `-0.8397` n `8`; equity avg `-1.2558` n `99`; fx avg `-0.1222` n `6`; index avg `-0.384` n `25`; metal avg `-0.4012` n `20`; unknown avg `0.1317` n `756`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1583`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1511`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.129`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1003`, n `666`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0929`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0878`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0863`, n `666`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0835`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0832`, n `666`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.082`, n `666`, weak_sample_signal
