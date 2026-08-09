# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-09T07:12:47.023038+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0021` n `12`; crypto_alt avg `-0.2311` n `230`; crypto_major avg `-0.0381` n `8`; equity avg `0.0272` n `112`; fx avg `-0.0027` n `6`; index avg `-0.0073` n `25`; metal avg `-0.0108` n `20`; unknown avg `0.019` n `785`
- 1h: commodity avg `-0.0299` n `12`; crypto_alt avg `0.0047` n `230`; crypto_major avg `0.154` n `8`; equity avg `0.0428` n `112`; fx avg `-0.0095` n `6`; index avg `-0.0109` n `25`; metal avg `-0.0118` n `20`; unknown avg `0.0327` n `784`
- 4h: commodity avg `0.0172` n `12`; crypto_alt avg `0.1617` n `230`; crypto_major avg `0.238` n `8`; equity avg `0.0209` n `112`; fx avg `-0.019` n `6`; index avg `-0.0109` n `25`; metal avg `-0.0042` n `20`; unknown avg `0.0254` n `752`
- 24h: commodity avg `0.2429` n `12`; crypto_alt avg `1.3967` n `230`; crypto_major avg `0.5941` n `8`; equity avg `0.7202` n `112`; fx avg `-0.0212` n `6`; index avg `0.0589` n `25`; metal avg `0.0187` n `20`; unknown avg `0.6062` n `752`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1456`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0936`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0685`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0672`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0615`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0614`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0572`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0489`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0462`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.045`, n `668`, weak_sample_signal
