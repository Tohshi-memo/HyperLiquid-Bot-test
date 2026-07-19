# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-19T16:52:29.881228+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.2` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0091` n `12`; crypto_alt avg `-0.0081` n `230`; crypto_major avg `-0.0329` n `8`; equity avg `0.0232` n `96`; fx avg `0.0006` n `6`; index avg `0.0079` n `25`; metal avg `-0.0042` n `20`; unknown avg `-0.0151` n `770`
- 1h: commodity avg `-0.0285` n `12`; crypto_alt avg `-0.1983` n `230`; crypto_major avg `-0.2247` n `8`; equity avg `0.001` n `96`; fx avg `-0.0009` n `6`; index avg `-0.0751` n `25`; metal avg `-0.0298` n `20`; unknown avg `-0.0393` n `770`
- 4h: commodity avg `-0.0225` n `12`; crypto_alt avg `-0.0254` n `230`; crypto_major avg `-0.09` n `8`; equity avg `-0.0609` n `96`; fx avg `0.0062` n `6`; index avg `-0.0854` n `25`; metal avg `-0.0034` n `20`; unknown avg `0.0708` n `770`
- 24h: commodity avg `0.2167` n `12`; crypto_alt avg `0.1084` n `230`; crypto_major avg `0.5398` n `8`; equity avg `0.2609` n `96`; fx avg `0.0523` n `6`; index avg `-0.0984` n `25`; metal avg `-0.0489` n `20`; unknown avg `0.068` n `752`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `0.1434`, n `666`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1401`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1381`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1296`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1292`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1276`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1191`, n `666`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1051`, n `666`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1012`, n `666`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0994`, n `668`, weak_sample_signal
