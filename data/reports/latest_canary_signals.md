# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-26T17:07:27.786281+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0051` n `12`; crypto_alt avg `-0.0935` n `230`; crypto_major avg `-0.1067` n `8`; equity avg `-0.0079` n `100`; fx avg `-0.0015` n `6`; index avg `-0.0108` n `25`; metal avg `-0.0004` n `20`; unknown avg `-0.0657` n `775`
- 1h: commodity avg `-0.0152` n `12`; crypto_alt avg `-0.0144` n `230`; crypto_major avg `0.0991` n `8`; equity avg `0.0556` n `100`; fx avg `-0.0174` n `6`; index avg `0.0111` n `25`; metal avg `0.0252` n `20`; unknown avg `-0.1619` n `775`
- 4h: commodity avg `-0.0322` n `12`; crypto_alt avg `0.3686` n `230`; crypto_major avg `0.6648` n `8`; equity avg `0.2229` n `100`; fx avg `-0.0211` n `6`; index avg `0.0343` n `25`; metal avg `0.0309` n `20`; unknown avg `0.1738` n `775`
- 24h: commodity avg `-0.4636` n `12`; crypto_alt avg `1.0911` n `230`; crypto_major avg `1.1396` n `8`; equity avg `0.8797` n `100`; fx avg `0.0023` n `6`; index avg `0.1895` n `25`; metal avg `0.2061` n `20`; unknown avg `-0.011` n `758`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1939`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1838`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1653`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1482`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1386`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1327`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1294`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1294`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.127`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1257`, n `668`, weak_sample_signal
