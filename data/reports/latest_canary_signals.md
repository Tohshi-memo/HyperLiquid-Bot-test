# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-08T10:37:30.923583+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0419` n `12`; crypto_alt avg `-0.013` n `230`; crypto_major avg `0.0051` n `8`; equity avg `0.0408` n `112`; fx avg `-0.0072` n `6`; index avg `-0.0074` n `25`; metal avg `-0.0104` n `20`; unknown avg `0.0` n `784`
- 1h: commodity avg `0.0643` n `12`; crypto_alt avg `0.0317` n `230`; crypto_major avg `0.0345` n `8`; equity avg `0.0695` n `112`; fx avg `-0.0107` n `6`; index avg `-0.005` n `25`; metal avg `0.0024` n `20`; unknown avg `1.1898` n `784`
- 4h: commodity avg `0.0865` n `12`; crypto_alt avg `0.2407` n `230`; crypto_major avg `0.2114` n `8`; equity avg `0.23` n `112`; fx avg `-0.0098` n `6`; index avg `0.0063` n `25`; metal avg `0.0389` n `20`; unknown avg `1.4019` n `784`
- 24h: commodity avg `0.1754` n `12`; crypto_alt avg `0.065` n `230`; crypto_major avg `0.1729` n `8`; equity avg `0.874` n `112`; fx avg `-0.0173` n `6`; index avg `0.0414` n `25`; metal avg `-0.076` n `20`; unknown avg `1.2546` n `750`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1146`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.086`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0769`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0686`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0672`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0649`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0576`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0533`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0531`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0506`, n `668`, weak_sample_signal
