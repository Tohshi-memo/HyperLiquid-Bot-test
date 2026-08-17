# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-17T03:37:30.487763+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.051` n `12`; crypto_alt avg `0.0167` n `230`; crypto_major avg `0.0339` n `8`; equity avg `0.0421` n `114`; fx avg `0.006` n `6`; index avg `0.0085` n `25`; metal avg `0.0062` n `20`; unknown avg `0.0939` n `792`
- 1h: commodity avg `-0.0357` n `12`; crypto_alt avg `0.123` n `230`; crypto_major avg `0.1851` n `8`; equity avg `0.2791` n `114`; fx avg `0.0292` n `6`; index avg `0.0283` n `25`; metal avg `-0.004` n `20`; unknown avg `0.1815` n `792`
- 4h: commodity avg `0.0086` n `12`; crypto_alt avg `0.8041` n `230`; crypto_major avg `1.1016` n `8`; equity avg `0.5968` n `114`; fx avg `-0.0101` n `6`; index avg `0.0347` n `25`; metal avg `0.2239` n `20`; unknown avg `0.8315` n `792`
- 24h: commodity avg `-0.1147` n `12`; crypto_alt avg `0.2478` n `230`; crypto_major avg `0.5666` n `8`; equity avg `0.708` n `114`; fx avg `-0.0202` n `6`; index avg `0.0747` n `25`; metal avg `0.2035` n `20`; unknown avg `0.0493` n `759`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.1785`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1731`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1463`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1442`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1316`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1247`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1112`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1015`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0931`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0898`, n `668`, weak_sample_signal
