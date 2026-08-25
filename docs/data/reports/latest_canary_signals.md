# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-25T16:22:28.729434+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0215` n `12`; crypto_alt avg `-0.2371` n `231`; crypto_major avg `-0.2331` n `8`; equity avg `-0.0688` n `122`; fx avg `-0.0062` n `6`; index avg `0.0004` n `25`; metal avg `-0.0411` n `20`; unknown avg `-0.0523` n `795`
- 1h: commodity avg `0.0168` n `12`; crypto_alt avg `0.0336` n `231`; crypto_major avg `0.0196` n `8`; equity avg `0.1478` n `122`; fx avg `-0.0165` n `6`; index avg `0.0328` n `25`; metal avg `0.0358` n `20`; unknown avg `0.0553` n `795`
- 4h: commodity avg `0.0066` n `12`; crypto_alt avg `0.0377` n `231`; crypto_major avg `0.4107` n `8`; equity avg `0.4212` n `122`; fx avg `0.0211` n `6`; index avg `-0.066` n `25`; metal avg `0.1472` n `20`; unknown avg `0.05` n `795`
- 24h: commodity avg `-0.6529` n `12`; crypto_alt avg `-1.7834` n `231`; crypto_major avg `-0.8943` n `8`; equity avg `1.3437` n `122`; fx avg `0.0392` n `6`; index avg `0.1653` n `25`; metal avg `-0.1947` n `20`; unknown avg `-0.9726` n `777`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1383`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1132`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1051`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1039`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1036`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.093`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0858`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0798`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0788`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0753`, n `668`, weak_sample_signal
