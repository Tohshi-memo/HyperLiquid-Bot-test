# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-02T14:07:27.989237+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0734` n `13`; crypto_alt avg `-0.0659` n `239`; crypto_major avg `0.0375` n `8`; equity avg `-0.041` n `156`; fx avg `-0.0082` n `6`; index avg `0.0026` n `27`; metal avg `0.0398` n `20`; unknown avg `0.2015` n `1259`
- 1h: commodity avg `-0.3674` n `13`; crypto_alt avg `0.3857` n `238`; crypto_major avg `0.3505` n `8`; equity avg `0.2275` n `156`; fx avg `-0.0223` n `6`; index avg `0.0483` n `27`; metal avg `0.2466` n `20`; unknown avg `27.1552` n `1257`
- 4h: commodity avg `-0.3535` n `13`; crypto_alt avg `0.4343` n `238`; crypto_major avg `0.2433` n `8`; equity avg `-0.3905` n `156`; fx avg `-0.0195` n `6`; index avg `0.0158` n `27`; metal avg `0.2103` n `20`; unknown avg `3.6409` n `1250`
- 24h: commodity avg `-0.8813` n `13`; crypto_alt avg `-2.1314` n `238`; crypto_major avg `-0.5271` n `8`; equity avg `0.5239` n `156`; fx avg `0.2592` n `6`; index avg `0.2924` n `27`; metal avg `0.2327` n `20`; unknown avg `7.6117` n `1075`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1858`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1787`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1672`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1629`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.14`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1347`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1307`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1255`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1212`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1188`, n `668`, weak_sample_signal
