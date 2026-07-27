# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-27T04:22:36.060368+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0053` n `12`; crypto_alt avg `0.0597` n `230`; crypto_major avg `0.1533` n `8`; equity avg `0.1439` n `100`; fx avg `0.006` n `6`; index avg `0.044` n `25`; metal avg `-0.0126` n `20`; unknown avg `0.2028` n `775`
- 1h: commodity avg `-0.0822` n `12`; crypto_alt avg `0.1504` n `230`; crypto_major avg `0.4429` n `8`; equity avg `0.0731` n `100`; fx avg `0.0082` n `6`; index avg `-0.0114` n `25`; metal avg `-0.0262` n `20`; unknown avg `0.0217` n `775`
- 4h: commodity avg `0.0753` n `12`; crypto_alt avg `0.1551` n `230`; crypto_major avg `0.316` n `8`; equity avg `0.2237` n `100`; fx avg `0.067` n `6`; index avg `-0.0225` n `25`; metal avg `-0.1365` n `20`; unknown avg `-0.0392` n `775`
- 24h: commodity avg `-0.5063` n `12`; crypto_alt avg `1.4112` n `230`; crypto_major avg `1.589` n `8`; equity avg `0.8446` n `100`; fx avg `0.0758` n `6`; index avg `0.0845` n `25`; metal avg `0.3044` n `20`; unknown avg `0.0074` n `759`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1724`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1586`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1474`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1336`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1279`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1205`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1201`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1156`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1105`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.099`, n `668`, weak_sample_signal
