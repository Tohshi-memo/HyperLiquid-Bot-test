# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-08T02:52:26.659550+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0449` n `12`; crypto_alt avg `0.1293` n `228`; crypto_major avg `0.2261` n `8`; equity avg `0.2115` n `74`; fx avg `-0.0505` n `6`; index avg `-0.062` n `23`; metal avg `0.1267` n `18`; unknown avg `-0.0211` n `517`
- 1h: commodity avg `0.1428` n `12`; crypto_alt avg `0.0666` n `228`; crypto_major avg `0.4669` n `8`; equity avg `0.6933` n `74`; fx avg `0.0048` n `6`; index avg `0.2121` n `23`; metal avg `-0.0252` n `18`; unknown avg `-0.1878` n `517`
- 4h: commodity avg `0.1334` n `12`; crypto_alt avg `-0.4991` n `228`; crypto_major avg `0.3599` n `8`; equity avg `0.9439` n `74`; fx avg `-0.0401` n `6`; index avg `0.4375` n `23`; metal avg `-0.0654` n `18`; unknown avg `-0.4756` n `516`
- 24h: commodity avg `0.4107` n `12`; crypto_alt avg `1.2946` n `228`; crypto_major avg `3.8855` n `8`; equity avg `2.019` n `74`; fx avg `-0.0955` n `6`; index avg `0.5393` n `23`; metal avg `-0.0481` n `18`; unknown avg `-5.3124` n `506`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.1222`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1006`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.091`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0772`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0763`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0735`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0689`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.064`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0626`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0575`, n `668`, weak_sample_signal
