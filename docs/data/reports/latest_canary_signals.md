# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-12T05:07:26.395300+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0481` n `13`; crypto_alt avg `-0.1027` n `239`; crypto_major avg `-0.1975` n `8`; equity avg `-0.1619` n `161`; fx avg `-0.0218` n `6`; index avg `-0.0124` n `27`; metal avg `0.0108` n `20`; unknown avg `-0.0665` n `1258`
- 1h: commodity avg `-0.0275` n `13`; crypto_alt avg `-0.1547` n `239`; crypto_major avg `-0.3313` n `8`; equity avg `-0.5382` n `161`; fx avg `-0.009` n `6`; index avg `-0.0768` n `27`; metal avg `-0.0181` n `20`; unknown avg `0.4286` n `1246`
- 4h: commodity avg `-0.0817` n `13`; crypto_alt avg `-0.16` n `239`; crypto_major avg `-0.34` n `8`; equity avg `-0.2514` n `161`; fx avg `-0.1027` n `6`; index avg `-0.0194` n `27`; metal avg `-0.1249` n `20`; unknown avg `-0.0307` n `1236`
- 24h: commodity avg `0.083` n `13`; crypto_alt avg `-1.7018` n `239`; crypto_major avg `-0.5515` n `8`; equity avg `-0.0689` n `161`; fx avg `-0.2` n `6`; index avg `-0.0427` n `27`; metal avg `-0.4998` n `20`; unknown avg `-0.0704` n `1127`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1869`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1319`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.13`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1279`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1103`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1036`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0987`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0931`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0917`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0842`, n `668`, weak_sample_signal
