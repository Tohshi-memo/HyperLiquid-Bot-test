# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-18T03:07:27.351603+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.049` n `13`; crypto_alt avg `0.1749` n `239`; crypto_major avg `0.3247` n `8`; equity avg `0.3881` n `163`; fx avg `0.0079` n `6`; index avg `0.0647` n `27`; metal avg `-0.0264` n `20`; unknown avg `2.1763` n `1260`
- 1h: commodity avg `0.0571` n `13`; crypto_alt avg `0.0516` n `239`; crypto_major avg `0.3461` n `8`; equity avg `-0.0068` n `163`; fx avg `-0.0205` n `6`; index avg `0.0283` n `27`; metal avg `-0.0484` n `20`; unknown avg `2.5325` n `1262`
- 4h: commodity avg `-0.1387` n `13`; crypto_alt avg `-0.9115` n `239`; crypto_major avg `-0.7657` n `8`; equity avg `-1.7534` n `163`; fx avg `-0.0938` n `6`; index avg `-0.2214` n `27`; metal avg `-0.6061` n `20`; unknown avg `4.5569` n `1257`
- 24h: commodity avg `0.2469` n `13`; crypto_alt avg `0.1431` n `239`; crypto_major avg `0.6146` n `8`; equity avg `-0.7458` n `163`; fx avg `-0.1198` n `6`; index avg `-0.1374` n `27`; metal avg `-0.8162` n `20`; unknown avg `7.1693` n `1071`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.1231`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.1026`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0989`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0979`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0932`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.086`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0852`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0811`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0784`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0669`, n `668`, weak_sample_signal
