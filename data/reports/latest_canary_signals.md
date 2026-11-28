# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-28T07:07:25.064564+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0125` n `13`; crypto_alt avg `-0.225` n `239`; crypto_major avg `-0.3926` n `8`; equity avg `-0.1105` n `168`; fx avg `0.0107` n `6`; index avg `-0.0064` n `27`; metal avg `-0.015` n `20`; unknown avg `174.7375` n `1251`
- 1h: commodity avg `-0.0093` n `13`; crypto_alt avg `0.2314` n `239`; crypto_major avg `-0.0801` n `8`; equity avg `0.0385` n `168`; fx avg `0.0023` n `6`; index avg `-0.0102` n `27`; metal avg `0.0215` n `20`; unknown avg `201.3648` n `1245`
- 4h: commodity avg `-0.0368` n `13`; crypto_alt avg `-1.5506` n `239`; crypto_major avg `-0.7811` n `8`; equity avg `-0.3289` n `168`; fx avg `0.0184` n `6`; index avg `-0.0508` n `27`; metal avg `-0.0368` n `20`; unknown avg `1.8432` n `1209`
- 24h: commodity avg `-0.869` n `13`; crypto_alt avg `-3.1872` n `239`; crypto_major avg `-2.9572` n `8`; equity avg `-0.3642` n `168`; fx avg `-0.098` n `6`; index avg `0.0047` n `27`; metal avg `-0.2964` n `20`; unknown avg `215.7102` n `969`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1489`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1478`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.1202`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0998`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0961`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0796`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0758`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0743`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.072`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0694`, n `668`, weak_sample_signal
