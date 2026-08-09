# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-09T20:37:33.530019+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0031` n `12`; crypto_alt avg `0.0037` n `230`; crypto_major avg `0.037` n `8`; equity avg `0.0161` n `112`; fx avg `-0.0011` n `6`; index avg `0.0005` n `25`; metal avg `0.0077` n `20`; unknown avg `-0.1089` n `785`
- 1h: commodity avg `-0.0008` n `12`; crypto_alt avg `0.1206` n `230`; crypto_major avg `-0.0367` n `8`; equity avg `0.0294` n `112`; fx avg `0.0109` n `6`; index avg `-0.0093` n `25`; metal avg `0.0227` n `20`; unknown avg `-0.0288` n `785`
- 4h: commodity avg `0.1154` n `12`; crypto_alt avg `0.2985` n `230`; crypto_major avg `-0.1496` n `8`; equity avg `0.103` n `112`; fx avg `0.0054` n `6`; index avg `0.0199` n `25`; metal avg `0.0283` n `20`; unknown avg `-0.3431` n `785`
- 24h: commodity avg `0.0896` n `12`; crypto_alt avg `1.4345` n `230`; crypto_major avg `0.0979` n `8`; equity avg `0.2106` n `112`; fx avg `0.0128` n `6`; index avg `0.0239` n `25`; metal avg `0.1015` n `20`; unknown avg `-0.2839` n `752`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1523`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1081`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1005`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0967`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.078`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0723`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0717`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0635`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0635`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0584`, n `668`, weak_sample_signal
