# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-25T16:37:29.041711+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0444` n `12`; crypto_alt avg `0.1452` n `231`; crypto_major avg `0.1133` n `8`; equity avg `-0.0109` n `122`; fx avg `0.0043` n `6`; index avg `0.0017` n `25`; metal avg `0.0256` n `20`; unknown avg `0.0292` n `795`
- 1h: commodity avg `0.1022` n `12`; crypto_alt avg `0.0802` n `231`; crypto_major avg `-0.0367` n `8`; equity avg `0.0019` n `122`; fx avg `0.0039` n `6`; index avg `-0.0011` n `25`; metal avg `-0.0151` n `20`; unknown avg `0.033` n `795`
- 4h: commodity avg `0.1143` n `12`; crypto_alt avg `0.0469` n `231`; crypto_major avg `0.3618` n `8`; equity avg `0.5678` n `122`; fx avg `0.0198` n `6`; index avg `-0.0231` n `25`; metal avg `0.2207` n `20`; unknown avg `-0.0201` n `795`
- 24h: commodity avg `-0.6193` n `12`; crypto_alt avg `-1.4891` n `231`; crypto_major avg `-0.5199` n `8`; equity avg `1.4378` n `122`; fx avg `0.0499` n `6`; index avg `0.1757` n `25`; metal avg `-0.1693` n `20`; unknown avg `-0.9295` n `777`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1385`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1136`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1051`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1042`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1035`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0931`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0863`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.08`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0787`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0754`, n `668`, weak_sample_signal
