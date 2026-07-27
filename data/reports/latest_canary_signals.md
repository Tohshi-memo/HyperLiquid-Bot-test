# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-27T03:07:29.431047+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0429` n `12`; crypto_alt avg `0.0137` n `230`; crypto_major avg `0.0456` n `8`; equity avg `0.08` n `100`; fx avg `-0.0016` n `6`; index avg `0.0239` n `25`; metal avg `-0.0138` n `20`; unknown avg `0.1759` n `775`
- 1h: commodity avg `-0.0406` n `12`; crypto_alt avg `0.0088` n `230`; crypto_major avg `-0.0884` n `8`; equity avg `0.2634` n `100`; fx avg `-0.004` n `6`; index avg `0.0367` n `25`; metal avg `-0.1286` n `20`; unknown avg `0.3207` n `775`
- 4h: commodity avg `-0.0063` n `12`; crypto_alt avg `-0.1598` n `230`; crypto_major avg `-0.5105` n `8`; equity avg `-0.2398` n `100`; fx avg `0.0999` n `6`; index avg `-0.136` n `25`; metal avg `-0.0127` n `20`; unknown avg `-0.0328` n `775`
- 24h: commodity avg `-0.4862` n `12`; crypto_alt avg `1.3728` n `230`; crypto_major avg `1.2402` n `8`; equity avg `0.7537` n `100`; fx avg `0.1418` n `6`; index avg `0.0654` n `25`; metal avg `0.3386` n `20`; unknown avg `-0.0039` n `758`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1667`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1488`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1464`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1376`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1293`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1244`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1224`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.122`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1214`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1025`, n `668`, weak_sample_signal
