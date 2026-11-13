# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-13T09:37:44.605564+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `1.5839` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.0111` n `13`; crypto_alt avg `0.1199` n `239`; crypto_major avg `0.3162` n `8`; equity avg `0.1692` n `162`; fx avg `-0.0193` n `6`; index avg `0.0171` n `27`; metal avg `0.0509` n `20`; unknown avg `-0.2941` n `1262`
- 1h: commodity avg `-0.0159` n `13`; crypto_alt avg `0.0246` n `239`; crypto_major avg `0.3862` n `8`; equity avg `0.44` n `162`; fx avg `-0.0384` n `6`; index avg `0.0397` n `27`; metal avg `0.0892` n `20`; unknown avg `-0.2801` n `1260`
- 4h: commodity avg `0.0918` n `13`; crypto_alt avg `1.8298` n `239`; crypto_major avg `1.4231` n `8`; equity avg `0.3582` n `162`; fx avg `0.0201` n `6`; index avg `0.035` n `27`; metal avg `-0.1608` n `20`; unknown avg `171.1211` n `1170`
- 24h: commodity avg `0.6975` n `13`; crypto_alt avg `-0.9957` n `239`; crypto_major avg `-2.9718` n `8`; equity avg `-1.4837` n `162`; fx avg `-0.0365` n `6`; index avg `-0.0084` n `27`; metal avg `-0.3621` n `20`; unknown avg `102.8154` n `1093`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1248`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1082`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0999`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0954`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0854`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0833`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0818`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.081`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0783`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.077`, n `668`, weak_sample_signal
