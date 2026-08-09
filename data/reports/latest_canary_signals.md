# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-09T07:22:30.423182+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0164` n `12`; crypto_alt avg `-0.182` n `230`; crypto_major avg `-0.0905` n `8`; equity avg `-0.046` n `112`; fx avg `-0.0045` n `6`; index avg `0.0066` n `25`; metal avg `-0.0` n `20`; unknown avg `-0.0305` n `785`
- 1h: commodity avg `-0.0438` n `12`; crypto_alt avg `-0.1921` n `230`; crypto_major avg `0.0124` n `8`; equity avg `-0.0148` n `112`; fx avg `0.0065` n `6`; index avg `0.0103` n `25`; metal avg `-0.0199` n `20`; unknown avg `-0.0051` n `785`
- 4h: commodity avg `0.0076` n `12`; crypto_alt avg `0.0641` n `230`; crypto_major avg `0.1317` n `8`; equity avg `0.0775` n `112`; fx avg `-0.0242` n `6`; index avg `-0.0006` n `25`; metal avg `-0.0145` n `20`; unknown avg `-0.006` n `752`
- 24h: commodity avg `0.2177` n `12`; crypto_alt avg `1.2415` n `230`; crypto_major avg `0.4907` n `8`; equity avg `0.6626` n `112`; fx avg `-0.0178` n `6`; index avg `0.0713` n `25`; metal avg `0.0209` n `20`; unknown avg `0.5579` n `752`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.143`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0916`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.067`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0642`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0615`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0596`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0571`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0508`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0483`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0434`, n `668`, weak_sample_signal
