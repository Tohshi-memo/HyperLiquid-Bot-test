# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-10T05:37:30.631758+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0028` n `12`; crypto_alt avg `0.0896` n `230`; crypto_major avg `0.1376` n `8`; equity avg `-0.0469` n `112`; fx avg `-0.0053` n `6`; index avg `-0.0115` n `25`; metal avg `0.101` n `20`; unknown avg `1.0075` n `785`
- 1h: commodity avg `-0.0364` n `12`; crypto_alt avg `0.0469` n `230`; crypto_major avg `0.1708` n `8`; equity avg `-0.0352` n `112`; fx avg `0.018` n `6`; index avg `0.0212` n `25`; metal avg `0.0779` n `20`; unknown avg `-0.2724` n `785`
- 4h: commodity avg `-0.1089` n `12`; crypto_alt avg `0.1704` n `230`; crypto_major avg `0.318` n `8`; equity avg `-0.1111` n `112`; fx avg `0.0237` n `6`; index avg `0.0057` n `25`; metal avg `0.2673` n `20`; unknown avg `0.7141` n `785`
- 24h: commodity avg `0.2658` n `12`; crypto_alt avg `0.8944` n `230`; crypto_major avg `0.1888` n `8`; equity avg `-0.2856` n `112`; fx avg `0.1228` n `6`; index avg `0.0254` n `25`; metal avg `-0.0156` n `20`; unknown avg `-0.3007` n `752`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1948`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1415`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1412`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1268`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1185`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1118`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1054`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1006`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1005`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0986`, n `668`, weak_sample_signal
