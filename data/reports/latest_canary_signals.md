# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-08T14:16:01.583104+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0012` n `12`; crypto_alt avg `0.0753` n `230`; crypto_major avg `0.0293` n `8`; equity avg `-0.0186` n `112`; fx avg `-0.0019` n `6`; index avg `0.0062` n `25`; metal avg `-0.0004` n `20`; unknown avg `0.0147` n `784`
- 1h: commodity avg `0.0188` n `12`; crypto_alt avg `0.1233` n `230`; crypto_major avg `0.1456` n `8`; equity avg `-0.0246` n `112`; fx avg `0.0001` n `6`; index avg `-0.01` n `25`; metal avg `-0.0107` n `20`; unknown avg `-0.1042` n `784`
- 4h: commodity avg `0.0944` n `12`; crypto_alt avg `0.2997` n `230`; crypto_major avg `0.2584` n `8`; equity avg `0.2125` n `112`; fx avg `-0.0122` n `6`; index avg `0.0374` n `25`; metal avg `-0.0455` n `20`; unknown avg `-0.2572` n `784`
- 24h: commodity avg `-0.0412` n `12`; crypto_alt avg `0.5337` n `230`; crypto_major avg `0.3638` n `8`; equity avg `1.2255` n `112`; fx avg `-0.0162` n `6`; index avg `0.0997` n `25`; metal avg `0.045` n `20`; unknown avg `-0.1154` n `750`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1194`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.083`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0727`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0688`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0669`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0612`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0574`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0534`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0526`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0501`, n `668`, weak_sample_signal
