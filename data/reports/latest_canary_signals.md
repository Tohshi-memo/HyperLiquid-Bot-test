# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-31T00:52:31.554762+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `-1.5664` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0648` n `12`; crypto_alt avg `0.0747` n `230`; crypto_major avg `-0.1245` n `8`; equity avg `0.0265` n `102`; fx avg `0.0657` n `6`; index avg `0.0027` n `25`; metal avg `-0.0133` n `20`; unknown avg `-0.058` n `779`
- 1h: commodity avg `0.0045` n `12`; crypto_alt avg `0.1889` n `230`; crypto_major avg `-0.1968` n `8`; equity avg `0.6202` n `102`; fx avg `0.1783` n `6`; index avg `0.2708` n `25`; metal avg `-0.0835` n `20`; unknown avg `3.8734` n `779`
- 4h: commodity avg `0.0066` n `12`; crypto_alt avg `0.0685` n `230`; crypto_major avg `-0.0896` n `8`; equity avg `1.4768` n `102`; fx avg `0.207` n `6`; index avg `0.3766` n `25`; metal avg `-0.0297` n `20`; unknown avg `0.0744` n `779`
- 24h: commodity avg `-0.0856` n `12`; crypto_alt avg `1.0477` n `230`; crypto_major avg `1.5372` n `8`; equity avg `8.2206` n `102`; fx avg `-0.1471` n `6`; index avg `1.1783` n `25`; metal avg `0.5608` n `20`; unknown avg `0.1106` n `738`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1463`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1431`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1094`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0986`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.082`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0805`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0776`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0716`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.063`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0604`, n `668`, weak_sample_signal
