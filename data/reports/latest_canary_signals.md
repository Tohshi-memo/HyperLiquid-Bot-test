# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-15T07:22:30.756272+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0523` n `12`; crypto_alt avg `0.1832` n `233`; crypto_major avg `0.1245` n `8`; equity avg `0.0245` n `136`; fx avg `0.0296` n `6`; index avg `-0.011` n `27`; metal avg `-0.0335` n `20`; unknown avg `0.7826` n `908`
- 1h: commodity avg `0.0396` n `12`; crypto_alt avg `-0.1187` n `233`; crypto_major avg `-0.3085` n `8`; equity avg `-0.1015` n `136`; fx avg `0.0337` n `6`; index avg `-0.0368` n `27`; metal avg `-0.0819` n `20`; unknown avg `17.2224` n `904`
- 4h: commodity avg `0.1061` n `12`; crypto_alt avg `-0.3329` n `233`; crypto_major avg `-0.5884` n `8`; equity avg `-0.5312` n `136`; fx avg `0.0861` n `6`; index avg `-0.1327` n `27`; metal avg `-0.1945` n `20`; unknown avg `3.0195` n `868`
- 24h: commodity avg `0.0144` n `12`; crypto_alt avg `-1.3797` n `233`; crypto_major avg `-0.6819` n `8`; equity avg `-0.2579` n `136`; fx avg `0.1862` n `6`; index avg `-0.0742` n `27`; metal avg `-0.3362` n `20`; unknown avg `4.3682` n `820`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1046`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0992`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0964`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0935`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0872`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.085`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0729`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0718`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0642`, n `668`, weak_sample_signal
