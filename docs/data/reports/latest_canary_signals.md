# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-30T19:37:37.945144+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0214` n `12`; crypto_alt avg `0.2109` n `234`; crypto_major avg `0.1529` n `8`; equity avg `-0.0227` n `142`; fx avg `0.0029` n `6`; index avg `-0.0097` n `26`; metal avg `-0.0087` n `20`; unknown avg `13.3671` n `969`
- 1h: commodity avg `-0.0819` n `12`; crypto_alt avg `0.1194` n `234`; crypto_major avg `0.1965` n `8`; equity avg `0.1384` n `142`; fx avg `0.0066` n `6`; index avg `0.0092` n `26`; metal avg `0.0367` n `20`; unknown avg `14.0692` n `967`
- 4h: commodity avg `-0.1212` n `12`; crypto_alt avg `-0.6011` n `234`; crypto_major avg `0.1326` n `8`; equity avg `-0.0966` n `142`; fx avg `-0.0249` n `6`; index avg `-0.0831` n `26`; metal avg `0.0364` n `20`; unknown avg `13.2896` n `961`
- 24h: commodity avg `0.3197` n `12`; crypto_alt avg `-0.0289` n `234`; crypto_major avg `0.5723` n `8`; equity avg `-0.1324` n `142`; fx avg `0.0638` n `6`; index avg `0.0205` n `26`; metal avg `-0.1842` n `20`; unknown avg `8.3998` n `820`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.134`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.131`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1231`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1095`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.108`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1013`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0903`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.087`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0858`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0798`, n `668`, weak_sample_signal
