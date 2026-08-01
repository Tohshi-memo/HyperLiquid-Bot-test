# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-01T22:10:13.932861+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1337` n `12`; crypto_alt avg `0.0395` n `230`; crypto_major avg `0.0657` n `8`; equity avg `0.0093` n `102`; fx avg `0.0048` n `6`; index avg `-0.0019` n `25`; metal avg `0.0038` n `20`; unknown avg `0.1506` n `782`
- 1h: commodity avg `-0.1923` n `12`; crypto_alt avg `0.2806` n `230`; crypto_major avg `0.2229` n `8`; equity avg `0.3577` n `102`; fx avg `0.0268` n `6`; index avg `0.0453` n `25`; metal avg `0.035` n `20`; unknown avg `0.2101` n `782`
- 4h: commodity avg `-0.2468` n `12`; crypto_alt avg `-0.1712` n `230`; crypto_major avg `-0.089` n `8`; equity avg `0.2343` n `102`; fx avg `0.0309` n `6`; index avg `0.0244` n `25`; metal avg `0.0803` n `20`; unknown avg `0.0153` n `782`
- 24h: commodity avg `-0.1473` n `12`; crypto_alt avg `-0.2145` n `230`; crypto_major avg `-0.7046` n `8`; equity avg `-0.0215` n `102`; fx avg `-0.0198` n `6`; index avg `0.0085` n `25`; metal avg `0.0553` n `20`; unknown avg `0.0276` n `765`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1154`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0995`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0882`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0873`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0777`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0748`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0746`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0689`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0679`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0672`, n `668`, weak_sample_signal
