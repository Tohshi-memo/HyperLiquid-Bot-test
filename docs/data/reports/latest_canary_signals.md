# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-08T13:52:27.291857+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0021` n `12`; crypto_alt avg `-0.0205` n `230`; crypto_major avg `0.0377` n `8`; equity avg `-0.011` n `112`; fx avg `0.0` n `6`; index avg `-0.0096` n `25`; metal avg `-0.0042` n `20`; unknown avg `-0.0097` n `784`
- 1h: commodity avg `0.0517` n `12`; crypto_alt avg `-0.0331` n `230`; crypto_major avg `-0.0213` n `8`; equity avg `0.0935` n `112`; fx avg `-0.0076` n `6`; index avg `0.0117` n `25`; metal avg `-0.0016` n `20`; unknown avg `-0.1922` n `784`
- 4h: commodity avg `0.1118` n `12`; crypto_alt avg `0.247` n `230`; crypto_major avg `0.2463` n `8`; equity avg `0.2066` n `112`; fx avg `-0.0159` n `6`; index avg `0.0339` n `25`; metal avg `-0.0398` n `20`; unknown avg `-0.1203` n `784`
- 24h: commodity avg `0.0476` n `12`; crypto_alt avg `0.244` n `230`; crypto_major avg `-0.0076` n `8`; equity avg `0.9386` n `112`; fx avg `0.0011` n `6`; index avg `0.0389` n `25`; metal avg `-0.0135` n `20`; unknown avg `-0.1336` n `750`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1198`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0856`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0755`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0689`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0678`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0613`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0574`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0536`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0527`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0508`, n `668`, weak_sample_signal
