# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-09T05:52:25.466460+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0202` n `12`; crypto_alt avg `0.0941` n `230`; crypto_major avg `0.0154` n `8`; equity avg `-0.0049` n `112`; fx avg `-0.0023` n `6`; index avg `0.0001` n `25`; metal avg `0.0032` n `20`; unknown avg `-0.1737` n `784`
- 1h: commodity avg `-0.0024` n `12`; crypto_alt avg `-0.2533` n `230`; crypto_major avg `-0.0868` n `8`; equity avg `0.0056` n `112`; fx avg `-0.0076` n `6`; index avg `-0.001` n `25`; metal avg `0.0037` n `20`; unknown avg `-0.1402` n `784`
- 4h: commodity avg `0.0753` n `12`; crypto_alt avg `0.1457` n `230`; crypto_major avg `-0.1644` n `8`; equity avg `-0.0179` n `112`; fx avg `-0.0071` n `6`; index avg `0.0043` n `25`; metal avg `0.0053` n `20`; unknown avg `-0.1333` n `784`
- 24h: commodity avg `0.2702` n `12`; crypto_alt avg `1.4383` n `230`; crypto_major avg `0.4464` n `8`; equity avg `0.5416` n `112`; fx avg `-0.0088` n `6`; index avg `0.0771` n `25`; metal avg `0.0237` n `20`; unknown avg `-0.0272` n `752`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1614`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1029`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0772`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0732`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0653`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0628`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0582`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0498`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0481`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0464`, n `668`, weak_sample_signal
