# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-09T13:11:43.216841+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0015` n `12`; crypto_alt avg `0.1589` n `230`; crypto_major avg `0.1365` n `8`; equity avg `0.0265` n `112`; fx avg `-0.0081` n `6`; index avg `-0.0028` n `25`; metal avg `0.0024` n `20`; unknown avg `-0.0199` n `785`
- 1h: commodity avg `0.0054` n `12`; crypto_alt avg `0.2982` n `230`; crypto_major avg `0.1854` n `8`; equity avg `0.0848` n `112`; fx avg `-0.0144` n `6`; index avg `0.0144` n `25`; metal avg `0.0188` n `20`; unknown avg `0.0071` n `785`
- 4h: commodity avg `-0.0629` n `12`; crypto_alt avg `0.3699` n `230`; crypto_major avg `0.1662` n `8`; equity avg `0.0219` n `112`; fx avg `-0.0079` n `6`; index avg `0.0114` n `25`; metal avg `0.0045` n `20`; unknown avg `0.0136` n `785`
- 24h: commodity avg `0.1226` n `12`; crypto_alt avg `1.2083` n `230`; crypto_major avg `0.1732` n `8`; equity avg `0.4452` n `112`; fx avg `-0.0178` n `6`; index avg `0.0389` n `25`; metal avg `0.0469` n `20`; unknown avg `0.2218` n `752`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1376`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0794`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0778`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0582`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0577`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0535`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0513`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0501`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0475`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0471`, n `668`, weak_sample_signal
