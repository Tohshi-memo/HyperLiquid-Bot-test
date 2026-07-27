# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-27T12:22:32.262307+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0439` n `12`; crypto_alt avg `-0.2928` n `230`; crypto_major avg `-0.3496` n `8`; equity avg `-0.286` n `100`; fx avg `-0.0132` n `6`; index avg `-0.0463` n `25`; metal avg `-0.0682` n `20`; unknown avg `-0.0171` n `776`
- 1h: commodity avg `0.1359` n `12`; crypto_alt avg `-0.2412` n `230`; crypto_major avg `-0.3775` n `8`; equity avg `-0.3319` n `100`; fx avg `-0.0085` n `6`; index avg `-0.0581` n `25`; metal avg `-0.1146` n `20`; unknown avg `-0.0071` n `776`
- 4h: commodity avg `0.0785` n `12`; crypto_alt avg `-0.3524` n `230`; crypto_major avg `-0.3192` n `8`; equity avg `-0.3723` n `100`; fx avg `-0.0516` n `6`; index avg `-0.0455` n `25`; metal avg `-0.0558` n `20`; unknown avg `-0.1689` n `775`
- 24h: commodity avg `-0.4172` n `12`; crypto_alt avg `0.2981` n `230`; crypto_major avg `0.8869` n `8`; equity avg `0.7503` n `100`; fx avg `0.0722` n `6`; index avg `0.079` n `25`; metal avg `0.2588` n `20`; unknown avg `-0.1433` n `759`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1945`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1339`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1242`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1215`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0947`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0933`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0924`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.092`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.091`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0905`, n `668`, weak_sample_signal
