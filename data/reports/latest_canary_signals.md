# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-23T06:37:33.673000+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0315` n `12`; crypto_alt avg `0.0174` n `230`; crypto_major avg `0.1118` n `8`; equity avg `0.0726` n `98`; fx avg `0.0051` n `6`; index avg `0.0027` n `25`; metal avg `-0.014` n `20`; unknown avg `0.0329` n `773`
- 1h: commodity avg `0.0851` n `12`; crypto_alt avg `-0.0549` n `230`; crypto_major avg `-0.0357` n `8`; equity avg `-0.2427` n `98`; fx avg `0.0123` n `6`; index avg `-0.0635` n `25`; metal avg `-0.0915` n `20`; unknown avg `0.0188` n `741`
- 4h: commodity avg `0.0831` n `12`; crypto_alt avg `0.0842` n `230`; crypto_major avg `0.0083` n `8`; equity avg `0.3257` n `98`; fx avg `0.009` n `6`; index avg `0.0617` n `25`; metal avg `-0.0298` n `20`; unknown avg `-0.1432` n `741`
- 24h: commodity avg `0.6745` n `12`; crypto_alt avg `0.0625` n `230`; crypto_major avg `0.2284` n `8`; equity avg `0.5503` n `98`; fx avg `-0.0853` n `6`; index avg `0.166` n `25`; metal avg `-0.0073` n `20`; unknown avg `1.6358` n `740`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.154`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1157`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.111`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.109`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1072`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0926`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0905`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0861`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.085`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0788`, n `666`, weak_sample_signal
